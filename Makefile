all: test

test:
	pytest -vv
.PHONY: test

build:
	pip3 install -r requirements.txt
.PHONY: build
