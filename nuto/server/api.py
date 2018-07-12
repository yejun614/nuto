
import hashlib

def createHashKey(message):
	
	hashPW = hashlib.new('sha256')
	hashPW.update(str(message).encode())

	return hashPW.hexdigest()

class API:

	def __init__(self, Model):

		self.Model = Model
		
		self.all_users = {}
		self.level = {'query':1, 'train':2, 'node':3, 'model':3, 'state':4}

	def add_user(self, hashKey, level):
		
		self.all_users[hashKey] = level

	def query(self, variables):

		try:

			hashPW = hashlib.new('sha256')
			hashPW.update(str( variables['hashKey'] ).encode())

			resultHashPW = hashPW.hexdigest()

			print('HASH: %s' % (resultHashPW))

			if (str(resultHashPW) in self.all_users):

				user_level = self.all_users[resultHashPW]

				if (variables['method'] == 'query'):

					# check level
					if (user_level < self.level['query']):
						return 'Permission error'

					# query
					state = variables['state']
					data = variables['data']

					resultQuery = self.Model.states[state].query([data])
					return resultQuery[0]

				elif (variables['method'] == 'train'):

					# check level
					if (user_level < self.level['train']):
						return 'Permission error'

						state = variables['state']

						data = variables['data']
						target = variables['target']

						resultTrain = self.Model.states[state].train(data, target)
						return resultTrain[0]

				elif (variables['method'] == 'node'):

					# check level
					if (user_level < self.level['node']):
						return 'Permission error'

				elif (variables['method'] == 'model'):

					# check level
					if (user_level < self.level['model']):
						return 'Permission error'

				elif (variables['method'] == 'state'):

					# check level
					if (user_level < self.level['state']):
						return 'Permission error'

				else:
					return 'no method'

			else:
				return 'no permission'

		except KeyError:
			pass
