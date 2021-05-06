import gem_parser
import argparse
import os
import time
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
 
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')
 
@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        print(file.filename)
        file.save(secure_filename(file.filename))
        filename = os.getcwd()
        filename = filename + '/' + file.filename
        print (filename)
        time.sleep(5)
        return jsonify(gem_parser.resume_data(filename))
 

if __name__ == '__main__':
    app.run(host='localhost', port=5000)