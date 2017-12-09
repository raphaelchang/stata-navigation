import cv2
import numpy as np

def FindMatches(queryImg, trainImg):
    surf = cv2.xfeatures2d.SURF_create()
    kpq, descq = surf.detectAndCompute(queryImg, None)
    kpt, desct = surf.detectAndCompute(trainImg, None)

    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)   # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descq, desct, k = 2)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)
    src_pts = np.array([kpq[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pts = np.array([kpt[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    return src_pts, dst_pts

