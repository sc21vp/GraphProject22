
from collections import defaultdict
import queue


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections):
        self._graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        self._graph[node2].add(node1)
    

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def neighbours(self,node):
        return self._graph[node]
    
    ## method for closure neighbours includes own node.
    def v_neighbours(self,node):
        s=self._graph[node].copy()
        s.update({node})
        return s

        
    def get_connections(self,nodes):
        conn=[]
        temp=nodes.copy()
        for node in nodes:
            temp.remove(node)
            for t in temp:
                if self.is_connected(node,t):
                    conn.append((node,t))
        return conn
    


    def is_clique(self,separator):
     
     temp=separator.copy()
     for i in separator:
       ng=self.neighbours(i)
       temp.remove(i)
       if not set(temp).issubset(ng):
           return False
       if len(temp)==1:
           break
     return True

    def get_vertices_degree(self):
     degree={}
     for key in self._graph:
        degree[key]=len(self.neighbours(key))
     return degree


    def bfs(self,visited,node): #function for BFS
      queue=[]
      path=[]
      visited.append(node)
      queue.append(node)
       
      while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        path.append(m) 
         

        for neighbour in self._graph[m]:
          if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
      return path



    def graph_connected(self):
        visited=[]
        v=next(iter(self._graph))
        path=self.bfs(visited,v)
        if len(path)==len(self._graph):
            return True
        return False


    def complement(self):
        track=[]
        conn=[]
        for v in self._graph:
            #print(leaf._graph.keys())
            track.append(v)
            u_list= list(self._graph.keys() - self.neighbours(v)-set(track))
            for u in  u_list:
                conn.append((v,u))
        return conn
        

