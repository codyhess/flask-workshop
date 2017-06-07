from flask import Flask, json, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    hello = request.args.get('hello', 'not here')
    return json.dumps({'hello': hello})

if __name__ == "__main__":
    app.run()
