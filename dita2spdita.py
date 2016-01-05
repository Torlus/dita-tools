import sys
import os
import re
import html
from xml.dom.minidom import Document, parse

if len(sys.argv) < 3:
    print('Usage:', sys.argv[0], '<root_file>', '<ditaval> [<out_directory>]', file=sys.stderr)
    exit(-1)

full_path = str(os.path.abspath(sys.argv[1]))
base_name = str(os.path.basename(sys.argv[1]))
base_dir = full_path[0:len(full_path) - len(base_name)]

out_dir = sys.argv[3] if len(sys.argv) > 3 else None

ditavals = {}
keydefs = {}

chapter_stack = []
index_stack = []
column_stack = []
for n in range(0, 100):
    chapter_stack.append(0)
    index_stack.append(0)
    column_stack.append(0)

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

# print('ditavals:', ditavals, file=sys.stderr)

root_tree = parse(full_path)


def expand_keydef(nd):
    key = nd.attributes['keyref'].value
    # print('keydef:', key)
    if key in keydefs:
        val = keydefs[key]
        # print(val)
        if 'text' in val:
            echo(val['text'], end='')
        else:
            fmt = val['format']
            if fmt == 'image':
                echo('<img src="', img_dir + val['href'], '" alt="', key, '"/>', sep='', end='')
            elif fmt == 'mail':
                echo('<a href="mailto:', val['href'], '">', val['href'], '</a>', sep='', end='')
            elif fmt == 'html':
                # print('html', val['href'], file=sys.stderr)
                echo('<a href="', val['href'], '">', val['href'], '</a>', sep='', end='')
            else:
                print('expand_keydef - format:', fmt, file=sys.stderr)
    else:
        print(key, 'not found in keydefs', file=sys.stderr)


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


def parse_body(depth, tree, **kwargs):
    root = not kwargs['child'] if 'child' in kwargs else True
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE:
            if filter_val(nd):
                tree.removeChild(nd)
            else:
                kwargs['child'] = True
                parse_body(depth, nd, **kwargs)
        elif nd.nodeType == nd.PROCESSING_INSTRUCTION_NODE:
            tree.removeChild(nd)
    if root:
        echo(tree.toxml())


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

    parse_body(depth, parse(base_dir + file_name), **kwargs)

    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE:
            if nd.nodeName in ['topicref']:
                parse_topicref(depth + 1, nd, **kwargs)
        elif nd.nodeType == nd.PROCESSING_INSTRUCTION_NODE:
            tree.removeChild(nd)

    chapter_stack[depth + 1] = 0

    if depth == 1:
        pass
        # echo('</section>')


def parse_mapref(depth, tree, **kwargs):
    file_name = tree.attributes['href'].value
    kwargs['file_name'] = file_name
    echo('<!-- ' + file_name + ' -->')
    parse_map(depth, parse(base_dir + file_name), **kwargs)


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
        elif nd.nodeType == nd.PROCESSING_INSTRUCTION_NODE:
            tree.removeChild(nd)


def parse_map(depth, tree, **kwargs):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE:
            if nd.nodeName in ['topicref']:
                parse_topicref(depth, nd, **kwargs)
            elif nd.nodeName in ['keydef']:
                if not filter_val(nd):
                    parse_keydef(depth, nd, **kwargs)
            else:
                parse_map(depth, nd, **kwargs)
        elif nd.nodeType == nd.PROCESSING_INSTRUCTION_NODE:
            tree.removeChild(nd)


def parse_root(depth, tree, **kwargs):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE:
            if nd.nodeName in ['map']:
                parse_map(depth, nd, **kwargs)
            elif nd.nodeName in ['mapref']:
                if filter_val(nd):
                    continue
                file_name = tree.attributes['href'].value
                kwargs['file_name'] = file_name
                echo('<!-- ' + file_name + ' -->')
                parse_map(depth, parse(base_dir + file_name), **kwargs)
        elif nd.nodeType == nd.PROCESSING_INSTRUCTION_NODE:
            tree.removeChild(nd)

if out_dir is not None:
    parse_root(0, root_tree, file_name=base_name)
else:
    echo('<!DOCTYPE html>', '<html>', '<head>', '<meta charset="UTF-8">', '</head>', '<body>')
    parse_root(0, root_tree, file_name=base_name)
    echo('</body>', '</html>')

# print(keydefs, file=sys.stderr)

