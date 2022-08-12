from main import Graph
from ring import isRing
from mcs import MCS,cliqueCutsets


twin_connections=[('a', 'b'),
                   ('a', 'd'),('a','c'), ('b', 'd'),('b', 'e'),('c','d'),('c','g'),('e', 'f'),  ('e', 'h')
                   ,('f','h'),('f','g'),('g','h')] ## gt graph


twin_connections1=[('a', 'b'),
                   ('a', 'd'),('a','c'),('a','e'), ('b', 'c'),('b', 'f'),('c','d'),('c','e'),('d', 'e')
                   ,('d','g'),('e','g'),('f','h'),('h','g'),('i','f'),('i','h'),('i','g')] ## not gt graph

g = Graph(twin_connections)



## time complexity for obtaining twin sets is O(n+m)
def twinSets(g):
    s={}
    print()
    for i in g._graph:
        s[i]=0
    for i in range(len(g._graph)):
        v = list(g._graph.keys())[i]
        neighbors=g.v_neighbours(v) 
        for u in neighbors:
            s[u]=s[u]+2**(i)
    dict2 = {}
    for key, value in s.items():
       if value not in dict2:
         dict2[value] = []
       dict2[value].append(key)
    print(dict2)
    return { key:value for (key,value) in dict2.items() if len(value)== 2}



#twin_sets=twinSets(g)

#print("twin sets:::",twin_sets)
##forming partition graph takes O(n+m) time.
def partionGraph(twin_sets):
    temp=twin_sets.copy()
    edges=[]
    for key, value in twin_sets.items():
        print(value)
        del temp[key]
        neighbor_set=g.neighbours(value[0])
        print(neighbor_set)
        for key1, value in temp.items():
            if set(value).issubset(neighbor_set):
                edges.append((key,key1))
    return edges
    
        
   






## total time complexity for iterating over all leafs of the graph and checking for ring O(n^3)
def isGtGraph(g):
 order,fillin_graph, clique_gen=MCS(g)

 leafs,clique_sptr=cliqueCutsets(g,fillin_graph,clique_gen,order)
 print(len(leafs))
 for leaf_g in leafs:
    print(leaf_g._graph)
    twin_sets=twinSets(leaf_g)
    print("twin sets:::",twin_sets)
    if len(twin_sets)==1:  ## condition for 1 vertex graph    time complexity O(1)
       continue ## one vertex graph
    if len(twin_sets)>1:
       ## obtained partion graph from graph G with respective twin partitions done in twinSets function.
       ## time complexity to obtained partition graph O(n+m)
       edges=partionGraph(twin_sets) 
       if(len(edges)>0):
           p_graph = Graph(edges)
           ## condition for ring graph.   time complexity O(n^2) for 7-antihole  time complexity O(1)
           if (not isRing(p_graph)[0] and len(twin_sets)!=7):
               return False  
    else:
         return False
 return True


result=isGtGraph(g)
print(result)






