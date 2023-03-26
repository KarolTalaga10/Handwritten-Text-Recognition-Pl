import cv2
import matplotlib.pyplot as plt
import numpy as np
import pickle
import random
NUM_PHOTO = 59
PATH_TO_PHOTO = f"data/photos/00{NUM_PHOTO}.jpg"

if __name__ == "__main__":
    img = cv2.imread(PATH_TO_PHOTO)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    with open('coord_word_dct.pkl', 'rb') as file:
        dct = pickle.load(file)
    
    lst_words = dct[f'00{NUM_PHOTO}']
    
    for i in lst_words:
        [x, y, w,h],word = i
        color = random.choices(range(256), k=3)
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
        cv2.putText(img, word, (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
    plt.imshow(img)
    plt.show()