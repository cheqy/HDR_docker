import os
from flask import Flask, render_template, redirect, url_for, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

import deep_run
import cassandra_run
import datetime

app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/static'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app) 

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return redirect(url_for('manage_file', filename=filename))
    return render_template('index.html')

@app.route('/result/<filename>')
def manage_file(filename):
    file_url = photos.url(filename)
    result = deep_run.deepnn(os.getcwd() + '/static/' + filename)
    cassandra_run.insertData(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), filename, result)
    return render_template('manage.html', filename=filename, file_url=file_url, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
