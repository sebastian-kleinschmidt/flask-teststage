from flask import Flask
app = Flask(__name__)

def index():
    return '<h1>Hello All!</h1>'
app.add_url_rule('/', 'index', index)


@app.route('/hellouser/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
