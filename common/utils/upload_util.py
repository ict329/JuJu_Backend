# -*- coding: utf-8 -*-
# -*- 2013-07-19 -*-
from werkzeug import secure_filename
import os
from bson.objectid import ObjectId

ALLOWED_UPLOAD_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])

def file_suffix(filename):
    return filename.rsplit('.', 1)[-1].lower()

def allowed_file(filename, file_extensions):
    return '.' in filename and \
        file_suffix(filename) in file_extensions


def upload_file(file, folder):
    if file and allowed_file(file.filename, ALLOWED_UPLOAD_EXTENSIONS):
        suffix = file_suffix(file.filename)
        filename = str(ObjectId()) + "." + suffix
        dir_path = os.path.abspath(folder+"/"+filename) 
        file.save(dir_path)
        return dir_path
    return "File is None or not allowed: file name = " + file.filename
    
