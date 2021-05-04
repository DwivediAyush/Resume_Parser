from flask import Flask, jsonify
import gem_parser
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
#get form
@app.route('/resume')
def resume():
    return jsonify(gem_parser.resume_data('test\\Abhay Pratap Singh CV.pdf'))
     



if __name__=="__main__":
    app.run(debug=True,port=8000)