all: test

test:
	pytest -vv
.PHONY: test

build:
	pip3 install -r requirements.txt
.PHONY: build

profile:
	python3 -m memory_profiler src/main.py
.PHONY: profile

run:
	python3 src/main.py
.PHONY: run
