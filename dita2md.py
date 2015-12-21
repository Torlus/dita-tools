import sys
import os
import re
from xml.dom.minidom import parse

index_stack = []
column_stack = []
for n in range(0, 100):
    index_stack.append(0)
    column_stack.append(0)

full_path = str(os.path.abspath(sys.argv[1]))
base_name = str(os.path.basename(sys.argv[1]))
base_dir = full_path[0:len(full_path) - len(base_name)]
# print(full_path)
# print(base_dir)
# print(base_name)

root_tree = parse(full_path)


def echo(*args, **kwargs):
    print(*args, **kwargs)


def parse_conbody(depth, tree, **kwargs):
    global index_stack, column_stack
    html = True if 'html' in kwargs else False

    for nd in tree.childNodes:
        if nd.nodeType == nd.TEXT_NODE:
            text = nd.nodeValue.replace('\n', '')
            text = ' '.join(re.split('\s+', text))
            echo(text, end='')
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'p':
            echo()
            parse_conbody(depth, nd)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'ph':
            parse_conbody(depth, nd)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'codeph':
            echo('```')
            parse_conbody(depth, nd)
            echo()
            echo('```')
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'u':
            echo('<u>', end='')
            parse_conbody(depth, nd, html=True)
            echo('</u>', end='')
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'b':
            echo('<b>' if html else '**', end='')
            parse_conbody(depth, nd)
            echo('</b>' if html else '**', end='')
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'ul':
            echo()
            index_stack[depth + 1] = 0
            parse_conbody(depth + 1, nd)
            index_stack[depth + 1] = 0
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'ol':
            echo()
            index_stack[depth + 1] = 1
            parse_conbody(depth + 1, nd)
            index_stack[depth + 1] = 0
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'li':
            index = index_stack[depth]
            if index == 0:
                echo('* ', end='')
                parse_conbody(depth, nd)
            else:
                echo(str(index) + '. ', end='')
                index_stack[depth] = index + 1
                parse_conbody(depth, nd)
            echo()
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'table':
            parse_conbody(depth, nd)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'tgroup':
            parse_conbody(depth, nd)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'colspec':
            parse_conbody(depth, nd)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'tgroup':
            parse_conbody(depth, nd)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'thead':
            column_stack[depth + 1] = 1
            parse_conbody(depth + 1, nd)
            column_stack[depth + 1] = 0
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'tbody':
            parse_conbody(depth + 1, nd)
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'row':
            echo()
            echo('| ', end='')
            column_stack[depth + 1] = 0
            parse_conbody(depth + 1, nd)

            if column_stack[depth] == 1:
                echo()
                count = column_stack[depth + 1]
                for n in range(0, count):
                    echo('| - ', end='')
                echo('|', end='')

            column_stack[depth + 1] = 0
        elif nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'entry':
            column_stack[depth] += 1
            parse_conbody(depth, nd)
            echo('| ', end='')
        else:
            echo('parse_conbody - unhandled:', nd, file=sys.stderr)


def parse_concept(depth, tree):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'title':
            text = nd.firstChild.data.replace('\n', '').replace('\t', ' ')
            text = ' '.join(text.split(' '))
            for i in range(0, depth):
                print('#', end='')
            print('', text)
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'conbody':
            parse_conbody(depth, nd)
    print()


def parse_topicref_href(depth, tree):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'concept':
            parse_concept(depth + 1, nd)
    print()


def parse_topicref(depth, tree):
    parse_topicref_href(depth, parse(base_dir + tree.attributes['href'].value))
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'topicref':
            parse_topicref(depth + 1, nd)


def parse_map(depth, tree):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'topicref':
            parse_topicref(depth, nd)


def parse_root(depth, tree):
    for nd in tree.childNodes:
        if nd.nodeType == nd.ELEMENT_NODE and nd.nodeName == 'map':
            parse_map(depth, nd)

parse_root(0, root_tree)
