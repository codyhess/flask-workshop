from flask import Flask, json, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/play')
def index():
    return json.dumps({
        'you': 'rock',
        'comp': 'rock',
        'win': 'WIN',
        })

@app.route('/v1')
def v1():
    return render_template('v1.html')

@app.route('/v2')
def v2():
    return render_template('v2.html')

@app.route('/v3')
def v3():
    return render_template('v3.html')

if __name__ == "__main__":
    app.run()
