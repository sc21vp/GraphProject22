# Graph classes recognition algorithms

Graph object is stored in list of dict set
Graph representation example:
[
    {a:{b,c},
     b:{c,b,d},
     c:{a,b},
     d:{b}}
]
### Time complexity if graph G stored in dict set:
Here n and m are vertices and edges
For adding edge:O(1)
For finding vertex:O(1) because of set(worst case O(n))
For removing vertex: O(n+m)
 

# Main Algorithms in Code base(for given unidirected G)
`````
1) Checking G is Chordal .
2) Checking G contains long hole.
3) Checking G is Ring. 
4) Implementation of MCS Algorithm for decompostion of graph G into clique-cutsets.
5) Recongnition of Gu class. 
6) Recongnition of Gt class.
7) Recongnition of Gut class.
8) K2,3, C6 complement, W54  Algorithms 
`````

# Algorithm Run(execution) commnad:
 
run command: python file_name.py  (in terminal)

example: if we need to execute gut_recognition graph algorithm, give below command
        
        python gut_recognition.py 

        returns True or Flase

Use "pprint" function  for better representation of graph object in console.
###### Note: Before executing any algorithm, please provide respective Graph G connections as input in that particular executing file and save it. 
