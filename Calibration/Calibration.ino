//Sensor stuff 
int sensorPin = A0;
int sensorValue; 
int sensorLow = 1023;
int sensorHigh = 0; 

//LED stuff
int redPin = 11;
int greenPin = 10;
int bluePin = 9;

//Sets the Colour of the RGB LED
void setColour(int red, int green, int blue)
{
  //The RGB LED that we are using is a common cathode and therefore requires these calculations beforehand
  red = 255 - red; 
  green = 255 - green;
  blue = 255 - blue; 

  //Displays the RGB combo
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue); 
}

//Calibration function - uses pass by reference to insert the values 
void Calibration(int *sensorHigh, int *sensorLow, int *sensorValue, int sensorPin)
{
  //For the first 5 seconds it will calibrate
   while(millis() < 5000)
   {

    setColour(255,255,255);
    sensorValue = analogRead(sensorPin);

    if(sensorValue > sensorHigh)
    {
      *sensorHigh = sensorValue; 
    }

    if(sensorValue < sensorLow)
    {
      *sensorLow = sensorValue; 
    }

    //During the last second it will flash red 
    while(millis() > 4000 && millis() < 5000)
    {
      setColour(0,0,0);
      delay(100);
      setColour(255,0,0);
      delay(100);
    }
   }
}

//This code runs at the start 
void setup() 
{
  Serial.begin(9600);
  Calibration(&sensorHigh, &sensorLow, &sensorValue, sensorPin);

  Serial.println(sensorLow);
  Serial.println(sensorHigh);
  //Turns Green 
  setColour(0,255,0);
}

void loop() 
{



}
