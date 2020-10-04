import csv
import numpy as np
from PIL import Image, ImageOps

datasets = ["42R_gmis_impervious_surface_percentage_utm_30m",
            "42R_hbase_probability_of_hbase_class_utm_30m",
            "Rainfall Intensity 27-8-2020",
            "VNP46A2.A2015001.h24v06.001.2020219104211-HDFEOS-GRIDS-VNP_Grid_DNB-Data_Fields-DNB_BRDF-Corrected_NTL(EDITED)"]
csvFiles = []

for i in range(4):
    img = Image.open("../Datasets/"+ datasets[i] + ".tif")
    img_arr = np.array(img)
    np.savetxt("../Datasets/"+ datasets[i] + ".csv", img_arr, delimiter=",")

    csvFile = open("../Datasets/"+ datasets[i] + ".csv")
    csvFiles.append(csvFile)


csvArr = [np.loadtxt(csvFiles[0], delimiter=','),
          np.loadtxt(csvFiles[1], delimiter=','),
          np.loadtxt(csvFiles[2], delimiter=','),
          np.loadtxt(csvFiles[3], delimiter=',')]
risk = []
latDiff = -0.0002672348
longDiff = 0.00028969392

lat = 25.058029
for i in range(len(csvArr[0])):
    long = 66.892306
    for j in range(len(csvArr[0][i])):
        risk.append([lat, long, (csvArr[0][i][j] / 51000) + (csvArr[1][i][j] / 51000)])
        long += longDiff
    lat += latDiff

riskCount = 0
for i in range(len(csvArr[2])):
    for j in range(len(csvArr[2][i])):
        risk[riskCount][2] += (csvArr[2][i][j] / 25500)
        riskCount += 1

riskCount = 0
for i in range(len(csvArr[3])):
    for j in range(len(csvArr[3][i])):
        risk[riskCount][2] += (csvArr[3][i][j] / 14571)
        riskCount += 1

with open("../Datasets/risk.csv", "w") as risk_file:
    writer = csv.writer(risk_file)
    for row in risk:
        writer.writerow(row)
