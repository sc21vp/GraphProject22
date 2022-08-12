from main import Graph
from ring import isRing
from mcs import MCS,cliqueCutsets
from longhole import containsHole
from typing import List
from graph_check import isW54Graph,isK23Graph,isC6ComplementGraph

connections=[('a', 'b'),
                   ('a', 'd'),('a','c'), ('b', 'd'),('b', 'e'),('c','d'),('c','g'),('e', 'f'),  ('e', 'h')
                   ,('f','h'),('f','g'),('g','h')] ## twin partition


connections1=[('a', 'c'),
                   ('a', 'd'),('a','f'), ('b', 'c'),('b', 'g'),('c','h'),('c','f'),('c', 'd'),  ('d', 'e')
                   ,('d','i'),('d','f'),('e','j'),('g','h'),('h','k'),('k','i'),('i','j')]

g = Graph(connections1)


## total time complexity for iterating over all leafs of the graph and checking for all  O(n^)
#operation include:
# 1)checking Graph G is (k2,3,c6 complement, w54)-free graph
# 2)Finding leafs of the graph 
# 3)Get anticomponents of corresponding leaf.
# 4)For each anticomponents check whether it is a long ring or containsHole or contains stable numbert<=2.
#  Total time O(n^6)  
def isGutGraph(g:Graph):
 if(isW54Graph(g) or  isK23Graph(g) or isC6ComplementGraph(g)):
     return False
 order,fillin_graph, clique_gen=MCS(g)
 leafs,clique_sptr=cliqueCutsets(g,fillin_graph,clique_gen,order)
 print("clique separators::",clique_sptr)
 for leaf_g in leafs:
        ## for obtaiing anitcomponents:
        ## complement of graph 
        conn=leaf_g.complement()
        if(len(conn)==0): ## stable set will be 1
            continue
        comp_leaf=Graph(conn)
        visited=[]
        anticomponents:List[Graph]=[]
        ## we get every connected component from complement graph using BFS and we do complement of that
        ## component to form anitcomponent of graph G.)(n**2)
        for u in comp_leaf._graph:
            if u not in visited:
              vertices_visited=comp_leaf.bfs(visited,u)
              component_edges=comp_leaf.get_connections(vertices_visited)
              conn1=Graph(component_edges).complement()
              if(len(conn1)==0):## stable set will be 2
                  continue
              anticomp= Graph(conn1)
              anticomponents.append(anticomp)
        ## for all anticomponents it takes O(n^4)
        for anticomp in anticomponents:
            ring=isRing(anticomp)
            ## checking if anticomp is long ring o(n^2) or containsHole time (n+m^2)
            if ((not (ring[0] and ring[1]>=5)) and containsHole(anticomp)) :
                   return False
 return True


     


print(isGutGraph(g))