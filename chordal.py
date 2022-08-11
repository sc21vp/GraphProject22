from main import Graph
from copy import deepcopy


## uses MCS algorithm with time complexity of O(n+m)
def elimination_order(g):
    n=len(g._graph)
    order=[0]*n  
    w={}
    for key in g._graph:
      w[key]=0
    for i in range(n,0,-1):
        filt_Dict = { key:value for (key,value) in w.items() if key not in order}
        v=max(filt_Dict,key=filt_Dict.get)## picked unnumbered max weight vertex
        order[i-1]=v
        v_ng=g.neighbours(v)
        for u in v_ng:
            if u not in order:
                w[u]=w[u]+1
    return order



## uses MSC algorithm for peo  O(n+m).
def is_chordal(g:Graph):
      order=elimination_order(g)
      g1=deepcopy(g)
      for v in order:
          ng_list=g1.neighbours(v)
          if g1.is_clique(ng_list):
              g1.remove(v)
          else:
              return False
      return True
