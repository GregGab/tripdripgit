# error_pages/handlers.py
#THIS IS THE VIEW FILE FOR ERRORS
from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html') , 404 #returning a tuple

# this is errors for forbidden pages
@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/404.html') , 403 #returning a tuple