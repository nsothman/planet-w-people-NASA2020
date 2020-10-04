from flask import Flask, render_template
import csv
app = Flask(__name__)

results = []
with open("./Datasets/risk.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

marking_safe = []
with open("./Datasets/marking_safe.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        marking_safe.append(row)

waste_acc = []
with open("./Datasets/waste_acc.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        waste_acc.append(row)

built_struc = []
with open("./Datasets/built_struc.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        built_struc.append(row)

med_serv = []
with open("./Datasets/med_serv.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        med_serv.append(row)


@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("map.html", results = results, marking_safe = marking_safe, waste_acc = waste_acc, built_struc = built_struc, med_serv = med_serv)

if __name__ == "__main__":
    app.run()
