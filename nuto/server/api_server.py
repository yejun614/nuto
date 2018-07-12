#!/usr/bin/python3
# programming: yejun, jung (yejun614@naver.com)

import os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer

import queue

# global variables
server_queue = queue.Queue()
process_queue = queue.Queue()

API = None

class RequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):

		global API

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

		# query
		response = API.query(get_variables)
		print('response: %s' % (response))

		# send response
		self.send_response(200)

		# send response header
		self.send_header('Content-type', 'text/plain; charset=utf-8')
		self.end_headers()

		# send response message to client
		self.wfile.write(str(response).encode())
		return

class Server:

	def __init__(self, addr=('localhost', 80), api=None):
		global API

		self.addr = addr

		API = api

		self.Server = HTTPServer(self.addr, RequestHandler)

	def open(self):

		# start web server
		print('http://%s:%d Ready...\n' % (self.addr[0], self.addr[1]))
		self.Server.serve_forever()

