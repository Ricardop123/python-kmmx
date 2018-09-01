class DBConnection:
	host = 'localhost'
	port = 54321
	user = 'pepito'
	#name mangling
	__passwd = 'therealpepito'

	def __init__(self, host, port, user, passwd):
		self.host = host
		self.port = port
		self.user = user
		self.__passwd = passwd

		print('conectado')
		

	def get_info(self):
		return {
		    'host': self.host,
		    'port': self.port,
		    'user': self.user,
		}
		

	def __del__(self):
		print('desconectado')
		
classpostgreSQL(DBConnectionSQL):
	name = 'postgreSQL'

	def get_info(self):
		d = super().get_info()
		d['engine'] = 'postgreSQL'
		return d 

	def __str__(self):
		return self.name

	def __repr__(self):
		return 'soy postgreSQL'	

conn = postgreSQL(host='localhost', port=54321, user='luis', passwd='1234')
print(conn.get_info())
del conn

#conn.connect()
#conn.disconnect()

#print ([attr for attr in dir(conn)])
