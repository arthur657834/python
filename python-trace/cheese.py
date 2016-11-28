from __future__ import unicode_literals

import os
import sys
import hashlib
import pygraphviz as pgv


def get_id(node):
    raw_str = '{0}:{1}:{2}'.format(
        node['filename'],
        node['firstlineno'],
        node['name']
    )
    return hashlib.sha1(raw_str).hexdigest()


def which_contains(node):
    return node['filename']


def what_names(node):
    return node['name']


def where_locates(node):
    return node['firstlineno']


def where_jumped(node):
    return node['lineno']


def extract_callstack(frame):
    ret = []

    while frame:
        filename = frame.f_code.co_filename
        firstlineno = frame.f_code.co_firstlineno
        name = frame.f_code.co_name
        lineno = frame.f_lineno

        ret.append({
            'filename': os.path.abspath(filename),
            'firstlineno': firstlineno,
            'name': name,
            'lineno': lineno
        })

        frame = frame.f_back

    return reversed(ret)


def add_subgraph(graph, subgraphs, subgraph):
    if subgraph not in subgraphs:
        pgv_ins = graph.add_subgraph(
            name='cluster' + subgraph,
            label=subgraph
        )
        subgraphs[subgraph] = (pgv_ins, set())


def add_node(graph, subgraphs, node):
    subgraph = which_contains(node)
    add_subgraph(graph, subgraphs, subgraph)

    node_id = get_id(node)
    if node_id not in subgraphs[subgraph][1]:
        subgraphs[subgraph][0].add_node(
            node_id,
            label='{0}:{1}'.format(where_locates(node), what_names(node))
        )
        subgraphs[subgraph][1].add(node_id)


def add_edge(graph, subgraphs, start, end, index):
    add_node(graph, subgraphs, start)
    add_node(graph, subgraphs, end)

    start_id = get_id(start)
    end_id = get_id(end)

    graph.add_edge(
        start_id,
        end_id,
        label='#{0} at {1}'.format(index + 1, where_jumped(start))
    )


def take_frame(frame=None, out=None):
    if not frame:
        frame = sys._getframe().f_back

    call_stack = list(extract_callstack(frame))
    graph = pgv.AGraph(strict=False, directed=True)
    subgraphs = {}

    for index, start in enumerate(call_stack[:-1]):
        end = call_stack[index + 1]
        add_edge(graph, subgraphs, start, end, index)

    if out:
        graph.draw(out, prog='dot')
        graph.close()
    else:
        return graph