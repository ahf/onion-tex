SOURCE   = slides.markdown
TARGET   = slides.pdf
TEMPLATE = beamer-ahf-simple.tex

DATA_START_DATE ?= 2010-01-01
DATA_END_DATE   ?= 2019-06-10

export TEXINPUTS:=$(shell pwd)/../../tex:${TEXINPUTS}

all: $(TARGET)

$(TARGET): $(SOURCE) $(TEMPLATE)
	pandoc --verbose -t beamer --slide-level 2 --template="./$(TEMPLATE)" $(SOURCE) -o $(TARGET)

data:
	mkdir -p data || true

data/networksize.csv: data
	wget -O $@ https://metrics.torproject.org/networksize.csv?start=$(DATA_START_DATE)\&end=$(DATA_END_DATE)

data/platforms.csv: data
	wget -O $@ https://metrics.torproject.org/platforms.csv?start=$(DATA_START_DATE)\&end=$(DATA_END_DATE)

data/bandwidth-flags.csv: data
	wget -O $@ https://metrics.torproject.org/bandwidth-flags.csv?start=$(DATA_START_DATE)\&end=$(DATA_END_DATE)

data/hidserv-rend-relayed-cells.csv: data
	wget -O $@ https://metrics.torproject.org/hidserv-rend-relayed-cells.csv?start=$(DATA_START_DATE)\&end=$(DATA_END_DATE)


clean:
	rm *.pdf || true

.PHONY: data/platforms.csv data/networksize.csv
