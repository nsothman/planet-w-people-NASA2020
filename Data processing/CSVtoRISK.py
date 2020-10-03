import csv
import numpy as np

csvFile = open("../Datasets/42R_gmis_impervious_surface_percentage_utm_30m.csv")

csvArr = np.loadtxt(csvFile, delimiter=',')
risk = []
lat = 25.058029
long = 66.892306
latDiff = -0.0002672348
longDiff = 0.00028969392

for i in range(len(csvArr)):
    long = 66.892306
    for j in range(len(csvArr[i])):
        point = [lat, long, csvArr[i][j] / 6375]
        risk.append(point)
        long += longDiff
    lat += latDiff

with open("../Datasets/risk.csv", "w") as risk_file:
    writer = csv.writer(risk_file)
    for row in risk:
        writer.writerow(row)
