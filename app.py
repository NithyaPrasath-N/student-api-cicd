from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Nithya", "department": "ECE"},
    {"id": 2, "name": "Rahul", "department": "CSE"},
    {"id": 3, "name": "Priya", "department": "IT"}
]

@app.route("/")
def home():
    return "testing to Student Management API 🚀"


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    new_student = {
        "id": len(students)+1,
        "name": data["name"],
        "department": data["department"]
    }

    students.append(new_student)

    return jsonify({
        "message":"Student Added Successfully",
        "student":new_student
    }),201


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )