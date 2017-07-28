// Pin holding the distance sensor
int sensorPin1 = 0;
// variable to hold sensor value
int sensorValue1;
// variable to calibrate low value
int sensorLow1 = 1023;
// variable to calibrate high value
int sensorHigh1 = 0;
// Pin holding the distance sensor
int sensorPin2 = 4;
// variable to hold sensor value
int sensorValue2;
// variable to calibrate low value
int sensorLow2 = 1023;
// variable to calibrate high value
int sensorHigh2 = 0;

//LED Pins
int redPin = 11;
int greenPin = 10;
int bluePin = 9;
int t1 = 5000;
int t2 = 15000;

//Function that allocates the colours on RGB LED
void setColour(int red, int green, int blue)
{
  red = 255 - red;
  green = 255 - green;
  blue = 255 - blue;
  
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);  
}

//Calibration function
void Calibration(int t, int *sensorHigh, int *sensorLow, int sensorValue, int sensorPin)
{
    // calibrate for the first five seconds after program runs
    while (millis() < t) 
    {
      setColour(255,255,255); //White
      // record the maximum sensor value
      sensorValue = analogRead(sensorPin);
      if (sensorValue > *sensorHigh) 
      {
        *sensorHigh = sensorValue;
      }
      
      // record the minimum sensor value
      if (sensorValue < *sensorLow) 
      {
        *sensorLow = sensorValue;
      }
      //In the final second RGB LED flashes blue
      while (millis() > (t-1000) && millis()< t)
       {
          setColour(0,0,0); //Off
          delay (100);
          setColour(0,0,255); //Blue
          delay (100);
       }
    }

}
 
void setup() {
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT); 

  //Calls first calibration for sensor 1
  Calibration(t1,&sensorHigh1,&sensorLow1, sensorValue1, sensorPin1);
  Serial.print("S1:");
  Serial.println(sensorLow1);
  Serial.print("S1:");
  Serial.println(sensorHigh1);

  //Five second delay betwenn calibration
  setColour(255,0,0); //Red
  delay(5000);
  
  //Colour change indicates start of next calibration
  setColour(255,255,255); //White
  //calls second calibration for sensor 2
  Calibration(t2,&sensorHigh2, &sensorLow2, sensorValue2, sensorPin2); 
  Serial.print("S2:");
  Serial.println(sensorLow2);
  Serial.print("S2:");
  Serial.println(sensorHigh2);
}

void loop()
{
  //Reads the values produced from the sensor
  sensorValue1 = analogRead(sensorPin1);
  sensorValue2 = analogRead(sensorPin2);

  //When the values are between the max and min values for sensor 1
  if(sensorValue1 > sensorLow1 && sensorValue1 < sensorHigh1)
  {
     //Prints the value of sensor 1 when in range
     Serial.print("S1:");
     Serial.println(sensorValue1);
     //setColour(0,255,0); //Green
  }
  else 
  {
    //Prints the value of sensor 1 when out of range
    Serial.print("S1:");
    Serial.println(sensorValue1);
    //setColour(255,0,0); //Red
  }
  
  //When the values are between the max and min values for sensor 2
  if(sensorValue2 > sensorLow2 && sensorValue2 < sensorHigh2)
  {
    //Prints the value of sensor 1 when in range
    Serial.print("S2:");
    Serial.println(sensorValue2);
    //setColour(0,0,255); //Blue
  }
  else 
  {
    //Prints the value of sensor 1 when out of range
    Serial.print("S2:");
    Serial.println(sensorValue2);
    //setColour(255,255,0); //Something?
  }

  //Half a second delay between printing values
  delay(500); 
  

}


