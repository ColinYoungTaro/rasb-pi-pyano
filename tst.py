import cv2
from PIL import Image
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
_,frame = vc.read()
img = frame * 255
img = img.astype("uint8")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
im = Image.fromarray(img)
img = im.toqpixmap()