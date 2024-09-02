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

    return {'status': 'success'}

@app.route('/view-files', methods=['GET', 'POST'])
def view_files():
    password_attempt = request.form.get('password', '')

    if password_attempt == PASSWORD:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        filtered_files = [file for file in files if file not in ['init-default-profile-extentions', 'gitignore']]
        return render_template('view_files.html', files=filtered_files)
    elif password_attempt == '' and request.method == 'POST':
        return 'Password is required'
    else:
        return render_template('password_prompt.html')

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/preview/<filename>')
def preview(filename):
    return render_template('preview.html', filename=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
