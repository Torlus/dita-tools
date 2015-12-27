import sys
import os
import re
import html
from xml.dom.minidom import parse

if len(sys.argv) < 3:
    print('Usage:', sys.argv[0], '<root_file>', '<ditaval> [<out_directory>]', file=sys.stderr)
    exit(-1)

chapter_stack = []
index_stack = []
column_stack = []
for n in range(0, 100):
    chapter_stack.append(0)
    index_stack.append(0)
    column_stack.append(0)

full_path = str(os.path.abspath(sys.argv[1]))
base_name = str(os.path.basename(sys.argv[1]))
base_dir = full_path[0:len(full_path) - len(base_name)]

out_dir = sys.argv[3] if len(sys.argv) > 3 else None

ditavals = {}
keydefs = {}

keys = ''

current_file = sys.stdout
if out_dir is not None:
    current_file = open(out_dir + '/' + 'chap-1.md', 'w')

img_dir = base_dir
if out_dir is not None:
    img_dir = '/docs_img/'


def parse_ditaval(tree):
    global ditavals
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'val':
            parse_ditaval(nd)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'prop':
            att = None
            val = None
            if nd.hasAttribute('att'):
                att = nd.attributes['att'].value
            if nd.hasAttribute('val'):
                val = nd.attributes['val'].value
            if att is not None and val is not None:
                # print(att, val, file=sys.stderr)
                ditavals[att] = val
        elif nd.nodeType != nd.ELEMENT_NODE:
            pass
        else:
            print('parse_ditaval - unhandled:', nd, file=sys.stderr)


ditaval_tree = parse(sys.argv[2])
parse_ditaval(ditaval_tree)

print('ditavals:', ditavals, file=sys.stderr)

root_tree = parse(full_path)


def expand_keydef(nd):
    key = nd.attributes['keyref'].value
    if key in keydefs:
        val = keydefs[key]
        if 'text' in val:
            echo(val['text'], end='')
        else:
            fmt = val['format']
            if fmt == 'image':
                echo('<img src="', img_dir + val['href'], '" alt="', key, '"/>', sep='', end='')
            elif fmt == 'mail':
                echo('<a href="mailto:', val['href'], '">', val['href'], '</a>', sep='', end='')
            elif fmt == 'html':
                echo('<a href="', val['href'], '">', val['href'], '</a>', sep='', end='')
            else:
                print('expand_keydef - format:', fmt, file=sys.stderr)


def echo(*args, **kwargs):
    global current_file
    indent = int(kwargs['indent']) if 'indent' in kwargs else None
    start = kwargs['start'] if 'start' in kwargs else None
    if start is not None:
        print(file=current_file)
        del kwargs['start']
    if indent is not None:
        for n in range(0, indent - 1):
            print(' ', sep='', end='', file=current_file)
        del kwargs['indent']
    print(*args, **kwargs, file=current_file)


def filter_val(nd):
    for att in ditavals:
        val = ditavals[att]
        if nd.hasAttribute(att):
            vals = nd.attributes[att].value.split(' ')
            # print(vals, val, file=sys.stderr)
            if val not in vals:
                return True
    return False


def parse_fig(depth, tree, **kwargs):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'title':
            echo('<p>', start='\n', indent=depth)
            parse_conbody(depth, nd, **kwargs)
            echo('</p>', start='\n', indent=depth)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'image':
            if nd.hasAttribute('keyref'):
                expand_keydef(nd)
            else:
                url = nd.attributes['href'].value
                echo('<img src="', img_dir + url, '" alt="', url, '"/>', sep='', end='')
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'p':
            pass
        elif nd.nodeType != nd.ELEMENT_NODE:
            pass
        else:
            print(kwargs['file_name'], 'parse_fig - unhandled:', nd, file=sys.stderr)


