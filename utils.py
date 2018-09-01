def login (user):
	if user['role'] == 'admin':
		return True 

	else:
		return False