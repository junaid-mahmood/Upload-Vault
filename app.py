import os
import shutil
from flask import Flask, render_template, request, send_from_directory, url_for

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads' 

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

PASSWORD = 'admin'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if os.path.isdir(file.filename):
        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        shutil.copytree(file.filename, folder_path)
    else:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/preview/<filename>')
def preview(filename):
    return render_template('preview.html', filename=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
