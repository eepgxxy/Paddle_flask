from flask import Flask
from flask import request
from flask import render_template
import os
app = Flask(__name__, static_folder="./")

@app.route('/')
def hello_segmentation():
    return render_template('home.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/save', methods=['GET', 'POST'])
def save():
    try:
        if request.method == 'POST' and request.files['img']:
            f = request.files['img']
            f.save('saved_files/img.png')
            os.system('python /home/aistudio/work/PaddleSeg/predict.py --image_path saved_files \
            --model_path ./model.pdparams \
            --save_dir saved_imgs \
            --crop_size 512 512 \
            --config pspnet.yml')
            return render_template('success.html')
        else:
            return render_template('failure.html')
    except:
        return render_template('failure.html')

@app.route('/result')
def result():
    return render_template('result.html')