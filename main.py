from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/code-portfolio")
def code():
    return render_template("python.html")


@app.route("/photo-portfolio")
def photo():
    return render_template("photo.html")


@app.route("/video-portfolio")
def video():
    return render_template("video.html")


if __name__ == "__main__":
    app.run(debug=True)
