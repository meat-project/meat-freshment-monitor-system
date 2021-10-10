# Meat-Freshment-Monitor-System

## Usage
### steps
1. in `.../Meat-Freshment-Monitor-System/codes/` directory, use the following 
	```bash=
	make
	```
	__makefile command__  to:
	1. fixes port __permission problem__
	2. auto-formats the arduino code
2. add the repo to the workspace in VS Code
3. upload code to arduino board, and run
### problems
- `[Error] Uploading sketch 'sensor.ino': Exit with code=1`
	- modify the permission of `/dev/ttyACMXXX`(varies depending on device) port, which arduino board used, with the command `chmod`
	- it's fixed in makefile
## Installation on Ubuntu, and use it with vscode
### IDE
- [Arduino IDE](https://www.arduino.cc/en/software) (we use Arduino 1.8.15)
### VS Code settings
- open "preferences" > "settings"
- set `Arduino: Command Path` to `arduino`
- set `Arduino: Path` to where you install arduino IDE. Here, I set it to `~/arduino-1.8.15/`

## Resource
### constants and formulas
- [some of MQ-136 code](https://github.com/Sanjay3008/Sewage-Gas-Monitoring-using-Iot-Version-2/blob/f199e6060e2b37410502cad5ec8bf4d761d838bf/Arduino%20Codes/Arduino.ino)
- [MQ-136 datasheet](http://china-total.com/product/meter/gas-sensor/MQ136.pdf)
- [MQ-137 code demo](https://circuitdigest.com/microcontroller-projects/arduino-mq137-ammonia-sensor)
### Headers
- [MH-Z CO2 sensors (MH-Z19B)](https://github.com/tobiasschuerg/MH-Z-CO2-Sensors)

## xelatex

### fonts

- [中文字體楷書格式連結](https://language.moe.gov.tw/result.aspx?classify_sn=23&subclassify_sn=436&content_sn=47)