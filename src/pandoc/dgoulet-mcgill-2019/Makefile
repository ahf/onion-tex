SOURCE     = slides.markdown
TARGET     = slides.pdf
TARGET_TEX = slides.tex
TEMPLATE   = beamer-ahf-simple.tex

DATA_START_DATE ?= 2010-01-01
DATA_END_DATE   ?= 2019-11-27

export TEXINPUTS:=$(shell pwd)/../../tex:${TEXINPUTS}

all: $(TARGET)

$(TARGET): $(TARGET_TEX) tikz
	latexmk -pdf -pdflatex="pdflatex --shell-escape %O %S" $(TARGET_TEX)

$(TARGET_TEX): $(SOURCE) $(TEMPLATE)
	pandoc --verbose -t beamer --slide-level 2 --template="$(TEMPLATE)" $(SOURCE) -o $(TARGET_TEX)

data:
	mkdir -p data || true

tikz:
	mkdir -p tikz || true

data/networksize.csv: data
	wget -O $@ https://metrics.torproject.org/networksize.csv?start=$(DATA_START_DATE)\&end=$(DATA_END_DATE)

data/bandwidth-flags.csv: data
	wget -O $@ https://metrics.torproject.org/bandwidth-flags.csv?start=$(DATA_START_DATE)\&end=$(DATA_END_DATE)

data/hidserv-rend-relayed-cells.csv: data
	wget -O $@ https://metrics.torproject.org/hidserv-rend-relayed-cells.csv?start=$(DATA_START_DATE)\&end=$(DATA_END_DATE)

data/iran.csv: data
	wget -O $@ https://metrics.torproject.org/userstats-bridge-country.csv?country=ir&start=$(DATA_START_DATE)\&end=$(DATA_END_DATE)

clean:
	rm -fr $(TARGET_TEX) tikz/ *.vrb *.dvi *.pdf *.aux *.auxlock *.fdb_latexmk *.fls *.log *.nav *.out *.snm *.toc || true

.PHONY: data/networksize.csv data/bandwidth-flags.csv data/hidserv-rend-relayed-cells.csv data/iran.csv
