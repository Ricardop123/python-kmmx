
def saludar():
	print('hola')
saludo = saludar()
print(saludo)

def suma(a, b, c = 0):
	return a + b + c

num1 = 5
num2 = 6	

print(suma(num1, num2, 4))

def foo(*args, **kwargs):
	print(args)
	print(kwargs)

foo('admin', name='richi', age=20)	

f = lambda x: print(x)
f.__call__('hola')

def myfunc(n):
	return lambda a : a = n

# user{}