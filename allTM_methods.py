import cv2
import numpy as np

def templateMatching(method):
    img_rgb = cv2.imread('cats.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('nasuc.png',0)
    w, h = template.shape[::-1]


    res = cv2.matchTemplate(img_gray,template,method=method)


    #accuracy
    threshold = 0.85
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv2.imwrite('allTMmethods.png',img_rgb)

templateMatching(5)
'''
TM_CCOEFF = 4
TM_CCOEFF_NORMED = 5
TM_CCORR = 2
TM_CCORR_NORMED = 3
TM_SQDIFF = 0
TM_SQDIFF_NORMED = 1
'''