# users/views.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from tripdripblog import db
from tripdripblog.models import User, BlogPost
from tripdripblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm #, PasswordResetForm
from tripdripblog.users.picture_handler import add_profile_pic
from werkzeug.security import generate_password_hash

users = Blueprint('users', __name__)

# register
@users.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


# Login
@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first() # first is called so you get it in right format

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Log in Success!')

            # if user was trying to get to a page that needed login
            next = request.args.get('next')

            # if user went straight to log in page
            if next ==None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html', form=form)





# Logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))


# account (update UserForm)
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():

    form = UpdateUserForm()

    if form.validate_on_submit():

        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.account'))

    # if user is not updating anything
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)


@users.route('/password_reset', methods=['GET', 'POST'])
@login_required
def password_reset():

    form = PasswordResetForm()

    if form.validate_on_submit():

        #if user.check_password(form.password.data) is not None:

        #form.password.data = current_user.password_hash
        #hashed_password = form.new_password.data)
        current_user.password_hash = form.password.data

        db.session.add
        db.session.commit()
        flash('User Password Updated!')
        return redirect(url_for('users.account'))

    # if user is not updating anything
    #elif request.method == "GET":

        #form.password.data = current_user.password_hash

    return render_template('password_reset.html', form=form)





# user's list of Blog posts
@users.route("/<username>") # < > means the username may change, depending on the user
def user_posts(username):

    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)


# user's list of Blog posts
@users.route("/trips/<username>") # < > means the username may change, depending on the user
def user_trips(username):

    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    trip_blogs = TripBlog.query.filter_by(author=user).order_by(TripBlog.date.desc()).paginate(page=page, per_page=5)
    return render_template('profile.html', trip_blogs=trip_blogs, user=user)
