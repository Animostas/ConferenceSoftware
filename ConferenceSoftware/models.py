from ConferenceSoftware import db

class User(db.Model):

	__tablename__ = 'users_user'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)
	email = db.Columnn(db.String(120), unique=True)
	password = db.Column(db.String(50))
	
	def __init__(self, name=None, email=None, password=None):
		self.name = name
		self.email = email
		self.password = password

	def __repr__(self):
		return self.name
