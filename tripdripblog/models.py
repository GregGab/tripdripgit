# models.py
from tripdripblog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

# assists with authenticating users
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), unique=True, index=True) # unique makes sure can have multiples of same email
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    new_password_hash = db.Column(db.String(128))

    # backref is string/attribute call referring to the connection
    # of the Blog post and user
    posts = db.relationship('BlogPost', backref='author', lazy=True)

    blogs = db.relationship('TripBlog', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def reset_password(self, password):

        #self.password_hash = password_hash

        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f"Username {self.username}"


class BlogPost(db.Model):

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"


class TripBlog(db.Model):

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    city_country = db.Column(db.String(140), nullable=False)
    stayed_where = db.Column(db.String(140), nullable=False)
    went_where = db.Column(db.String(140), nullable=False)
    trip_image = db.Column(db.String(64), nullable=False, default='default_trip.png')



    def __init__(self, title, text, city_country, stayed_where, went_where, trip_image, user_id,):
        self.title = title
        self.text = text
        self.city_country = city_country
        self.stayed_where = stayed_where
        self.went_where = went_where
        self.trip_image = trip_image
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title} --- {self.city_country}"
