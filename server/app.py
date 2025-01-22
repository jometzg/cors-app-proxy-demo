from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/corsdata', methods=['GET'])
def get_corsdata():
    response = make_response(jsonify({"message": "Hello, World!"}))
    response.headers['Access-Control-Allow-Origin'] = 'https://agreeable-mud-0bea1841e.4.azurestaticapps.net'
    return response

@app.route('/api/corsnoprotocoldata', methods=['GET'])
def get_corsnoprotocoldata():
    response = make_response(jsonify({"message": "Hello, World!"}))
    response.headers['Access-Control-Allow-Origin'] = 'agreeable-mud-0bea1841e.4.azurestaticapps.net'
    return response

@app.route('/api/corsstardata', methods=['GET'])
def get_corsstardata():
    response = make_response(jsonify({"message": "Hello, World!"}))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)
