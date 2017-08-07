
//Declaring variables
#include <time.h>

// Pin holding the distance sensor
int sensorPin = A0;
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

//Registers the purpose of each pin (input or output)
void setup() 
{
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT); 
  pinMode(button, INPUT);
}

//Checking when you press the button
void loop() 
  {
    sensorValue = analogRead(sensorPin);
    if(digitalRead(button) == LOW)
    {
      digitalWrite(ledpin, HIGH);
      Serial.print("S4:");
      Serial.println("2000");
                 
    }
    else
    {
      digitalWrite(ledpin, LOW);
      Serial.print("S4:");
      Serial.println ("3000");
    }

    delay(100);
    Serial.print("S3:");
    Serial.println(sensorValue);
    
  delay(500);
  }

