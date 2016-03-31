from ConferenceSoftware import app, db
from flask import request, session, g, redirect, url_for, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash

from ConferenceSoftware.main import index
from ConferenceSoftware.models import User
from ConferenceSoftware.registrationform import RegistrationForm

@app.route('/registration', methods=['GET','POST'])
def registration():
	form = RegistrationForm(request.form)
	if form.validate_on_submit():
		# create user in db
		user = User(name=form.name.data, email=form.email.data, password=generate_password_hash(form.password.data))
		# insert and commit to db
		db.session.add(user)
		db.session.commit()
		
		flash('Registered.')
		return redirect(url_for('index'))
	return render_template('registration.html', title='Register', form=form)
