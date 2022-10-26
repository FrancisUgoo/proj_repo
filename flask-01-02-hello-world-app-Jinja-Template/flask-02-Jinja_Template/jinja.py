from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def head():
    return render_template("index.html", number1=0, number2=1)

@app.route("/<int:num1>")
def number1(num1):
    return render_template("index.html", number1=num1, number2="Not added") 


@app.route("/<int:num1>/<int:num2>")
def number(num1,num2):
    return render_template("body.html", value1=num1, value2=num2, sum=num1+num2)



if __name__== "__main__":
    app.run(debug=True)