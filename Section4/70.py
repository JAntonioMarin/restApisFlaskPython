from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name):
        return {'student': name}

api.add_resource(Student, '/student/<string:name>') #http://127.0.0.1:5000/student/Rolf

app.run(port=5000)

# 127.0.0.1 - - [17/Apr/2020 20:17:47] "GET /student/Rolf HTTP/1.1" 200 -
# 127.0.0.1 - - [17/Apr/2020 20:19:08] "GET /student/PacoPepe HTTP/1.1" 200 -
# 127.0.0.1 - - [17/Apr/2020 20:19:19] "POST /student/PacoPepe HTTP/1.1" 405 -
