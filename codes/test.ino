#include"headers/MHZ.h"

#define MQ135 A0
#define MQ137 A1
const int ITER_TIME = 500;

void setup() //Runs only once
{
  Serial.begin(9600); //Initialise serial COM for displaying the value
}

void loop() {
  float mq135 = 0.0;
  float mq137 = 0.0;
  float sum135 = 0.0;
  float sum137 = 0.0;

  for(int test_cycle = 1 ; test_cycle <= ITER_TIME ; test_cycle++)
  
  
  {
    sum135 += analogRead(MQ135);
    sum137 += analogRead(MQ137);
  }
  mq135 = sum135 / ITER_TIME;
  mq137 = sum137 / ITER_TIME;
  Serial.print("mq135 average data = ");
  Serial.println(mq135);
  Serial.print("mq137 average data = ");
  Serial.println(mq137);
  delay(1000); //delay of 1sec
}