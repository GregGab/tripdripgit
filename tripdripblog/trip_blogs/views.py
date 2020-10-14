# trip_blogs/views.py
from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from werkzeug.exceptions import abort

from tripdripblog import db
from tripdripblog.models import BlogPost
from tripdripblog.blog_posts.forms import BlogPostForm

from tripdripblog.models import TripBlog
from tripdripblog.trip_blogs.forms import TripBlogForm

trip_blogs = Blueprint('trip_blogs', __name__)

# CREATE A TRIP BLOG POST
@trip_blogs.route('/create-trip', methods=['GET', 'POST'])
@login_required
def create_trip():

    form = TripBlogForm()

    if form.validate_on_submit():

        trip_blog = TripBlog(title=form.title.data,
                              text=form.text.data,
                              city_country=form.city_country.data,
                              stayed_where=form.stayed_where.data,
                              went_where=form.went_where.data,
                              trip_image=form.trip_image.data,
                              user_id=current_user.id,)

        db.session.add(trip_blog)
        db.session.commit()
        flash('Trip Blog Created')
        return redirect(url_for('core.index'))

    return render_template('create_trip.html', form=form)


# BLOG POST (VIEW)
@trip_blogs.route('/<int:trip_blog_id>') # int makes sure the id is an integer
def trip_blog(trip_blog_id):

    trip_blog = TripBlog.query.get_or_404(blog_post_id)
    return render_template('trip_blog.html', title=trip_blog.title,
                           date=trip_blog.date, post=trip_blog)


# UPDATE
@trip_blogs.route('/<int:trip_blog_id>/update', methods=['GET', 'POST'])
@login_required
def update(trip_blog_id):

    trip_blog = TripBlog.query.get_or_404(blog_post_id)

    if trip_blog.author != current_user:
        abort(403) # forbidden error if authorized person tries to edit post

    form = TripBlogForm()

    if form.validate_on_submit():

        trip_blog.title = form.title.data
        trip_blog.text=form.text.data

        db.session.commit()
        flash('Trip Blog Updated')
        return redirect(url_for('trip_blogs.trip_blog', trip_blog_id=trip_blog.id))

    elif request.method == 'GET':
        form.title.data = trip_blog.title
        form.text.data = trip_blog.text

    return render_template('create_trip.html', title='Updating', form=form)


# DELETE
@trip_blogs.route('/<int:trip_blog_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_trip(trip_blog_id):

    trip_blog = TripBlog.query.get_or_404(trip_blog_id)

    if trip_blog.author != current_user:
        abort(403)  # forbidden error if authorized person tries to edit post

    db.session.delete(trip_blog)
    db.session.commit()
    flash('Trip Blog Deleted')
    return redirect(url_for('core.index'))
