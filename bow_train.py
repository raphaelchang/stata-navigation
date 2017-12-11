import numpy as np
import cv2
from matplotlib import pyplot as plt

NUM_TRAIN = 26
dictionary = np.load("train/bow_dictionary.npy")
sift = cv2.xfeatures2d.SIFT_create()
bowExtract = cv2.BOWImgDescriptorExtractor(sift, cv2.BFMatcher(cv2.NORM_L2))
bowExtract.setVocabulary(dictionary)
bowTrain = np.empty((0, dictionary.shape[0]))

for i in range(1, NUM_TRAIN + 1):
    train = cv2.imread('train/' + str(i) + '.jpg')
    train = cv2.resize(train, (0, 0), None, 0.1, 0.1)
    kp, des = sift.detectAndCompute(train, None)
    bowDescriptor = bowExtract.compute(train, kp)
    bowTrain = np.append(bowTrain, bowDescriptor, axis=0)

print bowTrain
np.save("train/bow_train.npy", bowTrain)
