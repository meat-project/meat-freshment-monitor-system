all: clean classitier_gen
	@echo start classifying...
	@python3 serial_sensor.py
classitier_gen:
	@echo generating classifiers pickle file...
	@python3 classify_test.py
	@python3 decisiontree.py
clean:
	@echo remove classifiers
	@rm -rf *.pickle