import pprint
from main import Graph
from copy import deepcopy
from collections import deque
connections1 = [('a', 'b'),
                   ('a', 'c'),('b','c'), ('c', 'd'),('c', 'g'),('d','e'),('e','f'),('d', 'f'),  ('d', 'h'),('g','h'),
                   ('g','i'),('h','i')]

connections=[('a','b'),('a','c'),('a','e'),('a','d'),('c','b'),('c','a'),('c','e'),('e','d'),('b','e')]


connections2=[('a', 'c'),
                   ('a', 'd'),('a','f'), ('b', 'c'),('b', 'g'),('c','h'),('c','f'),('c', 'd'),  ('d', 'e')
                   ,('d','i'),('d','f'),('e','j'),('g','h'),('h','k'),('k','i'),('i','j')]

connec=[('a','b'),('a','d'),('a','e'),('b','d'),('b','c'),('b','g'),('c','h'),('d','e'),('d','f'),
('d','g'),('e','f'),('f','g'),('h','g')]  ## gu graph

#g = Graph(connections2)
#pretty_print = pprint.PrettyPrinter()
#pretty_print.pprint(g._graph)       

 
## Begin MCS M algorithm   time complexity is O(nm)

def MCS(g:Graph):
    g1=deepcopy(g)
    n=len(g._graph)
    order=[0]*n  
    w={}
    s=-1
    clique_generators=[]
    fill_edges=[]
    for key in g1._graph:
        w[key]=0
    for i in range(n,0,-1):
        #filtered = filter(lambda value: value != 0, order)
        filt_Dict = { key:value for (key,value) in w.items() if key not in order}
        v=max(filt_Dict,key=filt_Dict.get)## picked unnumbered max weight vertex
        if w[v]<=s:
          clique_generators.append(v)
        s=w[v]
        reached={}
        for key in g1._graph:
            if key==v:
                reached[key]=True
            else:
                reached[key]=False
        reach=[None]*n
        adj=[]
        adj=list(g1.neighbours(v))
        for key in adj:
            reached[key]=True
            if(reach[w[key]]==None):
                reach[w[key]]=deque([])  
            reach[w[key]].append(key)
        for j in range(n):
            while reach[j] !=None and len(reach[j])>0:
                u=reach[j][0]
                reach[j].popleft()
                for z in g1.neighbours(u):
                    if not reached[z]:
                        reached[z]=True
                        if w[z]>j:
                            adj.append(z)
                            if(reach[w[z]]==None):
                               reach[w[z]]=deque([])  
                            reach[w[z]].append(z)
                        else :
                            reach[j].append(z)
        for u in adj:
            w[u]=w[u]+1
            fill_edges.append((v,u))
        order[i-1]=v
        g1.remove(v)
    new_graph=Graph(fill_edges)
    return order,new_graph,clique_generators

        








#order,fillin_graph, clique_gen=MCS(g)
#print(order)
#print(clique_gen)


#function for getting clique minimal separators and executing decompostion step where we get clique-cutsets.
def cliqueCutsets(g:Graph,fillin_graph,clique_gen,order):
     g1=deepcopy(g)
     h1=deepcopy(fillin_graph)
     clique_sptr=[]
     leafs=[]
     for x in order:
         if x in clique_gen:
             separator= list(h1.neighbours(x))
             if g.is_clique(separator):
                 clique_sptr.append(separator)
                 g1_copy=deepcopy(g1)
                 for v in separator:
                     g1_copy.remove(v)
                 c= list(set(g1_copy.neighbours(x)))# 
                 g1_copy.remove(x)
                 for u in c:
                    nlist=g1_copy.neighbours(u)
                    c=c+list(nlist)
                    g1_copy.remove(u)
                 c=c+[x]   ### connected component containg x
                 del g1_copy
                 conn=g1.get_connections(c +separator)# getting edges for the leafs
                 leaf_graph=Graph(conn)  ## form leaf graph which does not admit clique-cutset.
                 leafs.append(leaf_graph)
                 for v in c:
                     g1.remove(v)
         h1.remove(x)
     leafs.append(g1)
     return leafs,clique_sptr
    
    
                     

                 


             
                     
             
         














#leafs,clique_sptr=cliqueCutsets(g,fillin_graph,clique_gen,order)
#print("clique separators:::::",clique_sptr)
#print("leaves of the graph")
#print("-------------------------")
