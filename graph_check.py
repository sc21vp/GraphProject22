from main import Graph
from copy import deepcopy
import itertools
k23=[('a','c'),('a','d'),('a','e'),('b','c'),('b','d'),('b','e')] ## k2,3 graph

c6bar=[('a','b'),('a','c'),('a','d'),('b','c'),('b','e'),('c','f'),('d','e'),('d','f'),('e','f')]## c6bar

w54=[('a','b'),('a','e'),('b','c'),('b','f'),('c','d'),('c','f'),('d','e'),('d','f'),('e','f')]


#g = Graph(w54)


## time complexitu O(n^5)
def isK23Graph(g:Graph):
    if(len(g._graph)!=5):
        return False
    vertices=list(itertools.permutations(list(g._graph.keys())))
    for v in vertices:
        if not g.is_connected(v[0],v[1]) :
            if not g.is_connected(v[2],v[3]) and not g.is_connected(v[2],v[4]) and not g.is_connected(v[3],v[4]):
                if g.is_connected(v[0],v[2]) and g.is_connected(v[0],v[3]) and g.is_connected(v[0],v[4]):
                    if g.is_connected(v[1],v[2]) and g.is_connected(v[1],v[3]) and g.is_connected(v[1],v[4]):
                                print(v)
                                return True
       
    return False

#print(isK23Graph(g))

## time complexitu O(n^6)
def isC6ComplementGraph(g:Graph):
    if(len(g._graph)!=6):
        return False
    vertices=list(itertools.permutations(list(g._graph.keys())))  
    for v in vertices:
        if g.is_connected(v[0],v[1]) and g.is_connected(v[0],v[2]) and g.is_connected(v[1],v[2]):
            if g.is_connected(v[3],v[4]) and g.is_connected(v[3],v[5]) and g.is_connected(v[4],v[5]):
                if g.is_connected(v[0],v[3]) and not g.is_connected(v[0],v[4]) and not g.is_connected(v[0],v[5]):
                      if g.is_connected(v[1],v[4]) and not g.is_connected(v[1],v[3]) and not g.is_connected(v[1],v[5]):
                          if g.is_connected(v[2],v[5]) and not g.is_connected(v[2],v[3]) and not g.is_connected(v[2],v[4]):
                              return True

    return False          


#print(isC6ComplementGraph(g))

## time complexitu O(n^6)
def isW54Graph(g:Graph):
    if(len(g._graph)!=6):
        return False
    vertices=list(itertools.permutations(list(g._graph.keys()))) 
    for v in vertices:
        if (g.is_connected(v[5],v[2]) and g.is_connected(v[5],v[3])
         and g.is_connected(v[5],v[4]) and g.is_connected(v[5],v[1]) and not g.is_connected(v[5],v[0])):
            if (g.is_connected(v[0],v[1]) and g.is_connected(v[0],v[4]) and  
                 not g.is_connected(v[0],v[2]) and not g.is_connected(v[0],v[3])):
                   if (g.is_connected(v[2],v[1]) and g.is_connected(v[2],v[3]) and  
                       not g.is_connected(v[2],v[4])) :
                        if (g.is_connected(v[4],v[3]) and not g.is_connected(v[4],v[1])):
                            return True
    return False

#print(isW54Graph(g))