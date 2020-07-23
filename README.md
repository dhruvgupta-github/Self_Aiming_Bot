# Self_Aiming_Bot
Video:
1. https://drive.google.com/file/d/1NxzPEN158nHj_AZZ6b__OlP5FzrGNjoZ/view?usp=sharing
2. https://drive.google.com/file/d/1YSd1IQCLcG7r4AAytBFFB_AUqV9GD7Uf/view?usp=sharing
### What is does ...
The bot has the ability to aim at the centeroid of any uniformed colored object using a Laser in a 2D plane.
The bot actuates with the help of 2 servo motors and detects colour using a camera.
### How it works ...
Working of bot has 2 aspects to it :-
#### 1. Hardware
The bot's frame basically forms a upside down "T" shape with 2 servo motors attatched on the vertical line in such a orientation that it provides 2D motion of 
a laser attatched to them.
Basically one servo allows rotation along y-axis and the second placed on top of it provides motion along x-axis.
The horizontal part(base) is basically a hollow cuboid.
The base has the camera attatched to it one the top of it and the power source(LiPo) and the micro-controller(Arduino) are placed inside the cuboid.
The whole structure is built from aluminium.

Images: https://drive.google.com/file/d/1S1nGumZOUwbty_NKC2zd2IPh2QHkuLpI/view?usp=sharing
#### 2. Sofware
I used Arduino Uno microcontroller for motor actuation and OpenCV for color detection.As both the python script for color detection and Arduino has to perform in synchronization hence this was achieved through asynchronous communication through pySerial library.
Both the codes are provided in "code" folder and are self-explanatory .

#### Additional
I used a PS4 camera and hence required a camera driver, this driver is also provided in the "cleye_drivrs".
I would prefer using logitech cameras as they do not require any additional drivers.


Actual Completion date : 15 Aug 2018
