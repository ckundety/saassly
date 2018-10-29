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

def to_table(node, lst):
    def build_tr(i):
        return '<TR><TD>' + f'{node} to {i}' + '</TD></TR>'

    trows = [build_tr(s) for s in lst]
    tab = '<\n<TABLE>' + ''.join(trows) + '</TABLE>\n>'
    return tab


def to_label(frm, tolst):
    return '\n'.join([frm + ' --> ' + i for i in tolst])


g.node('A-ledger', nohtml(to_table('A', ['B', 'C', 'E', 'F'])), shape='box')
g.node('B-ledger', nohtml(to_table('B', ['E', 'G'])), shape='box')
g.node('C-ledger', nohtml(to_table('C', ['E', 'D', 'G', 'B'])), shape='box')
g.node('D-ledger', nohtml(to_table('D', ['E', 'F', 'G'])), shape='box')
g.node('E-ledger', nohtml(to_table('E', ['F'])), shape='box')
g.node('F-ledger', nohtml(to_table('F', [])), shape='box')
g.node('G-ledger', nohtml(to_table('G', ['D'])), shape='box')

g.edge('A', 'A-ledger', style='dashed')
g.edge('B', 'B-ledger', style='dashed')
g.edge('C', 'C-ledger', style='dashed')
g.edge('D', 'D-ledger', style='dashed')
g.edge('E', 'E-ledger', style='dashed')
g.edge('F', 'F-ledger', style='dashed')
g.edge('G', 'G-ledger', style='dashed')


g.render('n_tier_network_init.gv', view=True)
