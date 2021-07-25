# Meat-Freshment-Monitor-System

## Usage
### steps
1. use the following __makefile command__ in `.../Meat-Freshment-Monitor-System/codes/` directory to:
	```bash=
	make
	```
	1. fixes port __permission problem__
	2. auto-formats the arduino code
2. add the repo to the workspace in VS Code
3. upload code to arduino board, and run
### problems
- `[Error] Uploading sketch 'sensor.ino': Exit with code=1`
	- set `/dev/ttyACMXXX` port, which arduino board used, with the command `chmod` (fixed in makefile)
## Installation on Ubuntu, and use it with vscode
### IDE
- [Arduino IDE](https://www.arduino.cc/en/software) (we use Arduino 1.8.15)
### VS Code settings
- open "preferences" > "settings"
- set `Arduino: Command Path` to `arduino`
- set `Arduino: Path` to where you install arduino IDE. Here, I set it to `~/arduino-1.8.15/`

## Resource
### Headers
- [MH-Z19B](https://github.com/tobiasschuerg/MH-Z-CO2-Sensors)