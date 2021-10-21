all: clean classitier_gen
	@echo start classifying...
	@python3 serial_sensor.py
classitier_gen:
	@echo generating classifiers pickle file...
	@python3 classify_test.py
clean:
	@rm -rf *.pickle