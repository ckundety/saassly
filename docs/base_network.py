from graphviz import Digraph, nohtml

g = Digraph(name='base_network',
            comment='SaaS network',
            engine='circo')

g.node('A')
g.node('B')
g.node('C')
g.node('D')
g.node('E')
g.node('F')
g.node('G')

g.edge('F', 'A')

g.edge('A', 'B')
g.edge('C', 'B')

g.edge('A', 'C')

g.edge('G', 'D')
g.edge('C', 'D')

g.edge('A', 'E')
g.edge('B', 'E')
g.edge('C', 'E')
g.edge('D', 'E')

g.edge('A', 'F')
g.edge('D', 'F')
g.edge('E', 'F')


g.edge('D', 'G')
g.edge('C', 'G')
g.edge('B', 'G')


g.render('base_network.gv', view=True)


def to_label(frm, tolst):
    return '\n'.join([frm + ' --> ' + i for i in tolst])


g.node('A-ledger', nohtml(to_label('A', ['B', 'C', 'E', 'F'])), shape='box')
g.node('B-ledger', nohtml(to_label('B', ['E', 'G'])), shape='box')
g.node('C-ledger', nohtml(to_label('C', ['E', 'D', 'G', 'B'])), shape='box')
g.node('D-ledger', nohtml(to_label('D', ['E', 'F', 'G'])), shape='box')
g.node('E-ledger', nohtml(to_label('E', ['F'])), shape='box')
g.node('F-ledger', nohtml(to_label('F', [])), shape='box')
g.node('G-ledger', nohtml(to_label('G', ['D'])), shape='box')

g.edge('A', 'A-ledger', style='dashed')
g.edge('B', 'B-ledger', style='dashed')
g.edge('C', 'C-ledger', style='dashed')
g.edge('D', 'D-ledger', style='dashed')
g.edge('E', 'E-ledger', style='dashed')
g.edge('F', 'F-ledger', style='dashed')
g.edge('G', 'G-ledger', style='dashed')

g.render('base_network_sale_ledgers.gv', view=True)
