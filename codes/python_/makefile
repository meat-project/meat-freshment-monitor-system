all: clean
	@echo generating classifiers pickle file...
	@python3 classifier_gen.py
run:
	@echo Please make sure you have classifiers\(use \"make all\" to generate them\)
	@echo trying to classify...
	@python3 classify.py
help:
	@echo all:"   "Generate all model for classifying
	@echo run:"   "Start classify the gas
	@echo clean:" "Remove all models \(pickle files\)
clean:
	@rm -rf *.pickle