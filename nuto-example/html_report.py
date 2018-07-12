
from nuto.ai import *
from nuto.data import *

FILE_NAME = 'report.html'

def main():
	
	html = report.html()

	# example model
	node_list = [node.Node() for n in range(4)]
	test_model = model.Model(node_list)

	test_model.addState('state')

	# add element in report
	html.add_elements([report.Model(test_model)])

	#export
	html.export(FILE_NAME)

	print('Create report file: ', FILE_NAME)

if __name__ == '__main__':
	main()
