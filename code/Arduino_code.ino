#include <Servo.h>



int anglex=90;
int rx=90;
int ry=90;
int angley=90;
String angleTemp = ""; 
char rec = ' ';

int read_flag = 0;


Servo myservo_x;

Servo myservo_y;// create servo object to control a servo

// twelve servo objects can be created on most boards



//int pos = 0;    // variable to store the servo position

int i = 0;
int j = 0;

void setup() {

  Serial.begin(9600);

  myservo_x.attach(8);  // attaches the servo on pin 9 to the servo object

  myservo_y.attach(6);

 
}





void loop()
{
  
// myservo_x.write(anglex);

//  myservo_y.write(angley);


    
if(Serial.available()>0)
{

rec = Serial.read();

if(rec == 'e')
{
  read_flag = 2;
}

if(read_flag == 1)
{
  angleTemp += rec;
}

if(rec == 's')
{
  read_flag = 1;
  angleTemp = "";
  
}



//delay(500);
  //Serial.flush();

if(read_flag == 2)
{
  
 for(i=2;i>=0;i--)
{
  if(i==2)
  anglex=(angleTemp[i]-'0');
  if(i==1)
  anglex=anglex+((angleTemp[i]-'0')*10);
  if(i==0)
  anglex=anglex+((angleTemp[i]-'0')*100);
    //int rx=map(anglex,180,0,108,62);
  
    
  
 }
  for(i=5;i>=3;i--)
{
  if(i==5)
  angley=(angleTemp[i]-'0');
  if(i==4)
  angley=angley+((angleTemp[i]-'0')*10);
  if(i==3)
  angley=angley+((angleTemp[i]-'0')*100);
   // int ry=map(angley,180,0,100,71);
  
 }
}
}


  myservo_x.write(anglex);

   myservo_y.write(angley);

//Serial.flush();


}





/*void loop() {

  while (Serial.available() == 0) {

    //    data_x=Serial.read();

    //    data_y=Serial.read();

    for (int i = 0; i <= 1; i++) {

      data[i] = Serial.read();

    }



    myservo_x.write(data[0]);

    myservo_y.write(data[1]);



    Serial.println(data[0]);

    Serial.println(data[1]);

  }

  

}*/











/*if(i = 3)
{
i = 0;
myservo_x.write(anglex);
//Serial.println(data[0]);

delay(500);
}*/


/*if(Serial.available()==1)
{
angleTempy= Serial.readString();

  
 for(i=0;i<3;i++)
{
  if(i==0)
  angley=(angleTempy[i]-'0');
  if(i==1)
  angley=angley+((angleTempy[i]-'0')*10);
  if(i==2)
  angley=angley+((angleTempy[i]-'0')*100);
  
    
  
 }
}*/

/*if(i = 3)
{
i = 0;
myservo_y.write(angley[0]);
//Serial.println(data[0]);

delay(500);
}*/
