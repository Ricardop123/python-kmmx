#user
 # username
  #passwd
  #role


class User:
	user = 'richi'
	__passwd = '12345'
	role = 'student'

	def __init__(self, user, passwd, role):
		self.user = user
		self.__passwd = passwd
		self.role = role 

	def set_user(self, user):
		self.user = user
		return True

	def get_user(self):
		return {
		'user': self.user,
		}

	def set_passwd(self, passwd):
		self.__passwd = passwd
		return True

	def get_info(self):
		return{
		'user': self.user,
		'role': self.role,
		}

	def login(self, user, passwd):
		if (user == self.user) and (passwd == self.__passwd):
			return True
		else:
			return False

if __name__ == '__main__':
	user = User(user='richi', passwd='12345', role='student')
	user.get_info()
	user.set_user(user='luis')
	print(user.get_user())
	user.set_passwd(passwd='12345')
	print(user.login(user='luis', passwd='12345')) #true

# @classmethod # todo calse objeto def user_type(cls)
#return[a,b,c]
# @staticmethod # solo objeto def user_type() sin necesidad de objeto creado
#  @property def getusername(self):
#                return self.