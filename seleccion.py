role = 'admin'

if role == 'admin':
	print('welcome')

elif role == 'user':
	print ('welcome')
else:
 print('denied')

users = ['luis','pepito']
passwd = ['luis123', 'therealpeito']

compress = zip (users, passwd)

# ('luis', 'luis123')
# ('pepito', 'therealpepito')
for role in compress:
	print (role)
	if role[0] == 'luis':
		print('welcome') 
		