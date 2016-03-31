from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, RadioField
from wtforms.validators import Required, EqualTo, Email

class RegistrationForm(Form):
	institution = TextField('Institution/Organization', [Required()])
	title = RadioField('Title', choices=[('Dr.', 'Dr.'),('Prof.','Prof.'),('Mr.','Mr.'),('Ms.','Ms.')], validators=[Required()])
	name = TextField('Full Name', [Required()])
	email = TextField ('Email Address', [Required(), Email()])
	password = PasswordField('Password', [Required()])
	confirm = PasswordField('Repeat Password', [Required(), EqualTo('password', message='Passwords must match')])
	# recaptcha = RecaptchaField()
