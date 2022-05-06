from flask import Flask
app = Flask(__name__)


@app.route("/")
def intro():
    return "<h1>App To Deploy"


if __name__ == "__main__":

    app.run(debug=True)
