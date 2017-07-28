//Declaring variables
#include <time.h>

// Pin holding the distance sensor
int sensorPin = 0;
// variable to hold sensor value
int sensorValue;
// variable to calibrate low value
int sensorLow = 1023;
// variable to calibrate high value
int sensorHigh = 0;

int ledpin = 2;
int redPin = 11;
int greenPin = 10;
int bluePin = 9;
int button = 13;
int t1 = 5000;
int t2 = 15000;

void setColour(int red, int green, int blue)
{
  red = 255 - red;
  green = 255 - green;
  blue = 255 - blue;
  
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);  
}

void Calibration(int t, int *sensorHigh, int *sensorLow, int sensorValue, int sensorPin)
{
    // calibrate for the first five seconds after program runs
    while (millis() < t) 
    {
      // record the maximum sensor value
      setColour(255,255,255);
      sensorValue = analogRead(sensorPin);
      if (sensorValue > sensorHigh) 
      {
        *sensorHigh = sensorValue;
      }
      
      // record the minimum sensor value
      if (sensorValue < sensorLow) 
      {
        *sensorLow = sensorValue;
      }

       while (millis() > (t-1000) && millis()< t)
       {
          setColour(0,0,0);
          delay (100);
          setColour(0,0,255);
          delay (100);
       }
    }
  
}

//Registers the purpose of each pin (input or output)
void setup() 
{
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT); 
  pinMode(button, INPUT);
  setColour(0,0,0);
  Calibration(t1,&sensorHigh,&sensorLow, sensorValue, sensorPin);
  Serial.print("S1:");
  Serial.println(sensorLow);
  Serial.print("S1:");
  Serial.println(sensorHigh); 
}

//Checking when you press the button
void loop() 
  {
    sensorValue = analogRead(sensorPin);
    if(digitalRead(button) == LOW)
    {
      digitalWrite(ledpin, HIGH);
      Serial.print("S2:");
      Serial.println("2000");
                 
    }
    else
    {
      digitalWrite(ledpin, LOW);
      Serial.print("S2:");
      Serial.println ("3000");
    }
    
    if(sensorValue > sensorLow && sensorValue < sensorHigh)
    {
      Serial.print("S1:");
      Serial.println(sensorValue);
      setColour(0,255,0);
    }
    else 
    {
      Serial.print("S1:");
      Serial.println(sensorValue);
      setColour(255,0,0);
    }
    
  delay(500);
  }

