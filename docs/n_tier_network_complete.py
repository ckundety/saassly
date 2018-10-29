from graphviz import Digraph, nohtml

g = Digraph(name='n_tier_network_init',
            comment='N-tier netowrk before ledger creation',
            engine='circo')

# regulator or miner
g.node('CM')

# organizations
g.node('A')
g.node('B')
g.node('C')
g.node('D')
g.node('E')
g.node('F')
g.node('G')


# transactions
g.edge('CM', 'A', headlabel='F', anodesep='0.01')

g.edge('CM', 'B', headlabel='A')
g.edge('CM', 'B', headlabel='C')

g.edge('CM', 'C', headlabel='A')

g.edge('CM', 'D', headlabel='C')
g.edge('CM', 'D', headlabel='G')

g.edge('CM', 'E', headlabel='A')
g.edge('CM', 'E', headlabel='B')
g.edge('CM', 'E', headlabel='C')
g.edge('CM', 'E', headlabel='D')

g.edge('CM', 'F', headlabel='A')
g.edge('CM', 'F', headlabel='D')
g.edge('CM', 'F', headlabel='E')

g.edge('CM', 'G', headlabel='B')
g.edge('CM', 'G', headlabel='C')
g.edge('CM', 'G', headlabel='D')


# sales only ledgers
# , sales=['B', 'C', 'E', 'F'])
# , sales=['E', 'G'])
# , sales=['E', 'D', 'G', 'B'])
# , sales=['E', 'F', 'G'])
# , sales=['F'])
# , sales=[])
# , sales=['D'])

def sale(frm, tolst):
    return '\n'.join([frm + ' --> ' + i for i in tolst])


def purchase(to, frmlst):
    return '\n'.join([to + ' <-- ' + i for i in frmlst])


g.node('A-ledger',
       nohtml(sale('A', ['B', 'C', 'E', 'F'])) + '\n' + nohtml(purchase('A', ['F'])),
       shape='box')
g.node('B-ledger',
       nohtml(sale('B', ['E', 'G'])) + '\n' + nohtml(purchase('B', ['A', 'C'])),
       shape='box')
g.node('C-ledger',
       nohtml(sale('C', ['E', 'D', 'G', 'B'])) + '\n' + nohtml(purchase('C', ['A'])),
       shape='box')
g.node('D-ledger',
       nohtml(sale('D', ['E', 'F', 'G'])) + '\n' + nohtml(purchase('D', ['C', 'G'])),
       shape='box')
g.node('E-ledger',
       nohtml(sale('E', ['F'])) + '\n' + nohtml(purchase('E', ['A', 'B', 'C', 'D'])),
       shape='box')
g.node('F-ledger',
       nohtml(sale('F', [])) + '\n' + nohtml(purchase('F', ['A', 'D', 'E'])),
       shape='box')
g.node('G-ledger',
       nohtml(sale('G', ['D'])) + '\n' + nohtml(purchase('G', ['B', 'C', 'D'])),
       shape='box')

g.edge('A', 'A-ledger', style='dashed')
g.edge('B', 'B-ledger', style='dashed')
g.edge('C', 'C-ledger', style='dashed')
g.edge('D', 'D-ledger', style='dashed')
g.edge('E', 'E-ledger', style='dashed')
g.edge('F', 'F-ledger', style='dashed')
g.edge('G', 'G-ledger', style='dashed')


g.render('n_tier_network_complete.gv', view=True)
