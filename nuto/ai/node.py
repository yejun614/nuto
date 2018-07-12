
import random
import numpy as np

def ReLU(weight, data):
	print(weight)
	print(data)

	x = float(weight) * float(data)
	return np.maximum(0, x)

class Node:

	def __init__(self, activate_func=None, layer=0):

		self.name = None

		if (activate_func == None):
			self.activate_func = ReLU
		
		else:
			self.activate_func = activate_func
		
		self.weight = random.random()

		self.connected_nodes = []

	def connect(self, node):

		if (node in self.connected_nodes):
			raise ValueError('Already connected')

		else:
			self.connected_nodes.append(node)

	def disconnet(self, node):
		self.connected_nodes.remove( self.connected_nodes.index(node) )

	# query for single layer nural networks
	def query(self, Data, Query=[], Process=[], limit=-1):
		
		Process.append(self)
		Query.append( self.activate_func(self.weight, self.Data) )

		if ( not(limit == -1) and (limit >= len(Process)) and (len(self.connected_nodes) > 1) ):

			for node in self.connected_nodes:
				return node.query(Data, Query, Process, limit)

		else:
			return Process, Query


def search(node, search_list=[], limit=-1):

	# check limit
	#if ((limit != -1) and (len(search_list) > limit)):
	#	return search_list

	if (len(node.connected_nodes) > 0):

		cnodes = []

		for n in node.connected_nodes:

			### BUG !!!!
			if (node == n): continue

			cnodes.append([node, n])
			cnodes += search(n)

		return search_list + cnodes

	else:
		return search_list + [[node, 0]]

def allNodes(node):

	search = search(node)
	all_nodes = []

	for node in search:

		if (node[0] not in all_nodes):
			all_nodes.append(node[0])

		if (node[1] not in all_nodes):
			all_nodes.append(node[1])

	return all_nodes

# Research Node Layer
def layer(Node):

	Search = search(Node)

	Layer = []
	all_nodes = []

	for node in Search:
		all_nodes += node

	for node in all_nodes:
		pass

	return Layer

# Research Query Perform Process

def frontProcess(self, input_node):

	Search = search(input_node)

	Process = {}
	for node in Search:

		if (node[0] in Process.keys()):
			Process[node[0]].append(node[1])

		else:
			Process[node[0]] = [node[1]]

	return Process

def backProcess(self, input_node):

	Search = search(input_node)

	Process = {}
	for node in Search:

		if (node[1] in Process.keys()):
			Process[node[1]].append(node[0])

		else:
			Process[node[1]] = [node[0]]

	return Process
