# coding: utf-8
import datetime
import hashlib
from flask import url_for
from tweet import db

class Post(db.Document):
	body = db.StringField(required=True)
	author = db.ReferenceField('User')
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)

	def __unicode__(self):
		return self.body

	meta = {
		'allow_inheritance': True,
		'indexes': ['-created_at'],
		'ordering': ['-created_at']
	}

class User(db.Document):
	_id = db.StringField()
	username = db.StringField(verbose_name='Login', max_length=255, required=True)
	name = db.StringField(max_length=255, required=True)
	password = db.StringField(verbose_name='Password',max_length=40)
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)

	# def save(self, *args, **kwargs):
	# 	self.password = self.render_pw(self.password)
	# 	super(User, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

	def render_pw(self, _secret):
		return hashlib.sha1(_secret).hexdigest()

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)