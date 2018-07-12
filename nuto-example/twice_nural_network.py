
from nuto.ai import *

def main():
	
	node1 = node.Node()
	node2 = node.Node()

	node1.connect(node2)

	# model
	query_model = query.queryModel(node1, node2, node1.backProcess(node1))
	train_model = train.trainModel(node1, node2, node1.backProcess(node1))

	# train
	example = [1, 1.2, 0.8]
	target = [1, 1, 1]

	trainModel.train(example, target, query_model)
	print('Train END!')
	print('----------------')

	for node in node1.allNodes(node1):
		print('weight: ', node.weight)

if __name__ == '__main__':
	main()

