// Display temperature using DHT11 using Arduino Mega
// DHT black wire to pin 2
// DHT white wire to pin 5v
// DHT brown wire to ground
// Paul McWhorter's class https://www.youtube.com/watch?v=kF6biceKwFY

#include "DHT.h"                //include DHT library
#define DHTPIN 2                //define which port will read DHT data
#define DHTTYPE DHT11           //define which type of DHT we're using

float tempF;
float tempC;
float humidity;
int setTime=500;
int dt=1000;

DHT TH(DHTPIN,DHTTYPE);         //pass to DHT library the TH object and pin and type

void setup(){
// put setup code here to run once
Serial.begin(115200);           //open serial port at 115200 baud
TH.begin();                     //start serial
delay(setTime);                 //delay
}

void loop(){
// main code goes here

//tempC=TH.readTemperature();   //celcius
tempF=TH.readTemperature(true); //read the temperature, true = faherenheit
humidity=TH.readHumidity();     //read the humidity

Serial.print(tempF);            //print temperature in F
Serial.print(",");              //print comma
Serial.println(humidity);       //print humidity
delay(dt);                      //delay of dt
}
