all: clean
	echo -e "\e[0;31m This is not a 'complete' make command. \e[0m"
	xelatex -synctex=1 -interaction=nonstopmode --shell-escape main.tex
clean:
	rm -f *.aux
	rm -f *.bcf
	rm -f *.log
	rm -f *.run.xml
	rm -f *.synctex.gz
	rm -f *.toc
clean_all: clean
	rm -f main.pdf
