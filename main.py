from flask import Flask , render_template                                       #web framework like streamlit or django
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[['STAID','STANAME                                 ']]                    #only station id and station name

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())         # converted data of stations.txt file into html then
                                                                                          # transferred it to home html file


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    """ copied path of the file , then str(station) is string and used .zfill( Pad a numeric string with zeros on the left,
    to fill a field of the given width.) got 4 zeroes digit before station no.
) """
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"         #used jupyterlab to get data systematically
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']=="1860-01-05"]['   TG'].squeeze()/10
    return {"station": station,
            "temperature": temperature}

@app.route("/api/v1/<station>")
def one_station(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])                    #dates here and above are all in integer format
    result = df.to_dict(orient="records")                                    #to_dict method used for converting data into dictionary
    return result                                                            # and change data format to records



@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)                                         #changed dates to string
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient="records")     #<year> is just empty and replaced by value
    return result                                                                       #df['DATE'].str here .str is a bridge , it tells pandas
                                                                                        # "Look at every single item in this column and
                                                                                        # treat it as a string so I can use string methods on it."
                                                                                        #str.startswith method used to ensure the year date starts with year and as string


if __name__== "__main__":                                                  #we now have our working Rest api
    app.run(debug=True)