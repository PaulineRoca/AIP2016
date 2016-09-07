INPUT_IPNB := $(wildcard *.ipynb)

OUTPUT_HTML = $(INPUT_IPNB:.md=.html)  
OUTPUT_PDF = $(INPUT_IPNB:.md=.pdf)  


.PHONY: all html clean pdf

all: html pdf

html: $(OUTPUT_HTML)

pdf: $(OUTPUT_PDF)

%.html: %.ipynb
	jupyter nbconvert $< --to html

%.pdf: %.ipynb
	jupyter nbconvert $< --to pdf
p
clean:
	@rm -f $(OUTPUT_HTML) $(OUTPUT_PDF)