def parse_conbody(depth, tree, **kwargs):
    global index_stack, column_stack
    for nd in tree.childNodes:
        if nd.nodeType == nd.TEXT_NODE:
            code = kwargs['code'] if 'code' in kwargs else False
            if code:
                text = nd.nodeValue
            else:
                text = nd.nodeValue.replace('\n', '')
                text = ' '.join(re.split('\s+', text))
            echo(html.escape(text), end='')
        elif nd.nodeType == nd.ELEMENT_NODE:
            if filter_val(nd):
                return
            if nd.nodeName == 'p':
                echo('<p>', start='\n', indent=depth)
                parse_conbody(depth, nd, **kwargs)
                echo('</p>', start='\n', indent=depth)
            elif nd.nodeName == 'title':
                pass
            elif nd.nodeName == 'codeblock':
                kwargs['code'] = True
                echo('<code><pre>', indent=depth)
                parse_conbody(depth, nd, **kwargs)
                echo('</pre></code>', start='\n', indent=depth)
            elif nd.nodeName == 'itemgroup':
                echo('<p>', start='\n', indent=depth)
                parse_conbody(depth, nd, **kwargs)
                echo('</p>', start='\n', indent=depth)
            elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'image':
                if nd.hasAttribute('keyref'):
                    expand_keydef(nd)
                else:
                    url = nd.attributes['href'].value
                    echo('<img src="', img_dir + url, '" alt="', url, '"/>', sep='', end='')
            elif nd.nodeName == 'keyword':
                expand_keydef(nd)
            elif nd.nodeName == 'xref':
                if nd.hasAttribute('href'):
                    echo('<a href="#TODO-', nd.attributes['href'].value, '">', sep='', end='')
                    parse_conbody(depth, nd, **kwargs)
                    echo('</a>', end='')
                else:
                    expand_keydef(nd)
            elif nd.nodeName == 'fig':
                parse_fig(depth, nd, **kwargs)
            elif nd.nodeName == 'ph':
                parse_conbody(depth, nd, **kwargs)
            elif nd.nodeName == 'codeph':
                kwargs['code'] = True
                echo('<code><pre>', indent=depth)
                parse_conbody(depth, nd, **kwargs)
                echo('</pre></code>', start='\n', indent=depth)
            elif nd.nodeName == 'u':
                echo('<u>', start=' ', end='')
                parse_conbody(depth, nd, **kwargs)
                echo('</u>', end='')
            elif nd.nodeName == 'b':
                echo('<b>', start=' ', end='')
                parse_conbody(depth, nd, **kwargs)
                echo('</b>', end='')
            elif nd.nodeName == 'i':
                echo('<i>', start=' ', end='')
                parse_conbody(depth, nd, **kwargs)
                echo('</i>', end='')
            elif nd.nodeName == 'ul':
                echo('<ul>', start='\n', indent=depth)
                index_stack[depth + 1] = 0
                parse_conbody(depth + 1, nd, **kwargs)
                index_stack[depth + 1] = 0
                echo('</ul>', start='\n', indent=depth)
            elif nd.nodeName == 'ol':
                echo('<ol>', start='\n', indent=depth)
                index_stack[depth + 1] = 1
                parse_conbody(depth + 1, nd, **kwargs)
                index_stack[depth + 1] = 0
                echo('</ol>', start='\n', indent=depth)
            elif nd.nodeName == 'li':
                index = index_stack[depth]
                echo('<li>', start='\n', indent=depth)
                if index > 0:
                    index_stack[depth] = index + 1
                parse_conbody(depth, nd, **kwargs)
                echo('</li>', start='\n', indent=depth)
            elif nd.nodeName == 'table':
                echo('<table>', start='\n', indent=depth)
                parse_conbody(depth, nd, **kwargs)
                echo('</table>', start='\n', indent=depth)
            elif nd.nodeName == 'tgroup':
                parse_conbody(depth, nd, **kwargs)
            elif nd.nodeName == 'colspec':
                parse_conbody(depth, nd, **kwargs)
            elif nd.nodeName == 'thead':
                column_stack[depth + 1] = 1
                parse_conbody(depth + 1, nd, **kwargs)
                column_stack[depth + 1] = 0
            elif nd.nodeName == 'tbody':
                column_stack[depth + 1] = 1
                parse_conbody(depth + 1, nd, **kwargs)
                column_stack[depth + 1] = 1
            elif nd.nodeName == 'row':
                echo('<tr>', start='\n', indent=depth)
                column_stack[depth + 1] = 0
                parse_conbody(depth + 1, nd, **kwargs)
                column_stack[depth + 1] = 0
                echo('</tr>', start='\n', indent=depth)
            elif nd.nodeName == 'entry':
                echo('<td>', start='\n', indent=depth)
                column_stack[depth] += 1
                parse_conbody(depth, nd, **kwargs)
                echo('</td>', start='\n', indent=depth)
            # Task-related stuff
            elif nd.nodeName == 'context':
                parse_conbody(depth, nd, **kwargs)
            elif nd.nodeName == 'steps':
                echo('<ol>', start='\n', indent=depth)
                index_stack[depth + 1] = 1
                parse_conbody(depth + 1, nd, **kwargs)
                index_stack[depth + 1] = 0
                echo('</ol>', start='\n', indent=depth)
            elif nd.nodeName == 'step':
                index = index_stack[depth]
                echo('<li>', start='\n', indent=depth)
                if index > 0:
                    index_stack[depth] = index + 1
                parse_conbody(depth, nd, **kwargs)
                echo('</li>', start='\n', indent=depth)
            elif nd.nodeName == 'choices':
                echo('<ul>', start='\n', indent=depth)
                index_stack[depth + 1] = 0
                parse_conbody(depth + 1, nd, **kwargs)
                index_stack[depth + 1] = 0
                echo('</ul>', start='\n', indent=depth)
            elif nd.nodeName == 'choice':
                index = index_stack[depth]
                echo('<li>', start='\n', indent=depth)
                if index > 0:
                    index_stack[depth] = index + 1
                parse_conbody(depth, nd, **kwargs)
                echo('</li>', start='\n', indent=depth)
            elif nd.nodeName == 'cmd':
                echo('<p>', start='\n', indent=depth)
                parse_conbody(depth, nd, **kwargs)
                echo('</p>', start='\n', indent=depth)
            elif nd.nodeName == 'info':
                echo('<p>', start='\n', indent=depth)
                parse_conbody(depth, nd, **kwargs)
                echo('</p>', start='\n', indent=depth)
            elif nd.nodeName == 'result':
                echo('<p>', start='\n', indent=depth)
                parse_conbody(depth, nd, **kwargs)
                echo('</p>', start='\n', indent=depth)
            elif nd.nodeName == 'postreq':
                echo('<p>', start='\n', indent=depth)
                parse_conbody(depth, nd, **kwargs)
                echo('</p>', start='\n', indent=depth)
            # Reference-related stuff
            elif nd.nodeName == 'section':
                parse_conbody(depth, nd, **kwargs)
            else:
                print(kwargs['file_name'], 'parse_conbody - unhandled Element:', nd, file=sys.stderr)

        elif nd.nodeType in [nd.COMMENT_NODE, nd.DOCUMENT_TYPE_NODE]:
            pass
        else:
            print(kwargs['file_name'], 'parse_conbody - unhandled NodeType:', nd, file=sys.stderr)


