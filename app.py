from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

employees_info = {
		"xyz": {
		"Tech": "Linux",
		"salary": "10L"
		},
		"abc": {
		"Tech": "Dev",
		"salary": "13L"
		}
	}
class Help(Resource):
	def get(self):
		help={
		"All Endpoints": ["/esinfo"]
		}
		return help
class Employees(Resource):
	def get(self):
		if request.args:
			if "ename" not in request.args.keys():
				message={
				"message": "use only ename as query parameter",
				"help": "/esinfo?ename=<your_emp_name>"
				}
				return message
			emp_name=request.args.get("ename")
			if emp_name in employees_info.keys():
				return employees_info.get(emp_name)
			message={
			"message": "sorry, we do not find given emp name in out list"

			}	
			return message
		return employees_info


api.add_resource(Help,"/")
api.add_resource(Employees,"/esinfo")
#api.add_resource(Employee,"/api/v1/einfo/<string:ename>")

app.run(debug=True,port=5000,host="localhost")