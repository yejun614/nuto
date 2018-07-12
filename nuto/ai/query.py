
# queryModel

class queryModel:
	def __init__(self, input_node, output_node, process, Data=None):
		
		self.input_node = input_node
		self.output_node = output_node

		self.process = process	# backProcess

		self.Data = Data

	# processing width layer
	def query(self, Data, Node=None):

		# check node and data
		if (Node == None): Node = [self.input_node]
		#if (Data == None): Data = self.Data

		# check data length
		if (len(Node) != len(Data)):
			raise IndexError()

		Query = []
		for num in range(len(Data)):
			query = Node[num].activate_func( Node[num].weight, Data[num] )
			Query.append( query )

		if (self.output_node in Node):
			return Query[ Node.index(self.output_node) ]

		else:
			nextData = []
			nextNode = []

			for node in Node:
				for next_node in node.connected_nodes:

					if (next_node in nextNode):
						continue

					nextNode.append(next_node)

					data = 0
					for n in self.process[next_node]:
						index = Node.index(n)
						data += Query[index]

					nextData.append(data)

			return self.query(nextData, nextNode)

	'''
	def query(self, Data, Nodes=[], Layer=0, Query=[], limit=-1):
		
		# check node
		if (len(Nodes) == 0): Nodes.append(self.input_node)

		# output
		output = []

		for num in range(len(Nodes)):

			node = Nodes[num]

			if (node in self.process.keys()):
				
				sumData = 0

				for data in Data[num]:
					sumData += data

				output.append( node.activate_func( node.weight, sumData ) )

			else:
				output.append( node.activate_func( node.weight, Data[num][0] ) )

		# check output_node
		if (self.output_node in Nodes):
			return Query + output
		
		# check limit
		if ((limit != -1) and (Layer >= limit)):
			return Query + output

		# connected nodes
		connectedNodes = set([])

		for node in Nodes:
			connectedNodes.union( set(node.connected_nodes) )

		newData = []

		connectedNodes = list(connectedNodes)
		for node in connectedNodes:
			
			if (node in self.process.keys()):
				newData.append([])

				for n in self.process[node]:
					if (n.layer == layer):
						newData[-1].append(n)

			else:
				pass

		return query(newData, connectedNodes, Layer=Layer+1, Query, limit)
	'''

