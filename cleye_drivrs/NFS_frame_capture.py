from PIL import ImageGrab
import numpy as np
import cv2
while(True):
    img = ImageGrab.grab(bbox=(0,50,683,706)) #bbox specifies specific region (bbox= x,y,width,height)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img ,(600,600) )
    cv2.imshow("test", img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
