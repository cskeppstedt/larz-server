all: install test

run: install test
	python main.py

install:
	pip install -r requirements.txt

test:
	py.test --feature features
