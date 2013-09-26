from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, validators
from wtforms.validators import Required

class LoginForm(Form):
	username = TextField('username', validators = [Required()])
	password = PasswordField('password', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)

class ContactForm(Form):
	email = TextField('Email', [validators.Email()])
	mensagem = TextField('Mensagem', [validators.Length(min=6, max=35)])

class TweetAddForm(Form):
	message = TextField('Mensagem', [validators.Length(min=1, max=140)])