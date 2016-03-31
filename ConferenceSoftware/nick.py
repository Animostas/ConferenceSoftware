from ConferenceSoftware import app, db
from flask import request, session, g, redirect, url_for, abort, render_template
from flask_sqlalchemy import SQLAlchemy

@app.route('/registration')
def registration():
	return render_template('registration.html')
