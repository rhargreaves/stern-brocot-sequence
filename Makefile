all: test

test:
	pytest
.PHONY: test

build:
	pip3 install -r requirements.txt
