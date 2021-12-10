from flask import Flask
from werkzeug.wrappers import request
app = Flask(__name__)

@app.route('/')
def index():
    return 'hola Mundo!'

# GET, POST, PUT, PATCH, DELETE
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def test(post_id):
    if request.method == 'GET':
        return 'El id del post es:' + post_id
    else:
        return 'Este es otro método y no GET'

@app.route('/lele', methods=['POST'])
def lele():
    print(request.form)
    print(request.form['llave1'])
    print(request.form['llave2'])
    return 'lele'