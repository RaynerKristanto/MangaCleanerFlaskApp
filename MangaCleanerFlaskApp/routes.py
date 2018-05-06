from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, send_file, send_from_directory
from werkzeug.utils import secure_filename
from MangaCleanerFlaskApp import app

UPLOAD_FOLDER= 'uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'png'])

app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            # flash('Please upload a file')
            return redirect('/')
        # file = request.files['file']
        # if file.filename == '':
        #     flash('Please upload a valid file')
        #     return render_template('index.html')
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


@app.route('/download')
def download():
    try:
        #return send_from_directory(filename='contoured.jpg', as_attachment=True)
    	return send_file('contoured.jpg', attachment_filename='contoured.jpg', as_attachment=True)
    except Exception as e:
	    return str(e)
