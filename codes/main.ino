#include "headers/MHZ.h"
//#include <ESP8266WiFi.h>
#include <SoftwareSerial.h>

const int MQ136 = A0;
const int MQ137 = A1;
const int ITER_TIME = 500;
const int SETUP_DELAY = 200;
const int LOOP_DELAY = 2000;
const int CO2_IN = 10;
MHZ mhz19b(CO2_IN, MHZ19B);

void setup()  // Runs only once
{
	Serial.begin(9600);
	/*pinMode(CO2_IN, INPUT);
	while(!mhz19b.isReady())
		delay(SETUP_DELAY);*/
	Serial.println("debugging...");
	Serial.println("MQ-136  for H2S");
	Serial.println("MQ-137  for NH3");
	Serial.println("MH-Z19B for CO2 and temperature");
	Serial.println("----------start recording----------");
}

void loop() {
	mq136_routine();
	mq137_routine();
	// mhz19b_routine();
	delay(LOOP_DELAY);
}

void mq136_routine() {
	const double SO2_CURVE[] = { 40.44109566, -1.085728557 };  // reference is mentioned in readme
	double mq136 = 0.0;
	double sum136 = 0.0;

	for(int test_cycle = 1; test_cycle <= ITER_TIME; test_cycle++) {
		sum136 += analogRead(MQ136);
	}
	mq136 = sum136 / ITER_TIME;

	Serial.print("H2S average data: ");
	Serial.println(mq136);
}

void mq137_routine() {
	const double RL = 47;	  // The value of resistor RL is 47K
	const double m = -0.263;  // Enter calculated Slope
	const double b = 0.42;	  // Enter calculated intercept
	const double Ro = 20;	  // Enter found Ro value
	double VRL;				  // Voltage drop across the MQ sensor
	double Rs;				  // Sensor resistance at gas concentration
	double ratio;			  // Define variable for ratio

	VRL = analogRead(MQ137) * (5.0 / 1023.0);		 // Measure the voltage drop and convert to 0-5V
	Rs = ((5.0 * RL) / VRL) - RL;					 // Use formula to get Rs value
	ratio = Rs / Ro;								 // find ratio Rs/Ro
	double ppm = pow(10, ((log10(ratio) - b) / m));	 // use formula to calculate ppm

	Serial.print("NH3 (ppm) = ");
	Serial.println(ppm);
}

void mhz19b_routine() {
	int co2_ppm = mhz19b.readCO2PWM();
	int temperature = mhz19b.getLastTemperature();

	Serial.print("CO2 (ppm) = ");
	Serial.println(co2_ppm);
	Serial.print("temperature = ");
	Serial.println(temperature);
}