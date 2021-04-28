from flask import Flask, render_template
import os

app = Flask("app")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greetings")
def greetings():
    return render_template("greeting.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
