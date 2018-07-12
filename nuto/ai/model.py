
import sys
sys.path.append('C:\\Users\\정예준\\Google 드라이브(nutofromync@gmail.com)\\next nuto')

import random

from nuto.ai.query import *
from nuto.ai.train import *

class State:

	def __init__(self, input_node, output_node):

		self.name = None

		self.input_node = input_node
		self.output_node = output_node

		self.connected_states = []

		# connect
		if (self.output_node not in self.input_node.connected_nodes):
			self.input_node.connect(self.output_node)

	# connect to other states
	def connect(self, state):

		if (state in self.connected_states):
			raise ValueError('Already connected')

		else:
			self.connected_states.append(state)

	def disconnect(self, state):
		self.connected_states.remove( self.connected_states.index(state) )

	def query(self, data):
		query_model = queryModel(self.input_node, self.output_node, self.backProcess())
		return query_model.query(data), query_model

	def train(self, data, target, train_rate=0.5):
		train_model = trainModel(self.input_node, self.output_node, self.backProcess())
		query_model = queryModel(self.input_node, self.output_node, self.backProcess())

		return train_model.train(data, target, query_model, train_rate)

	def search(self, node=None, search_list=[], limit=-1):

		# check limit
		#if ((limit != -1) and (len(search_list) > limit)):
		#	return search_list

		if (node == None): node = self.input_node

		if (len(node.connected_nodes) > 0):

			cnodes = []

			for n in node.connected_nodes:

				### BUG !!!!
				if (node == n): continue

				cnodes.append([node, n])
				cnodes += self.search(n)

			return search_list + cnodes

		else:
			return search_list + [[node, 0]]

	def allNodes(self, node=None):

		# check node
		if (node == None): node = self.input_node

		search = self.search(node)
		all_nodes = []

		for node in search:

			if (node[0] not in all_nodes):
				all_nodes.append(node[0])

			if (node[1] not in all_nodes):
				all_nodes.append(node[1])

		return all_nodes

	# Research Node Layer
	def layer(self, Node=None):
		
		# check node
		if (Node == None): Node = self.input_node

		Search = self.search(Node)

		Layer = []
		all_nodes = []

		for node in Search:
			all_nodes += node

		for node in all_nodes:
			pass

		return Layer

	# Research Query Perform Process

	def frontProcess(self, input_node=None):

		if (input_node == None): input_node = self.input_node

		Search = self.search(input_node)

		Process = {}
		for node in Search:

			if (node[0] in Process.keys()):
				Process[node[0]].append(node[1])

			else:
				Process[node[0]] = [node[1]]

		return Process

	def backProcess(self, input_node=None):

		if (input_node == None): input_node = self.input_node

		Search = self.search(input_node)

		Process = {}
		for node in Search:

			if (node[1] in Process.keys()):
				Process[node[1]].append(node[0])

			else:
				Process[node[1]] = [node[0]]

		return Process

	# Error value Back-Propagation
	def backPropagation(self, error, output_node=None, length=-1):
		
		if (output_node == None): output_node = self.output_node


class Model:

	def __init__(self, nodes):

		# set name
		self.name = None

		# create nodes
		self.nodes = nodes

		# state
		self.states = {}

	def __del__(sefl):
		pass

	# append state in model
	def addState(self, name, input_node=None, output_node=None):
		
		if (input_node == None): input_node = random.choice(self.nodes)
		if (output_node == None): output_node = random.choice(self.nodes)

		self.states[name] = State(input_node, output_node)
		self.states[name].name = name

