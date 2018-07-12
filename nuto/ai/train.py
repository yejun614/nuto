
class trainModel:

	def __init__(self, input_node, output_node, process):
		
		self.input_node = input_node
		self.output_node = output_node

		self.process = process	# backProcess

	def backPropagation(self, Node, Error):
		
		if (Node not in self.process):
			return

		else:
			totalWeight = 0
			for node in self.process[Node]:
				totalWeight += node.weight

			for node in self.process[Node]:
				node.weight = Error * (node.weight / totalWeight)

				self.backPropagation(node, node.weight)

	def train(self, Data, Target, queryModel, trainRate=0.5):
		
		queryResults = []
		Error = []

		for num in range(len(Data)):
			data = Data[num]

			queryResults.append(queryModel.query([data]))

			error = queryResults[-1] - Target[num]
			Error.append( error )

			# Back-Propagation
			self.backPropagation(self.input_node, Error[-1] * trainRate)
