import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome</h1>"

@app.route("/about", methods=["GET"])
def about():
    return "<h1>About</h1>"


app.run()