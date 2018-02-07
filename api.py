from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome!'

@app.route('/api/info', methods = ['GET'])
def info():
    return jsonify({ 'name': 'flask api demo', 'version': '1.0.0' })

@app.route('/api/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(debug = True)
