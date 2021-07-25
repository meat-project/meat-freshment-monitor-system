//#include "headers/MHZ.h"

const int MQ136 = A0;
const int MQ137 = A1;
const int ITER_TIME = 500;

void setup()  // Runs only once
{
	Serial.begin(9600);	 // Initialise serial COM for displaying the value
}

void loop() {
	float mq136 = 0.0;
	float mq137 = 0.0;
	float sum136 = 0.0;
	float sum137 = 0.0;

	for(int test_cycle = 1; test_cycle <= ITER_TIME; test_cycle++) {
		sum136 += analogRead(MQ136);
		sum137 += analogRead(MQ137);
	}

	mq136 = sum136 / ITER_TIME;
	mq137 = sum137 / ITER_TIME;
	Serial.print("mq136 average data = ");
	Serial.println(mq136);
	Serial.print("mq137 average data = ");
	Serial.println(mq137);

	delay(1000);
}