from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm, RequestForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Request
from flask import request
from werkzeug.urls import url_parse
from datetime import datetime

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

# Dashboard Page Route

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = RequestForm()
    requests = Request.query.order_by(Request.client_priority).all()
    sameClientRequestsA = Request.query.filter_by(client=form.client.data).order_by(Request.client_priority).all()
    sameClientRequestsD = Request.query.filter_by(client=form.client.data).order_by(Request.client_priority.desc()).all()

    if form.validate_on_submit():
        request = Request(title=form.title.data, description=form.description.data, client=form.client.data, 
            client_priority=form.client_priority.data, product_area=form.product_area.data, target_date=form.target_date.data, reporter=current_user)

        # Check through all priority numbers for the given client looking for a duplicate value
        duplicate = "no"
        for check in sameClientRequestsA:
            if check.client_priority == form.client_priority.data:
                duplicate = "yes"

        # If a duplicate was found, move through the exisitng list of requests and increase priority of all items by one to reorder list
        if duplicate == "yes":
            for item in sameClientRequestsD:
                if item.client_priority >= form.client_priority.data:
                    item.client_priority = item.client_priority +1
                    db.session.add(item)
                    db.session.commit()                

        db.session.add(request)
        db.session.commit()
        flash('Your request has been posted!')
        return redirect(url_for('index'))
    return render_template("index.html", title='Home Page', form=form, requests=requests)

# Login and Registraion Routes

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# Logout Route

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Single Request View Route

@app.route('/request/<id>')
@login_required
def view(id):
    request = Request.query.filter_by(id=id).first_or_404()
    return render_template('view.html', request=request)

# Delete Request Route

@app.route('/delete/<id>')
@login_required
def delete(id):
    request = Request.query.filter_by(id=id).first_or_404()
    db.session.delete(request)
    db.session.commit()
    return redirect(url_for('index'))

