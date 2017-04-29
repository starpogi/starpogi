import os
from flask import Flask
from flask_compress import Compress

app = Flask(__name__)
Compress(app)


@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
