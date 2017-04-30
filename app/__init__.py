import os
from flask import Flask
from flask_compress import Compress

app = Flask(__name__)
Compress(app)


@app.route('/')
def index():
    return "Hello"


@app.route('/.well-known/acme-challenge/EqR_kjfp5D-y5e6n78qnQkOR_YfsMk0G5zJXJwi8JXE')
def cert_auth_challenege():
    return "EqR_kjfp5D-y5e6n78qnQkOR_YfsMk0G5zJXJwi8JXE.aFBw64AccQoHNKnhqbHOMUdaKJxtW7Ny4oe9DELEn5w"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
