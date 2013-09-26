# coding: utf-8
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from tweet import app, db, lm
from forms import LoginForm, ContactForm, TweetAddForm
from bson.objectid import ObjectId
from tweet.models import Post, User

@app.before_request
def before_request():
	g.user = current_user

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	
	form = LoginForm()

	if form.validate_on_submit():
		user = User.objects(username=form.username.data).first()
		crypt_pass = user.render_pw(form.password.data)

		if user.username and crypt_pass == user.password:
			remember_me = True if form.remember_me.data == 'y' else False
			login_user(user, remember=remember_me)

		return redirect(request.args.get('next') or '/')

	return render_template('login.html', 
		title = 'Sign In',
		form = form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@lm.user_loader
def load_user(id):
	return User.objects.get(_id=ObjectId(id))

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	return render_template('index.html', user=g.user)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			flash('Email enviado com sucesso!')
			return redirect('/')

	return render_template('contato.html', form=form)

@app.route('/tweets')
@login_required
def tweets():
	tweets = Post.objects.all()
	form = TweetAddForm()

	return render_template('tweets/list.html',
		title = 'Tweets',
		user = g.user,
		form = form,
		tweets = tweets)

@app.route('/tweet/add', methods = ['POST'])
@login_required
def tweet_add():
	form = TweetAddForm()

	if form.validate_on_submit():
		post = Post(body=form.message.data)
		post.save()
		post.author=User(id=current_user.id)
		post.save()
		return redirect(url_for('tweets'))

# @app.route('/tweet/detail/<slug>')
# @login_required
# def tweets_detail(slug):
# 	tweet = Post.objects(slug=slug).first()
	
# 	return render_template('tweets/detail.html',
# 		title = tweet.body,
# 		user = g.user,
# 		tweet = tweet)	