from intro_to_flask import app
from flask import render_template, request, flash,session,url_for, redirect,abort
from forms import  SignupForm,SigninForm,EditSignupForm
from flask_mail import Message, Mail
from models import db, User
import os

mail = Mail()

#http://explore-flask.readthedocs.io/en/latest/users.html-->confirm email

@app.route('/')
def index():
   return render_template('index.html')
   
@app.route('/signup',methods = ['POST', 'GET'])
def signup():
	form = SignupForm()  
	if request.method == 'POST':
		if form.validate() == False:
		  return render_template('signup.html', form=form)
		else:   
		  newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
		  db.session.add(newuser)
		  db.session.commit() 
		  session['email'] = newuser.email
		  return redirect(url_for('profile'))
      
	elif request.method == 'GET':
		return render_template('signup.html', form=form)  
			
   
@app.route('/list')
@app.route('/list/<int:page>', methods=['GET'])
def list(page=1):
  users = User.query.order_by(User.uid.desc()).paginate(page, 1, False)
  print(users.prev_num)
  return render_template('list.html',users=users)

@app.route('/profile')
def profile():

  if 'email' not in session:
    return redirect(url_for('signin'))

  user = User.query.filter_by(email = session['email']).first()
  
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('profile.html')
    
@app.route('/editprofile', methods = ['POST', 'GET'])
def editprofile():

  if 'email' not in session:
    return redirect(url_for('signin'))

  user = User.query.filter_by(email = session['email']).first()

  if user is None:
    return redirect(url_for('login'))
  elif request.method == 'GET':
	form = SignupForm(obj=user)
	return render_template('editprofile.html', form=form)
  elif request.method == 'POST':
		form = EditSignupForm()
		if form.validate() == False:
		  return render_template('editprofile.html', form=form)
		else:   
		  #newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
		  user.firstname = form.firstname.data
		  user.lastname = form.lastname.data
		  if form.password.data != '':
			user.password = form.password.data
		  db.session.commit() 
		  #session['email'] = newuser.email
		  return redirect(url_for('editprofile'))
		  
@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SigninForm()
  
  if 'email' in session:
    return redirect(url_for('profile'))
    
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      
      return redirect(url_for('profile'))
                
  elif request.method == 'GET':
    return render_template('signin.html', form=form)  
    
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('email', None)
   return redirect(url_for('index'))

@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      directory = 'upload'
      if not os.path.exists(directory):
		os.makedirs(directory)
      f.save(directory+'/'+f.filename)
      return 'file uploaded successfully'
         
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404   
    
if __name__ == '__main__':
   app.run(debug = True)
