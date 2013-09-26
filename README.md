tweet
=====

Simple tweet example using by Flask

install
=======

	sudo easy_install flask flask-security flask_mongoengine flask-script
	
configure
=========

To use the system we need to create a new user, so run:

	python manage.py shell
	from tweet.models import *
	user = User(name='My name',username='me@mymail.com')
	user.password = user.render_pw('password')
	user.save()

Type CTRL + D to get out from shell.

run
===

First, have sure that your mongodb server is running and take a look on config.py to validate the values.

	python manage.py runserver
