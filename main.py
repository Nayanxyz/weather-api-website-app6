from flask import Flask , render_template                                       #web framework like streamlit or django

app = Flask("Website")

@app.route("/home")
def home():
    return render_template("webpage1.html")


@app.route("/about/")
def about():
    return render_template("about.html")

app.run(debug=True)