import csv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import pickle

PATH_TO_DATA = "data/photos"
PATH_TO_ANNOT = "data/annotations"

if __name__ == "__main__":
    # Bare coordinates
    coord_dct = {}
    coord_word_dct = {}
    with open(os.path.join(PATH_TO_ANNOT, "coords.csv")) as f:
        reader = csv.reader(f)
        for row in reader:
            key, *coord = row
            key = key.split(".", 1)[0]
            coord = [eval(i) for i in coord]
            if key not in coord_dct.keys():
                coord_dct[key] = [coord]
            else:
                coord_dct[key].append(coord)

    # Coordinates with corresponding words
    with open(os.path.join(PATH_TO_ANNOT, "coordswords.csv"), encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 6:
                key, *coord, word = row
            else:
                key, *coord = row
                word = " "
            key = key.split(".", 1)[0]
            coord = [eval(i) for i in coord]
            if key not in coord_word_dct.keys():
                coord_word_dct[key] = [(coord, word)]
            else:
                coord_word_dct[key].append((coord, word))

    with open("coord_dct.pkl", "wb") as file:
        pickle.dump(coord_dct, file)

    with open("coord_word_dct.pkl", "wb") as file:
        pickle.dump(coord_word_dct, file)
