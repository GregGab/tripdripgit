# trip_blogs/picture_handler.py

import os
from PIL import Image
from flask import url_for, current_app

def add_trip_pics(pic_upload, username):

    filename = pic_upload.filename
    # "mypicture . jpg"
    # this means you split mypicture.jpg
    # to only check the type which is jpg
    ext_type = filename.split('.')[-1]
    # whatever the user uploads it as, its saved as
    # "username.jpg , this can be saved as an hash also
    storage_filename = str(username)+'.'+ext_type

    filepath = os.path.join(current_app.root_path, 'static/trip_pics', storage_filename)

    output_size = (200, 200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
