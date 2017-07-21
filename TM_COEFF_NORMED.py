import cv2
import numpy as np

def templateMatchingTM_COEFF_NORMED(accuracy):
    #the most accurate method found
    #loads the RGB image
    img_rgb = cv2.imread('google.png')
    #transforms it into grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #loads the template
    template = cv2.imread('go.png',0)
    #gets the width and the height of the template in order to compute the area to search
    #(W-w+1) \times (H-h+1)  where W and H belon to the original image and w and h belong to the template
    w, h = template.shape[::-1]
    #computes the template matching area with cv2.TM_COEFF_NORMED
    #R(x,y)= \frac{ \sum_{x',y'} (T'(x',y') \cdot I'(x+x',y+y')) }{ \sqrt{\sum_{x',y'}T'(x',y')^2 \cdot \sum_{x',y'} I'(x+x',y+y')^2} }
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    #sets the accuracy (if the accuracy is small, it will find a lot of matchings and the rectangle will be thicker
    #if you want bigger accuracy, you have to increase the accuracy or decrease the error factor
    #locates the template on the original image
    loc = np.where( res >= accuracy)
    for pt in zip(*loc[::-1]):
        #sdraw a red rectangle in the area te template given was found in the original image
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    #creates a resulting image where the template is highlighted with red over the original image
    cv2.imwrite('res.png',img_rgb)
templateMatchingTM_COEFF_NORMED(0.85)