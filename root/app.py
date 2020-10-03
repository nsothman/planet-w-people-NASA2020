from flask import Flask, render_template, request
import csv
app = Flask(__name__)

results = []
with open("../Datasets/risk.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("map.html", results = results)

if __name__ == "__main__":
    app.run(debug=True)
