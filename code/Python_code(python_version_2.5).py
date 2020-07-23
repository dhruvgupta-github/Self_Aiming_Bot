import cv2
import os
#import serial
import struct
import numpy as np
import time
#ser=serial.Serial('COM3',9600)
time.sleep(2)
cam=cv2.VideoCapture(1)                     
lower =np.array([105,50,50])
upper=np.array([140,255,255])

x2 = 0
y2 = 0
x1 = 0
y1 = 0

while True:
        ret,frame=cam.read()
        if ret==False:
                print ('false')
        _frame=cv2.resize(frame,(600,600))
        frame=cv2.flip(frame,1)
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(hsv,lower,upper)
        cv2.imshow('hkj',mask)
        cx=0
        cy=0
        
        mask=cv2.erode(mask,None,iterations=2)
        mask=cv2.dilate(mask,None,iterations=2)
        contours,hierachy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        area = 0
        i_max = 0
        i = 0

        if contours != []:
            for cnt in contours:
                if(area < cv2.contourArea(cnt)):
                    area = cv2.contourArea(cnt)
                    i_max = i

                i+=1    


                    
            cnt = contours[i_max]

            
            M=cv2.moments(cnt)
            cx=int(M["m10"]/M["m00"])
            cy=int(M["m01"]/M["m00"])
            ((cx,cy),radius)=cv2.minEnclosingCircle(cnt)     
            cv2.circle(frame,(int(cx),int(cy)),int(radius)+30,(0,255,255),2)
            cv2.circle(frame,(int(cx),int(cy)),5,(0,255,0),-1)
           
            cx=int (45+(cx*.08404402))
            cy=int (81.5+(cy*.0672268))
            #x1=int(64+(cx*0.3)*.255555)
            x=str(int((-34)+(cx*1.2)))
            if len(x) == 1:
                    x = '00'+x
            if len(x) == 2:
                    x = '0'+x

            #y1=int(69+(cy*0.3)*.2211111)
            y=str(int((-34)+((180-cy)*1.5)))
            if len(y) == 1:
                    y = '00'+y
            if len(y) == 2:
                   y = '0'+y

            print(x,y)
           
            
            #data = 's'+str(x) + str(y)+'e'       


            #ser.write(str(data))
        
           # print("data sent")
##            time.sleep(0.5)
            
            #print(ser.readline())
        cv2.imshow('frame',frame)  
            
        ##        if cv2.waitKey(1) == ord('a'):
        ##            ser.write(str(data))
        
     #   if abs(x1-x2)>5 or abs(y1-y2)>5:
            #ser.write(str(data))
       #         x2=x1
       #         y2=y1
               #time.sleep(1)
                
        #time.sleep(1)

        

             
        if cv2.waitKey(1) == 27:
                break

cv2.destroyAllWindows()
cam.release()
