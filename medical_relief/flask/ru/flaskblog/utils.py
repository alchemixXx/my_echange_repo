import os

def save_picture(form_picture):
    f_name, f_ext = os.path.split(form_picture.filename)
    picture_fn = f_name + f_ext
    return picture_fn
