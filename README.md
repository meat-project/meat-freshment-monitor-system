# Meat-Freshment-Monitor-System (肉類食品新鮮度監測系統)

---

## Usage

1. `cd meat-freshment-monitor-system/codes/main`
   - open ardion IDE, then compile and upload code.
2. `cd meat-freshment-monitor-system/codes/python_`
3. `make`
4. `make run`

### Arduino

1. 在 `meat-freshment-monitor-system/codes/main` 資料夾中
2. makefile 有解決 permission 問題和自動排版的功能，使用 `make` 功能即可。
3. 使用 arduino IDE 作為環境， upload 後，即可開始使用 python code 預測。

### python code

1. 使用 arduino IDE upload code 到 arduino board 之後，到 `meat-freshment-monitor-system/codes/python_` 資料夾中
2. 使用 makefile 即可建立模型，並開始即時預測肉類新鮮度分類。
3. 若有 makefile 使用上問題，可使用 `make help`

### problems

- `[Error] Uploading sketch 'sensor.ino': Exit with code=1`
  - modify the permission of `/dev/ttyACMXXX`(varies depending on device) port, which arduino board used, with the command `chmod`

  - it's fixed in makefile

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
- [英文字體 Times New Roman 字體格式連結(微軟版本)](https://aur.archlinux.org/packages/ttf-ms-win10/)
