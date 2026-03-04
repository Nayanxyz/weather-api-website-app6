from flask import Flask , render_template                                       #web framework like streamlit or django

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")                                     #special pattern for url symbol <> to add/change values in url
def about(station, date):
    temperature = 23
    return {"station": station,                                          #gerated api data /23 is hard coded ,but we can change station and date from url
            "date": date,
            "temperature": temperature}

if __name__== "__main__":                                                  #so that we can run main.py here only.
    app.run(debug=True)