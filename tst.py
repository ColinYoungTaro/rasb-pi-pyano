import cv2
from PIL import Image
cv2.namedWindow("preview")
vc = cv2.VideoCapture(-1)
_,frame = vc.read()
cv2.imwrite("demo.png",frame)