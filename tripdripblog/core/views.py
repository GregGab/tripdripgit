# core/views.py
from flask import render_template, request, Blueprint
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from tripdripblog import db
from tripdripblog.models import User, BlogPost
from tripdripblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm #, PasswordResetForm
from tripdripblog.users.picture_handler import add_profile_pic
from werkzeug.security import generate_password_hash

core = Blueprint('core', __name__)

@core.route('/', methods=['GET', 'POST'])
def index():

    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)

    # Login

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

    return render_template('index.html', blog_posts=blog_posts, form=form)

@core.route('/info')
def info():
    return render_template('info.html')
