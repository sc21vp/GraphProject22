from chordal import is_chordal
from main import Graph
from copy import deepcopy



connec=[('a','b'),('a','e'),('b','c'),('c','d'),('d','e'),('a1','a'),('a1','e'),('a1','b'),('b1','b'),('b1','a'),
('b1','c'),('b1','c1'),('c1','c'),('c1','b'),('c1','d')]  ## gu graph

#g = Graph(connec)

def sortByVertexDegree(subset_list, sorted_degree):
    x_list=[]
    for d in sorted_degree:
        if d in subset_list:
           x_list.append(d)
    return x_list   
## time complexity O(n^2)
def isRing(g:Graph):
    not_ring=(False,0)
    if (not g.graph_connected()): 
        return not_ring  
    if (is_chordal(g)):
        return not_ring  
    X=[] ## will store partition of vertices 
    max_vertices=set()
    g1=deepcopy(g)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    degree=g.get_vertices_degree()
    v=max(degree,key=degree.get) ## get vertex with maximum  degree  
    subset_list=[]
    for u in g._graph:    
        if(g.v_neighbours(u).issubset(g.v_neighbours(v))):
            subset_list.append(u)
    sorted_degree=dict(sorted(degree.items(), key=lambda item: item[1]))
    x_list = sortByVertexDegree(subset_list, sorted_degree)
    for i in range(len(x_list)-1):
        if(not g.v_neighbours(x_list[i]).issubset(g.v_neighbours(x_list[i+1]))):
            return not_ring
    for x in x_list:
        g1.remove(x)
    if (not is_chordal(g1)):
         return not_ring
    max_vertices.add(x_list[-1])       
    rest_v=g.v_neighbours(x_list[-1]).difference(x_list)
    X.append(x_list)
    x_list=list(g1.v_neighbours(list(rest_v)[0]).intersection(rest_v)) ### obtaining x2 list.
    n=len(x_list)
    partition_list=X[0]
    while n!=0:
        x_list = sortByVertexDegree(x_list, sorted_degree)
        for i in range(len(x_list)-1):
            if(not g.v_neighbours(x_list[i]).issubset(g.v_neighbours(x_list[i+1]))):
                return not_ring 
        X.append(x_list)
        partition_list=partition_list+x_list
        max_vertices.add(x_list[-1])       
        x_list=g.v_neighbours(x_list[-1]).difference(set(partition_list))
        n=len(x_list)
    ### checking if parition sets is <=3 or partition sets are not subsets of graph G vertices.
    if (len(X)<=3 or not set(partition_list).issubset(set(g._graph.keys()))):
         return not_ring
    g2=deepcopy(g)
    temp_g2=deepcopy(g)
    for v in temp_g2._graph:
        if v not in max_vertices:
            print(v)
            g2.remove(v)
    g2_degree=g2.get_vertices_degree()
    print(g2._graph)    
    print(g2_degree)
    if (len(g2._graph)>=4 and all(d ==2 for d in g2_degree.values())  and g2.graph_connected()):
        return True, len(g2._graph)
    return not_ring

    
       
    
        







        






#print(isRing(g))