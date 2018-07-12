
from time import strftime, gmtime

def Model(model):

	body = '<div class="model">'

	body += '<p><b><big><l>(model)</l> %s <sub>%s</sub></big></b></p>' % (model.name, id(model))
	body += '<p>number of state: %d</p>' % (len(model.states))
	body += '<p>number of node: %d</p>' % (len(model.nodes))

	# check states
	if (len(model.states) > 0):

		body += '<li>'

		for state in model.states.keys():
			body += State(model.states[state])

		body += '</li><br />'

	# check nodes
	if (len(model.nodes) > 0):

		body += '<li>'

		for node in model.nodes:
			body += Node(node)

		body += '</li><br />'

	body += '</div>'

	# return html
	return body


def State(state):
	
	body = '<div class="state">'

	body += '<p><b><big><l>(state)</l> %s <sub>%s</sub></big></b></p>' % (state.name, id(state))

	body += '<p><u>input node</u></p>'
	body += '<p>%s <b><sub>%s</sub></b></p>' % (state.input_node.name, id(state.input_node))

	body += '<p><u>output node</u></p>'
	body += '<p>%s <b><sub>%s</sub></b></p>' % (state.output_node.name, id(state.output_node))

	body += '<p><u>Search</u></p>'
	body += '<p>%s</p>' % (state.search())

	body += '<p><u>Layer</u></p>'
	body += '<p>%s</p>' % (state.layer())

	body += '<p><u>Front Process</u></p>'
	body += '<p>%s</p>' % (state.frontProcess())

	body += '</div>'

	# return html
	return body

def Node(node):
	
	body = '<div class="node">'

	body += '<p><b><big><l>(node)</l> %s <sub>%s</sub></big></b></p>' % (node.name, id(node))
	body += '<p>Weight: %f</p>' % (node.weight)

	body += '</div>'

	#return html
	return body

def queryModel(model):
	
	body = ''

	# return htnk
	return body

def trainMode(model):
	pass

class html:

	def __init__(self):
		
		self.head = '<meta charset="utf-8">'
		self.body = ''

	def add_elements(self, elements):
		
		for element in elements:
			self.body += element

	def export(self, fn, author='unkown', style='style.css'):
		
		file = open(fn, 'w')
		file.write('<html><head>')
		file.write(self.head)
		file.write('<link rel="stylesheet" href="%s">' % (style))

		file.write('</head><body>')
		file.write('<p><b>nuto.data.report</b></p>')
		file.write('<p>%s (time: %s)</p>' % (fn, strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())))
		file.write('<p>author: %s</p><br />' % (author))

		file.write('<div id="report">')
		file.write(self.body)
		file.write('</div>')

		file.write('</body></html>')

		file.close()

