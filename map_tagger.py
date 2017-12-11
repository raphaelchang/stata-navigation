import numpy as np
import csv

with open('maps/map_tags.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    next(csvReader, None)
    array=[]
    for row in csvReader:
        array.append(row[1:])
    np.save("maps/map_tags.npy", array)
