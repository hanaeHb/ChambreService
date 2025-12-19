from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    print("Starting Flask app on port 8088...")
    app.run(debug=True, port=8088)
