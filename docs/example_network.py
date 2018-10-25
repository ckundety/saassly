from graphviz import Digraph

g = Digraph(comment='An example SaaS network',
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


g.render('example_network.gv', view=True)
