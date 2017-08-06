// Pin holding the distance sensor
int sensorPin1 = A0;
// variable to hold sensor value
int sensorValue1;
// variable to calibrate low value
int sensorLow1 = 1023;
// variable to calibrate high value
int sensorHigh1 = 0;
// Pin holding the distance sensor
int sensorPin2 = A4;
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


void setup() {
  //Intiliases all the input/output pins used
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop()
{
  //Reads the values produced from the sensor
  sensorValue1 = analogRead(sensorPin1);
  sensorValue2 = analogRead(sensorPin2);

  //Prints out the readings from the two sensors
  Serial.print("S1:");
  Serial.println(sensorValue1);

  delay(100);

  Serial.print("S2:");
  Serial.println(sensorValue2);

  //Half a second delay between printing values
  delay(500);


}
