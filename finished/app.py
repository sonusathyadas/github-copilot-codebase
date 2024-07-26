import os
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response
from flask_cors import CORS
 
load_dotenv()

from apis import books_api

app = Flask(__name__)


@app.errorhandler(400)
def handle_400_error(error):
    return make_response(jsonify({'error':'Bad request'}),400)

@app.errorhandler(404)
def handle_404_error(error):
    return make_response(jsonify({'error':'Not found'}),404)

@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)

app.register_blueprint(books_api.get_blueprint(), url_prefix='/api/v1/books')


# Start flask application
if __name__ == '__main__':
    CORS=CORS(app)
    app.run(host='0.0.0.0', port=5000, debug= True)