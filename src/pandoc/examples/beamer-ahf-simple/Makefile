SOURCE   = example.markdown
TARGET   = example.pdf
TEMPLATE = beamer-ahf-simple.tex

export TEXINPUTS:=$(shell pwd)/../../../tex:${TEXINPUTS}

all: $(TARGET)

$(TARGET): $(SOURCE)
	pandoc -t beamer --pdf-engine=pdflatex --slide-level 2 --template="../../templates/$(TEMPLATE)" $(SOURCE) -o $(TARGET)

clean:
	rm *.pdf || true
