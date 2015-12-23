import sys
import os
import re
import html
from xml.dom.minidom import parse

index_stack = []
column_stack = []
for n in range(0, 100):
    index_stack.append(0)
    column_stack.append(0)

full_path = str(os.path.abspath(sys.argv[1]))
base_name = str(os.path.basename(sys.argv[1]))
base_dir = full_path[0:len(full_path) - len(base_name)]

root_tree = parse(full_path)


def echo(*args, **kwargs):
    indent = int(kwargs['indent']) if 'indent' in kwargs else None
    start = kwargs['start'] if 'start' in kwargs else None
    if start is not None:
        print()
        del kwargs['start']
    if indent is not None:
        for n in range(0, indent - 1):
            print(' ', sep='', end='')
        del kwargs['indent']
    print(*args, **kwargs)


def parse_conbody(depth, tree, **kwargs):
    global index_stack, column_stack
    # html = kwargs['html'] if 'html' in kwargs else False
    for nd in tree.childNodes:
        if nd.nodeType == nd.TEXT_NODE:
            text = nd.nodeValue.replace('\n', '')
            text = ' '.join(re.split('\s+', text))
            echo(html.escape(text), end='')
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'p':
            echo('<p>', indent=depth)
            parse_conbody(depth, nd, **kwargs)
            echo('</p>', start='\n', indent=depth)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'ph':
            parse_conbody(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'codeph':
            echo('<code>', indent=depth)
            parse_conbody(depth, nd, **kwargs)
            echo('</code>', start='\n', indent=depth)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'u':
            echo('<u>', start=' ', end='')
            parse_conbody(depth, nd, **kwargs)
            echo('</u>', end='')
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'b':
            echo('<b>', start=' ', end='')
            parse_conbody(depth, nd, **kwargs)
            echo('</b>', end='')
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'ul':
            echo('<ul>', indent=depth)
            index_stack[depth + 1] = 0
            parse_conbody(depth + 1, nd, **kwargs)
            index_stack[depth + 1] = 0
            echo('</ul>', start='\n', indent=depth)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'ol':
            echo('<ol>', indent=depth)
            index_stack[depth + 1] = 1
            parse_conbody(depth + 1, nd, **kwargs)
            index_stack[depth + 1] = 0
            echo('</ol>', start='\n', indent=depth)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'li':
            index = index_stack[depth]
            echo('<li>', indent=depth)
            if index > 0:
                index_stack[depth] = index + 1
            parse_conbody(depth, nd, **kwargs)
            echo('</li>', start='\n', indent=depth)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'table':
            echo('<table>', indent=depth)
            parse_conbody(depth, nd, **kwargs)
            echo('</table>', start='\n', indent=depth)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'tgroup':
            parse_conbody(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'colspec':
            parse_conbody(depth, nd, **kwargs)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'thead':
            column_stack[depth + 1] = 1
            parse_conbody(depth + 1, nd, **kwargs)
            column_stack[depth + 1] = 0
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'tbody':
            column_stack[depth + 1] = 1
            parse_conbody(depth + 1, nd, **kwargs)
            column_stack[depth + 1] = 1
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'row':
            echo('<tr>', indent=depth)
            column_stack[depth + 1] = 0
            parse_conbody(depth + 1, nd, **kwargs)
            column_stack[depth + 1] = 0
            echo('</tr>', start='\n', indent=depth)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'entry':
            echo('<td>', indent=depth)
            column_stack[depth] += 1
            parse_conbody(depth, nd, **kwargs)
            echo('</td>', start='\n', indent=depth)
        elif nd.nodeType == nd.COMMENT_NODE:
            pass
        else:
            echo(kwargs['file_name'], 'parse_conbody - unhandled:', nd, file=sys.stderr)


def parse_concept(depth, tree, **kwargs):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'title':
            echo('<h' + str(depth) + '>', indent=depth)
            echo(html.escape(nd.firstChild.data), indent=depth)
            print('</h' + str(depth) + '>')
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'conbody':
            parse_conbody(depth, nd, **kwargs)


def parse_topicref_href(depth, tree, **kwargs):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'concept':
            parse_concept(depth + 1, nd, **kwargs)


def parse_topicref(depth, tree, **kwargs):
    file_name = tree.attributes['href'].value
    kwargs['file_name'] = file_name
    echo('<!-- ' + file_name + ' -->')
    parse_topicref_href(depth, parse(base_dir + file_name), **kwargs)
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'topicref':
            parse_topicref(depth + 1, nd, **kwargs)


def parse_map(depth, tree, **kwargs):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'topicref':
            parse_topicref(depth, nd, **kwargs)


def parse_root(depth, tree, **kwargs):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'map':
            parse_map(depth, nd, **kwargs)

echo('<!DOCTYPE html>', '<html>', '<head>', '<meta charset="UTF-8">', '</head>', '<body>')
parse_root(0, root_tree, file_name=base_name)
echo('</body>', '</html>')
