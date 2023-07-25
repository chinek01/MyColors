"""

Portfolio: MyColors
#100DaysOfCode with Python
Day: 91
Date: 2023-07-23
Author: MC

"""

import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from ImgColor import ImgColor

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './upload/'


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        if len(filename) > 1:
            fullpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(fullpath)

            color_class = ImgColor()
            color_class.open_img_file(fullpath)

            palette = color_class.color_percent_top_10_fit()

            # dodanie palet kolorów
            return render_template('index.html',
                                   hex_success=True,
                                   hex_palette=palette)

        return render_template('index.html')


# some test
if __name__ == '__main__':
    app.run(debug=True)
