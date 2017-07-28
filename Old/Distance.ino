//LED pins
int redPin = 11;
int greenPin = 10;
int bluePin = 9;

//Sensor 
int sensorPin = A0;
int sensorVal = 0;
int sensorLow = 1023;
int sensorHigh = 0; 


void setColour(int red, int green, int blue)
{
  red = 255 - red;
  green = 255 - green;
  blue = 255 - blue;

  analogWrite(redPin,red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}

void Blink()
{
  while (millis() > 1000 && millis() < 2000)
  {
    setColour(255,255,255);
    delay(1000);
    setColour(0,0,0); 
    delay(1000);
  }

  while (millis() > 2000 && millis() < 4000)
  {
    setColour(255,255,255);
    delay(200);
    setColour(0,0,0); 
    delay(200);
  }

  while (millis() > 4000 && millis() < 5000)
  {
    setColour(255,255,255);
    delay(40);
    setColour(0,0,0); 
    delay(40);
  }
}

void setup() 
{
  pinMode(redPin,OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  
  //Sensor
  Serial.begin(9600);

  
  //Turns LED to white
  setColour(255,255,255); 
  
  //Calibrate the sensor 
  while(millis() < 5000)
  {
    Blink();
    sensorVal = analogRead(sensorPin);
    if(sensorVal >= sensorHigh)
    {
      sensorHigh = sensorVal; 
    }

    if(sensorVal <= sensorLow)
    {
      sensorLow = sensorVal; 
    }
  }
  
  Serial.println(sensorLow);
}

void loop() 
{
  sensorVal = analogRead(sensorPin); 

  if (sensorVal > sensorLow  && sensorVal < sensorHigh)
  {
      setColour(0,255,0);
      Serial.println(sensorVal);
  }
  else 
  {
      setColour(255, 0, 0);
      Serial.println(sensorVal);
  }
  
  delay(400);
   
}
