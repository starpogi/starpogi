import os
from flask import Flask
from flask_compress import Compress

app = Flask(__name__)
Compress(app)


@app.route('/')
def index():
    return "Hello"


@app.route('.well-known/acme-challenge/vZrl32ZOApJXtEgbIxOJmj9DQ7b32EJWAucsA8-GdO4')
def cert_auth_challenege():
    return "vZrl32ZOApJXtEgbIxOJmj9DQ7b32EJWAucsA8-GdO4.aFBw64AccQoHNKnhqbHOMUdaKJxtW7Ny4oe9DELEn5w"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
