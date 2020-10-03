import numpy as np
from PIL import Image, ImageOps

img = Image.open('../Datasets/42R_gmis_impervious_surface_percentage_utm_30m.tif')
img_inv = ImageOps.invert(img)
img_arr = np.array(img_inv)

np.savetxt("../Datasets/42R_gmis_impervious_surface_percentage_utm_30m.csv", img_arr, delimiter=",")
