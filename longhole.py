from main import Graph
from copy import deepcopy


#connections=[('a','b'),('a','c'),('b','d'),('c','e'),('c','f'),('d','e'),('e','f')]
#g = Graph(connections)
not_in_hole={}
in_path={}




def process(a,b,c,g_c):
    in_path[c]=1
    adj_c=g_c.neighbours(c)
    for d in list(adj_c):
       if ( not g_c.is_connected(d,a) and (not g_c.is_connected(d,b)) ):
           if in_path[d]==1:
               return True
           elif not_in_hole[(b,c),d]==0:
               return process(b,c,d,g_c)
    in_path[c] =0
    not_in_hole[(a,b),c] =1
    not_in_hole[(c,b),a]=1
    return False
 
## total time complexity in O(n+m^2) for a disconnected graph OR o(m^2)  for connected graph.
def containsHole(g:Graph):
    graph_comps=[]
    if(not g.graph_connected()):
      visited=[]
      for u in g._graph:
            if u not in visited:
              vertices_visited=g.bfs(visited,u)
              component_edges=g.get_connections(vertices_visited)
              g_comp= Graph(component_edges)
              graph_comps.append(g_comp)
    else:
        graph_comps.append(g)  
    for g_c in graph_comps:
        edges=g_c.get_connections(list(g_c._graph.keys()))
        ## initialzing not_in_hole and in_path variables.
        for v in g_c._graph:
            for edge in edges:
                not_in_hole[edge,v]=0
                not_in_hole[(edge[1],edge[0]),v]=0
            in_path[v]=0
        for u in g_c._graph:
            in_path[u]=1
            for edge in edges:
                if (g_c.is_connected(edge[0],u) and (not g_c.is_connected(u,edge[1])) 
                and not_in_hole[(u,edge[0]),edge[1]] ==0 ):
                    in_path[edge[0]]=1
                    if(process(u,edge[0],edge[1],g_c)):
                        return True
                    in_path[edge[0]]=0
            in_path[u]=1
    return False






#print(containsHole(g))