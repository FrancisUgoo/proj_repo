from flask import Flask

app = Flask(__name__)

@app.route("/")
def firstpage():
    return "<h1> This is the First Page </h1>"

@app.route("/<string:secon>")
def secondpage(secon):
    return f"<h1>This is the second page and you typed {secon}.</h1>"

@app.route("/<string:aa>/<string:bb>")
def thirdpage(aa,bb):
    return f"<h1> This is the third page and you typed {aa} and {bb}. </h1>"


if __name__ == "__main__":
    app.run(debug=True)

