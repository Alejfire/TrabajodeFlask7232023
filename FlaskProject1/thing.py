from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def home(home):
    return render_template("uh.html")


@app.route("/login", methods = ["POST", "GET"])
def  login():
    return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>Error???</h1>"


@app.route("/num2")
def num2():
    return render_template("num2.html")


@app.route("/num3")
def num3():
    return render_template("num3.html")


@app.route("/num5")
def num4():
    return render_template("num5.html")


if __name__ == "__main__":
    app.run(debug = True)