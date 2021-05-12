import gem_parser
import argparse
import os
# def get_argument():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-f", "--file",required=True,help = "Filename",type=str) 
#     args = parser.parse_args()
#     return args.file

# def main():
#     files = get_argument()
#     print(gem_parser.resume_data(files))
#     os.remove(files)


# if __name__ == "__main__":
#     main()

from flask import Flask,render_template,request,jsonify
from werkzeug.utils import secure_filename
import time
 
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(),'resume')
print (app.config['UPLOAD_FOLDER'])

@app.route('/')
def form():
    return render_template('form.html')
 
@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        print (os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        time.sleep(3)
        return jsonify(gem_parser.resume_data(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename))))
 

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
