import cv2
import cv
import numpy as np
class Segment:
    def __init__(self,segments=2):
        #define number of segments
        self.segments=segments
    
#K-means Clustering
    def kmeans(self,image):
        image=cv2.GaussianBlur(image,(7,7),0)
        vectorized=image.reshape(-1,3)
        vectorized=np.float32(vectorized)
        criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        ret,label,center=cv2.kmeans(vectorized,2,criteria,10,0)
        res = center[label.flatten()]
        segmented_image = res.reshape((image.shape))
        return label.reshape((image.shape[0],image.shape[1])),segmented_image.astype(np.uint8)

#Extraction of image component
    def extractComponent(self,image,label_image,label):
        component=np.zeros(image.shape,np.uint8)
        component[label_image==label]=image[label_image==label]
        return component

if __name__=="__main__":
    import argparse
    import sys
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to the image")
    ap.add_argument("-n", "--segments", required = False, type = int,
                help = "# of clusters")
    args = vars(ap.parse_args())
    image=cv2.imread(args["image"])
    if len(sys.argv)==3:
        seg = Segment()
        label,result= seg.kmeans(image)
    else:
        seg=Segment(args["segments"])
        label,result=seg.kmeans(image)

#Extracting image features from the preprocessed image
result=seg.extractComponent(image,label,1)
r = result
result = cv2.medianBlur(result,15)
area , avg , cutoff, idx = 0 , 0 , 0 , 0
imgray = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,0,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
for cnt in contours:
    area = cv2.contourArea(cnt) + area

#Saving the herbs image individually
avg = area/len(contours)
for cnt in contours :
    idx = idx + 1
    x,y,w,h = cv2.boundingRect(cnt)
    roi = r[y:y+h, x:x+w]
    cv2.imwrite(str(idx) + 'lig6.jpg' , roi)