def parse_concept(depth, tree, **kwargs):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'title':
            echo('<h' + str(depth + 1) + '>', indent=depth)
            for c in range(0, depth + 1):
                echo(str(chapter_stack[c]) + '.', end='')
            echo(' ', end='')
            text = html.escape(nd.firstChild.data)
            echo(text, indent=depth)
            echo('</h' + str(depth + 1) + '>')
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'conbody':
            parse_conbody(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'taskbody':
            parse_conbody(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'refbody':
            parse_conbody(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'shortdesc':
            parse_conbody(depth, nd, **kwargs)
        elif nd.nodeType != nd.ELEMENT_NODE:
            pass
        else:
            print(kwargs['file_name'], 'parse_concept - unhandled:', nd, file=sys.stderr)


def parse_topicref_href(depth, tree, **kwargs):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'concept':
            parse_concept(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'task':
            parse_concept(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'reference':
            parse_concept(depth, nd, **kwargs)
        elif nd.nodeType != nd.ELEMENT_NODE:
            pass
        else:
            print(kwargs['file_name'], 'parse_topicref_href - unhandled:', nd, file=sys.stderr)


def parse_topicref(depth, tree, **kwargs):
    global current_file
    file_name = tree.attributes['href'].value
    kwargs['file_name'] = file_name
    echo('<!-- ' + file_name + ' -->')
    chapter_stack[depth] += 1
    if depth == 0:
        if out_dir is not None:
            current_file.close()
            fn = 'chap-' + str(chapter_stack[0])
            # echo('{% include ' + fn + ' %}')
            current_file = open(out_dir + '/' + fn + '.md', 'w')
            echo('---')
            echo('layout: docs')
            echo('permalink: /docs/' + fn + '/')
            echo('title: ' + fn)
            echo('---')
        # echo('<section>')

    parse_topicref_href(depth, parse(base_dir + file_name), **kwargs)
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'topicref':
            parse_topicref(depth + 1, nd, **kwargs)
        elif nd.nodeType != nd.ELEMENT_NODE:
            pass
        else:
            print(kwargs['file_name'], 'parse_topicref - unhandled:', nd, file=sys.stderr)
    chapter_stack[depth + 1] = 0

    if depth == 1:
        pass
        # echo('</section>')


def parse_mapref(depth, tree, **kwargs):
    file_name = tree.attributes['href'].value
    kwargs['file_name'] = file_name
    echo('<!-- ' + file_name + ' -->')
    parse_map(depth, parse(base_dir + file_name), **kwargs)
    for nd in tree.childNodes:
        if nd.nodeType != nd.ELEMENT_NODE:
            pass
        else:
            print(kwargs['file_name'], 'parse_mapref - unhandled:', nd, file=sys.stderr)


def parse_keydef(depth, tree, **kwargs):
    global keys, keydefs
    if tree.nodeName == 'keyword':
        val = ''
        for nd in tree.childNodes:
            if nd.nodeType == nd.TEXT_NODE:
                text = nd.nodeValue.replace('\n', '')
                text = ' '.join(re.split('\s+', text))
                val += html.escape(text)
        keydefs[keys] = {'text': val}
    if tree.nodeName == 'keydef':
        keys = tree.attributes['keys'].value
        if tree.hasAttribute('format'):
            fmt = tree.attributes['format'].value
            href = tree.attributes['href'].value
            keydefs[keys] = {'format': fmt, 'href': href}
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE:
            parse_keydef(depth, nd, **kwargs)


def parse_map(depth, tree, **kwargs):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'topicref':
            parse_topicref(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'mapref':
            parse_mapref(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'map':
            parse_map(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'keydef':
            if not filter_val(nd):
                parse_keydef(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'title':
            parse_map(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'topicmeta':
            parse_map(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'searchtitle':
            parse_map(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'prodname':
            parse_map(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'prodinfo':
            parse_map(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'vrmlist':
            parse_map(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'vrm':
            parse_map(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'keyword':
            parse_map(depth, nd, **kwargs)
        elif nd.nodeType != nd.ELEMENT_NODE:
            pass
        else:
            print(kwargs['file_name'], 'parse_map - unhandled:', nd, file=sys.stderr)


def parse_root(depth, tree, **kwargs):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'map':
            parse_map(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'mapref':
            if filter_val(nd):
                return
            file_name = tree.attributes['href'].value
            kwargs['file_name'] = file_name
            echo('<!-- ' + file_name + ' -->')
            parse_map(depth, parse(base_dir + file_name), **kwargs)
        elif nd.nodeType != nd.ELEMENT_NODE:
            pass
        else:
            print('<root>', 'parse_root - unhandled:', nd, file=sys.stderr)

if out_dir is not None:
    parse_root(0, root_tree, file_name=base_name)
else:
    echo('<!DOCTYPE html>', '<html>', '<head>', '<meta charset="UTF-8">', '</head>', '<body>')
    parse_root(0, root_tree, file_name=base_name)
    echo('</body>', '</html>')

# print(keydefs, file=sys.stderr)

