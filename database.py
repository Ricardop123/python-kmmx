from sqlalchemy import create_engine, cplumn, integer, string
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://luis:@localhost:5432/kmmx')
base = declarative_base()

class User(base):
	__tablename__ = 'users'
	id = column(integer, primary_key=True)
	nickname = column(string)
	name = column(string)
	passwd = column(string)

	def __repr__(self):
		return '<user(nickname={nickname}, name={name}, passwd={passwd})>'.format(nickname=self.nickname,
																				  name=self.name,
																				  passwd=self.passwd)

	def	__str__(self):
		return '<user(nickname={nickname}'