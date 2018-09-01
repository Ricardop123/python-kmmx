
#from helpers.utils import login

from helpers. utils import (
	login1,
	login2,
	)

user1 = {
	'username': 'pepito',
	'role': 'admin',
	'password': 'therealpeito',
	'info':{
	'address': 'industria',
	'phone': '12345',
	'ssn': '123' 
	} 
}	

user2 = {
	'username': 'pepito2',
	'role': 'dba',
	'password': 'therealpeito2',
	'info':{
	'address': 'industria',
	'phone': '12345',
	'ssn': '123' 
	} 
}	

is_admin1 = login(user1)
print(is_admin1) #true

is_admin2 = login(user2)
print(is_admin2) #false

# Diccionario: user['clave']
