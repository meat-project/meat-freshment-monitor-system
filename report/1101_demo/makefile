all: clean
	xelatex -synctex=1 -interaction=nonstopmode --shell-escape main.tex
clean:
	rm -f main.[al]* *.synctex.gz main.toc
clean_all: clean
	rm -f main.pdf