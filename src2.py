import csv
import json
import re
path = './A2/images/'
listing = os.listdir(path)
listing = listing[1:]
#Declaring the path of the test image folder and extracting the histogram feature
path2 = './Assignment2/test/'
listing2 = os.listdir(path2)
for file in listing2:
	pathft = str(path2) + file
	image = cv2.imread(pathft)
	histogramtest = hist(image.flatten(), 128)
	histogramtest = str(histogramtest)

#Recognising the herb by pattern matching with the extracted feature
for file in listing:
	pathf = str(path) + file
	image = cv2.imread(pathf)
	histogram = hist(image.flatten(), 128)
	histogram = str(histogram)
if histogram == histogramtest:
str(file)
file = ''.join([i for i in file if not i.isdigit()])
file = re.sub('.jpg', '', file)
print(file)