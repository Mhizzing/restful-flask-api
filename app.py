# Learning from https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Using only Flask to make an API
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})


@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
    return jsonify({'data': num**2})


# Using flask_restful to implement an API
class Bye(Resource):
    # Corresponds to GET request
    def get(self):
        return jsonify({'message': 'bye world'})
    
    # Corresponds to POST request
    def post(self):
        data = request.get_json()
        return jsonify({'data': data}), 201


class Cube(Resource):
    def get(self, num):
        return jsonify({'square': num**3})


# Define resource URLs
api.add_resource(Bye, '/bye')
api.add_resource(Cube, '/cube/<int:num>')


# driver function
if __name__ == '__main__':
    app.run(debug = True)