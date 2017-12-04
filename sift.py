import numpy as np
import cv2
from matplotlib import pyplot as plt

inp = cv2.imread('input.png', 0)
train = cv2.imread('panorama.png', 0)

sift = cv2.SIFT()

kp1, des1 = sift.detectAndCompute(inp,None)
kp2, des2 = sift.detectAndCompute(train,None)
