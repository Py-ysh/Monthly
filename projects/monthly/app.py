from plot import *
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def i_index():
    pie = pie_plot()
    return render_template("index.html", plot=pie)

if __name__ == '__main__':
    app.run(debug=True)