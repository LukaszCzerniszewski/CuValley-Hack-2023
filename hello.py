from flask import Flask
app = Flask(__name__)

from flask import send_from_directory

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('front', path)

@app.route('/')
def hello_world():
    return send_from_directory('front', 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
