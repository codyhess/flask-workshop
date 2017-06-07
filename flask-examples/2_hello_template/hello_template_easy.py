from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=''):
    return '<h1>Hello ' + name + '!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
