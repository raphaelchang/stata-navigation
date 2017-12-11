import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt
import surf_match as sm

TOP_CHECKS = 5

def Query(queryFile):
    dictionary = np.load("train/bow_dictionary.npy")
    train = np.load("train/bow_train.npy")
    locs = np.load("maps/map_tags.npy")
    sift = cv2.xfeatures2d.SIFT_create()
    bowExtract = cv2.BOWImgDescriptorExtractor(sift, cv2.BFMatcher(cv2.NORM_L2))
    bowExtract.setVocabulary(dictionary)

    query = cv2.imread(queryFile)
    query = cv2.resize(query, (0, 0), None, 0.1, 0.1)
    kp, des = sift.detectAndCompute(query, None)
    bowDescriptor = bowExtract.compute(query, kp)
    similarities = np.empty((0, 1))

    for t in train:
        similarity = np.dot(bowDescriptor, t.T) / (np.linalg.norm(bowDescriptor) * np.linalg.norm(t))
        similarities = np.append(similarities, np.atleast_2d(similarity), axis=0)

    topSim = np.argsort(similarities, axis=0)[::-1]

    best_inlier = 0
    best_train = 0
    for i in range(0, min(TOP_CHECKS, train.shape[0])):
        trainImg = cv2.imread('train/' + str(topSim[i][0] + 1) + '.jpg')
        trainImg = cv2.resize(trainImg, (0, 0), None, 0.1, 0.1)
        qpts, tpts = sm.FindMatches(query, trainImg)
        H, inlierMask = cv2.findHomography(qpts, tpts, cv2.RANSAC, 10.0)
        numInliers = inlierMask.ravel().tolist().count(1)
        if numInliers > best_inlier:
            best_inlier = numInliers
            best_train = topSim[i][0]
        # imwarp = cv2.warpPerspective(query, H, (trainImg.shape[1], trainImg.shape[0]))
        # cv2.imshow("Transformed", imwarp)
        # cv2.imshow("Original", trainImg)
        # cv2.waitKey(0)
    loc = locs[int(best_train / 2)]
    return (loc[0], loc[1], loc[2], best_train % 2)


if __name__ == '__main__':
    print Query(sys.argv[1])
