#!/usr/bin/python3
# nuto http server
# programming: yejun, jung (yejun614@naver.com)

import os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer

import queue

# global variables
server_queue = queue.Queue()
process_queue = queue.Queue()

MODEL = None

class RequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):

		global MODEL

		print(' Client Connection ', self.client_address)

		# body

		# analysis path
		path = self.path
		path = path.split('?')[-1]
		path = path.split('&')

		get_variables = {}
		for p in path:
			
			p = p.split('=')
			if (len(p) <= 1):
				continue

			get_variables[p[0]] = p[1]

		print('[%s:%d] client header: %s\n' % (self.client_address[0], self.client_address[1], get_variables))

		# send queue
		response = ''
		'''
		server_queue.put(get_variables)

		try:
			response = process_queue.get(timeout=3)

		except queue.Empty:
			response = 'error!'

		'''

		# analysis headers
		try:
			if (get_variables['method'] == 'query'):
				print('[%s:%d] method: ' % (self.client_address[0], self.client_address[1]), get_variables['method'])

				state_name = get_variables['state']
				data = get_variables['data']

				result = MODEL.states[state_name].query([data])
				response = result[0]

				print('[%s:%d] query result: %s' % (self.client_address[0], self.client_address[1], response))

		except KeyError:
			response = 'key error !'
			print('[%s:%d] query result: %s' % (self.client_address[0], self.client_address[1], response))


		# send response
		self.send_response(200)

		# send response header
		self.send_header('Content-type', 'text/plain; charset=utf-8')
		self.end_headers()

		# send response message to client
		self.wfile.write(str(response).encode())
		return

class Server:

	def __init__(self, addr=('localhost', 80), Model=None):
		global MODEL

		self.addr = addr

		MODEL = Model
		print(MODEL.states)

		self.Server = HTTPServer(self.addr, RequestHandler)

	def open(self):

		# start web server
		print('http://%s:%d Ready...\n' % (self.addr[0], self.addr[1]))
		self.Server.serve_forever()


if __name__ == '__main__':

	if (len(sys.argv) > 1):
		pass

	print('Nuto Server')
	
	server = Server()
	server.start()

