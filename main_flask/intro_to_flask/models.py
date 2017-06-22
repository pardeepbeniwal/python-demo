from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
import datetime
from sqlalchemy import desc
db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(255))
  addresses = db.relationship('Address', backref='user',lazy='dynamic')
  created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  
  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
    
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)
  
  def check_password(self, password):
	return check_password_hash(self.pwdhash, password)

class Address(db.Model):
	__tablename__ = 'address'
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.String(50))
	user_id = db.Column(db.Integer, db.ForeignKey('users.uid'))
	
