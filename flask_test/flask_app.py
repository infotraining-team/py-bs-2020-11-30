import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

persons = [
    {'id' : 0,
    'name' : "Leszek",
    'phone' : "12312312"},

    {'id' : 1,
    'name' : "Ola",
    'phone' : "54534534"},

    {'id' : 2,
    'name' : "Stefan",
    'phone' : "5231241234"}
]

@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome</h1>"

@app.route("/about", methods=["GET"])
def about():
    return "<h1>About</h1>"

@app.route("/api/v1/phonebook", methods=["GET"])
def phonebook():
    return jsonify(persons)

@app.route("/api/v1/phonebook/add", methods=["POST"])
def add_person():
    print(request.json)
    if request.json and "name" in request.json and "phone" in request.json:        
        person = {}
        person["name"] = request.json["name"]
        person["phone"] = request.json["phone"]
        person["id"] = 123
        persons.append(person)
    else:
        return jsonify({})

    return jsonify(person)

app.run()