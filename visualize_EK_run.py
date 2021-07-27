import matplotlib.pyplot as plt
import networkx as nx
NOT_VISITED = 0
VISITED = 1
class Node:
	nodes = []
	def __init__(self, id = None):
		self.neighbours = []
		self.id = id
		self.nodes.append(self)
	def get_neighbours(self):
		return self.neighbours
	def add_neighbour(self, node):
		self.neighbours.append(node)
	def remove_neighbour(self, node):
		if node in self.neighbours:
			self.neighbours.remove(node)
	def get_id(self):
		return self.id
class Graph:
	def __init__(self, nodes = []):
		self.nodes = nodes
	def getnodes(self):
		return self.nodes


def path_exists(g, source, dest):
	'''returns path if exists between source and dest in graph g, else None'''
	q = []
	q.append((source,[source]))
	visited_dict = {}
	for i in range(len(g.getnodes())):
		visited_dict[g.getnodes()[i]] = NOT_VISITED
	visited_dict[source] = VISITED
	while(len(q) != 0):
		v, path = q.pop()
		if v == dest:
			return path 
		for w in v.neighbours:
			if visited_dict[w] == NOT_VISITED:
				visited_dict[w] = VISITED
				q.append((w, path + [w]))
def convert_path_to_edges(path):
	'''converts vertices in path to edges'''
	return [(path[i],path[i+1]) for i in range(len(path)-1)] if path is not None else None

def find_min_cap(path, c):
	'''finds the minimal flow that can go under c's constraints'''
	return min([c[x] for x in path])

def create_graph_edges(g):
	'''auxiliary function mainly for constructing the visual graph'''
	E = []
	for i in g.getnodes():
		for j in i.get_neighbours():
			E.append([i.get_id(),j.get_id()])
	return E

def ford_fulkerson_iteration(g, c, f, s, t):
	'''a single iteration of ff, including update of edges
	assuming edges are ok before start of iteration'''
	path = convert_path_to_edges(path_exists(g, s, t))
	if path is not None:
		min_cap = find_min_cap(path, c)
		for i in path:
			f[i] = f[i] + min_cap
			c[i] = c[i] - min_cap
			if c[i] == 0:
				i[0].remove_neighbour(i[1])
		return -1
	return 0
	

def run_ford_fulkerson(g, c, f, s, t):
	'''full run of the ford and fulkerson method (edmond-karp algorithm)
	since the path found by bfs is the shortest'''
	status = -1
	pos = None
	e = create_graph_edges(g)
	while(status != 0):
		pos = draw_graph(e, c, f, pos) #draw the graph with updated flow
		status = ford_fulkerson_iteration(g, c, f, s, t)
	return f


def draw_graph(e, c, f, pos):
	G = nx.Graph()
	edges = e
	G.add_edges_from(edges)
	if pos is None:
		pos = nx.spring_layout(G)
	plt.figure()
	cmap = []
	for node in G:
		if node in ['s','t']:
			cmap.append('gold')
		else:
			cmap.append('pink')

	nx.draw(G,pos,edge_color='black',width=1,linewidths=1,\
	node_size=300,node_color=cmap,alpha=0.9,\
	labels={node:node for node in G.nodes()})

	edge_l1 = {(i[0].get_id(),i[1].get_id()):\
	str(f[i])+'\\'+str(c[i]+f[i]) for i in c.keys() if f[i] > 0}
	
	edge_l2 = {(i[0].get_id(),i[1].get_id()):\
	str(f[i])+'\\'+str(c[i]+f[i]) for i in c.keys() if f[i] == 0}
	
	nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_l1,font_color='red')
	nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_l2,font_color='black')
	plt.axis('off')
	plt.show()
	return pos

	