import numpy as np
import cv2
from matplotlib import pyplot as plt

dictionary = np.load("bow_dictionary.npy")
train = np.load("bow_train.npy")
sift = cv2.xfeatures2d.SIFT_create()
bowExtract = cv2.BOWImgDescriptorExtractor(sift, cv2.BFMatcher(cv2.NORM_L2))
bowExtract.setVocabulary(dictionary)

query = cv2.imread('query.jpg')
query = cv2.resize(query, (0, 0), None, 0.1, 0.1)
kp, des = sift.detectAndCompute(query, None)
bowDescriptor = bowExtract.compute(query, kp)

for t in train:
    similarity = np.dot(bowDescriptor, t.T) / (np.linalg.norm(bowDescriptor) * np.linalg.norm(t))
    print similarity
