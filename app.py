
#app.py
from flask import Flask, request, render_template
import urllib
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.dates import date2num

from io import BytesIO

import pandas as pd
from datetime import datetime, timedelta


import matplotlib.dates as mdates
    
from scipy import signal

def get_data():
    import re
    import datetime
    date = []
    data = []
    for year in range(1929,2011):
        with open("sun_data/rz{}.txt".format(year),"r") as row_txt:
            txts = re.split("----*\s*",row_txt.read())
        yearly_data = []
        for month in range(12):
            txt_month = txts[month]
            index = re.search(r"  1 ",txt_month).span()[0]
            txt_month = txt_month[index:]
            rows = txt_month.split("\n")
            ls = []
            for i,row in enumerate(rows):
                if i<31 and re.fullmatch( '\s*',row)==None and re.match("\s*Monthly",row)==None:
                    R = row.split(" ")[-1]
                    if month+1 in [1,3,5,7,8,10,12] and i+1>31:
                        print(year,month+1,i+1,R)
                    elif month+1 in[4,6,9,11] and i+1>30:
                        print(year,month+1,i+1,R)
                    elif month+1 == 2 and i+1>28:
                        if year%4!=0:
                            print(year,month+1,i+1,R)
                        elif  i+1>29:
                            print(year,month+1,i+1,R)
                           
                    if R in ["-",""]:
                        pass
                    else:
                        R = float(R)
                        date += [datetime.datetime(year,month+1,i+1)]
                        ls+=[R]      
            yearly_data += ls
        data += yearly_data
    return (date,data)

app = Flask(__name__)

fig, ax = plt.subplots(1,1)

date,data = get_data()
#dateのフォーマットを修正
xfmt = mdates.DateFormatter("%y-%m") 
ax.xaxis.set_major_formatter(xfmt)
    

ax.plot(date,data)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plot/btc")
def plot_btc():

    # Obtain query parameters
    start = datetime.strptime(request.args.get("start", default="1929-01-01", type=str), "%Y-%m-%d")
    end = datetime.strptime(request.args.get("end", default="2010-12-31", type=str), "%Y-%m-%d")

    if start > end:
        start, end = end, start
    if (start + timedelta(days=7)) > end:
        end = start + timedelta(days=7)

    png_out = BytesIO()

    ax.set_xlim([start, end])
    ax.set_ylabel("sun")

    plt.xticks(rotation=30)#ラベルを斜めにしてるだけ

    plt.savefig(png_out, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_out.getvalue())

    return "data:image/png:base64," + img_data

if __name__ == "__main__":
    app.run(debug=True, port=5000)

    
