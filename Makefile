# Example files.
EXAMPLE_TEX_FILE   = example/example.tex
EXAMPLE_PDF_FILE   = example/example.pdf
EXAMPLE_OUTPUT_DIR = example/output

export TEXINPUTS:=$(shell pwd)/src/tex:${TEXINPUTS}

all: example

clean: example-clean

# Build the example file.
example: $(EXAMPLE_PDF_FILE)

example-clean:
	rm -rf $(EXAMPLE_OUTPUT_DIR) $(EXAMPLE_OUTPUT_DIR)

$(EXAMPLE_OUTPUT_DIR):
	mkdir $(EXAMPLE_OUTPUT_DIR)

$(EXAMPLE_PDF_FILE): $(EXAMPLE_TEX_FILE) $(EXAMPLE_OUTPUT_DIR) example-clean
	latexmk -pdf -output-directory=$(EXAMPLE_OUTPUT_DIR) $<
	cp $(EXAMPLE_OUTPUT_DIR)/$(notdir $(EXAMPLE_PDF_FILE)) $(EXAMPLE_PDF_FILE)

.PHONY: all clean example-clean
