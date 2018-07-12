
from nuto.ai import *
from nuto.server import *

def main():

	# example model
	node_list = [node.Node() for n in range(4)]
	test_model = model.Model(node_list)

	test_model.addState('Hi')

	# train
	print('\nStart train data\n')
	test_model.states['Hi'].train([2, 2.2, 2.1, 0.8, 0.9], [1, 1, 1, 1, 1])

	# server open
	print('-------------------------------------------------')
	server = http_server.Server(('localhost', 8000), test_model)
	server.open()

if __name__ == '__main__':
	main()
