import numpy as np
import cv2
from matplotlib import pyplot as plt

NUM_TRAIN = 26
DICTIONARY_SIZE = 1000
sift = cv2.xfeatures2d.SIFT_create()
BOW = cv2.BOWKMeansTrainer(DICTIONARY_SIZE)

for i in range(1, NUM_TRAIN + 1):
    train = cv2.imread('train/' + str(i) + '.jpg')
    train = cv2.resize(train, (0, 0), None, 0.1, 0.1)
    kp, des = sift.detectAndCompute(train,None)
    BOW.add(des)

dictionary = BOW.cluster()
print dictionary
np.save("train/bow_dictionary.npy", dictionary)
