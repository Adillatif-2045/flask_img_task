from flask import Flask, render_template
import os
import hashlib

app = Flask(__name__)
pic_folder = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER'] = pic_folder

@app.route('/')
def uploadpic():
    pic_path = os.path.join(app.config['UPLOAD_FOLDER'], 'pic.jpg')
    with open(pic_path, 'rb') as f:
        file_contents = f.read()
        file_md5 = hashlib.md5(file_contents).hexdigest()

    return render_template('index.html', image_upload=pic_path, file_md5=file_md5)


@app.route('/uploadpic')
def helloworld():
    return 'HELLO WORLD'


if __name__ == '__main__':
    app.run(debug=True)
