# Max_Flow_Visualization
A step by step visualization of edmond-karp algorithm showing the flow in the network after each of edmond-karp's algorithm iterations until finally terminating 
upon reaching maximum flow.


**NOTE** the positions of the vertices may vary between runs since their locations are randomly selected upon each run


## Run Example:

using the code:
```
from visualize_EK_run import *
ns = Node('s')
n1 = Node('1')
n2 = Node('2')
n3 = Node('3')
n4 = Node('4')
nt = Node('t')
ns.add_neighbour(n1)
ns.add_neighbour(n2)
n1.add_neighbour(n3)
n1.add_neighbour(n4)
n2.add_neighbour(n4)
n3.add_neighbour(nt)
n3.add_neighbour(n4)
n4.add_neighbour(nt)
g = Graph(ns.nodes)
c = {(ns,n1):5,(ns,n2):7, (n1,n3):6, (n1,n4):8, (n2,n4):5,\
    (n3,nt):7, (n3,n4):4 ,(n4,nt):5}
f = {k:0 for k in c.keys()}
run_ford_fulkerson(g, c, f, ns, nt)
```
yields the following:
### iteration 0
![iteration 0](https://user-images.githubusercontent.com/42470657/127089855-de71a648-bffe-4668-a894-9aa234984df0.jpeg)
### iteration 1
![iteration 1](https://user-images.githubusercontent.com/42470657/127089854-f5cd45b1-44a1-4619-ad12-d1efe85bcd21.jpeg)
### iteration 2
![iteration 2](https://user-images.githubusercontent.com/42470657/127089851-0c392be8-3ae9-4e4e-8f8f-b46b063b4c18.jpeg)
