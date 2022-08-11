
import pprint
from main import Graph
from copy import deepcopy
from mcs import MCS,cliqueCutsets

connections=[('a','b'),('a','c'),('a','e'),('a','d'),('c','b'),('c','a'),('c','e'),('e','d'),('b','e')]


connec=[('a','b'),('a','d'),('a','e'),('b','d'),('b','c'),('b','g'),('c','h'),('d','e'),('d','f'),
('d','g'),('e','f'),('f','g'),('h','g')]

connections2=[('a', 'c'),
                   ('a', 'd'),('a','f'), ('b', 'c'),('b', 'g'),('c','h'),('c','f'),('c', 'd'),  ('d', 'e')
                   ,('d','i'),('d','f'),('e','j'),('g','h'),('h','k'),('k','i'),('i','j')] ## gu exampl
g = Graph(connections2)

    

def guHelper(g:Graph):
 
      n=len(g._graph)
      print(n)
      degree=g.get_vertices_degree()
      if all(d >= n-2 for d in degree.values()):
        ## complement of graph 
        conn = g.complement() ## getting connections(vertices with edges) for complement of graph
        if len(conn)==0:
            return True## all are trivial anticomponents, so they are isomorphic to K1 graph.
        else :
          comp_leaf=Graph(conn) ## complement of graph object
          visited=[]
          ## from complement graph get  connected components using BFS.
          for u in comp_leaf._graph:
              if u not in visited:
                comp=comp_leaf.bfs(visited,u)  
                if len(comp) <=2:   # condition for ismorphic to K2 complement or K1 graph.
                    True            
      elif any(d <= n-3 for d in degree.values()):
          print(degree)
          keys = { key:value for (key,value) in degree.items() if value==n-1}.keys()
          print(keys)
          leaf_copy:Graph=deepcopy(g)
          if(len(keys)>0):
            for k in keys:
              leaf_copy.remove(k)
          comp_degree=leaf_copy.get_vertices_degree() ## O(n+m)
          print(comp_degree)
          ## checking a graph is a long hole   O(n+m) time
          if (len(leaf_copy._graph)>=5 and all(d ==2 for d in comp_degree.values()) and leaf_copy.graph_connected()):
             return True
      return False



def gu_recognize(g):
    order,fillin_graph, clique_gen=MCS(g)## get fill-in graph with perfect elimination ordering.
    leaves,clique_sptr=cliqueCutsets(g,fillin_graph,clique_gen,order) ## get leaves from the decompostion of the tree
    print(clique_sptr)
    for leaf in leaves:
      if(not guHelper(leaf)):
        return False
    return True

    



result=gu_recognize(g)


print(result)