#include "MHZ.h"
#include <SoftwareSerial.h>

const int MQ136_PIN = A0;
const int MQ137_PIN = A1;
const int MHZ19B_PIN = 10;
const int ITER_TIME = 500;
const int SETUP_DELAY = 5000;
const int LOOP_DELAY = 2000;

MHZ mhz19b(MHZ19B_PIN, MHZ19B);

void setup()  // Runs only once
{
	Serial.begin(9600);
	pinMode(MQ136_PIN, INPUT);
	pinMode(MQ137_PIN, INPUT);
	pinMode(MHZ19B_PIN, INPUT);

	Serial.println("MQ-136  for H2S");
	Serial.println("MQ-137  for NH3");
	Serial.println("MH-Z19B for CO2 and temperature");
	Serial.println("----------start recording----------");
}

void loop() {
	mq136_routine();
	mq137_routine();
	mhz19b_routine();

	delay(LOOP_DELAY);
}

void mq136_routine() {
	const static float m_136 = -0.23;  // Slope
	const static float b_136 = 0.449;  // Y-Intercept
	const static float R0_136 = 43.5;  // Sensor Resistance in fresh air
	const static float RL_136 = 20.0;
	float sensor_volt;	// Define variable for sensor voltage
	float RS_gas;		// Define variable for sensor resistance
	float ratio;		// Define variable for ratio
	double sensorValue = analogRead(MQ136_PIN);

	sensor_volt = sensorValue * (5.0 / 1023.0);
	RS_gas = ((5.0 * RL_136) / sensor_volt) - RL_136;  // Get value of RS in a gas
	ratio = RS_gas / R0_136;						   // Get ratio RS_gas/RS_air
	double ppm_log = (log10(ratio) - b_136) / m_136;   // Get ppm value in linear scale according to the the ratio value
	double ppm = pow(10, ppm_log);					   // Convert ppm value to log scale

	Serial.print("H2S: ");
	Serial.print(ppm);
	Serial.println(" ppm");
}

void mq137_routine() {
	const static double RL = 47;	 // The value of resistor RL is 47K
	const static double m = -0.263;	 // Enter calculated Slope
	const static double b = 0.42;	 // Enter calculated intercept
	const static double Ro = 20;	 // Enter found Ro value
	double VRL;						 // Voltage drop across the MQ sensor
	double Rs;						 // Sensor resistance at gas concentration
	double ratio;					 // Define variable for ratio

	VRL = analogRead(MQ137_PIN) * (5.0 / 1023.0);	 // Measure the voltage drop and convert to 0-5V
	Rs = ((5.0 * RL) / VRL) - RL;					 // Use formula to get Rs value
	ratio = Rs / Ro;								 // find ratio Rs/Ro
	double ppm = pow(10, ((log10(ratio) - b) / m));	 // use formula to calculate ppm

	Serial.print("NH3: ");
	Serial.print(ppm);
	Serial.println(" ppm");
}

void mhz19b_routine() {
	int co2_ppm = mhz19b.readCO2PWM();
	Serial.print("CO2: ");
	Serial.print(co2_ppm);
	Serial.println(" ppm");

	/*int temperature = mhz19b.getLastTemperature();	// not configured due to no Rx,Tx connections.
	Serial.print("temperature = ");
	Serial.println(temperature);*/
}
