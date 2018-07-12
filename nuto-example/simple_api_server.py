
from nuto.ai import *
from nuto.server import *

def main():

	# example model
	node_list = [node.Node() for n in range(4)]
	test_model = model.Model(node_list)

	test_model.addState('Hi')

	# API
	serverAPI = api.API(test_model)
	print(serverAPI.Model.states)

	# add user
	pw = api.createHashKey('Hi')
	serverAPI.add_user(pw, 2)

	print('hashKey is %s' % (pw))

	# train
	print('\nStart train data\n')
	test_model.states['Hi'].train([2, 2.2, 2.1, 0.8, 0.9], [1, 1, 1, 1, 1])

	# server open
	print('-------------------------------------------------')
	server = api_server.Server(('localhost', 8000), serverAPI)
	server.open()

if __name__ == '__main__':
	main()
