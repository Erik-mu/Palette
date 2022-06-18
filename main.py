import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from colorthief import ColorThief


UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    flash('Image successfully uploaded and displayed below')
    colorthief =ColorThief(f"static/uploads/{file.filename}")
    palette = colorthief.get_palette(color_count=5)
    print(palette)
    return render_template('index.html', filename=filename, colors=palette)
    



@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == '__main__':
    app.run(debug=True)
