all: clean
	echo -e "\e[0;31m This is not a 'complete' make command. \e[0m"
	xelatex -synctex=1 -interaction=nonstopmode --shell-escape main.tex
clean:
	rm -f main.[al]* *.synctex.gz main.toc
clean_all: clean
	rm -f main.pdf
