all: run

run:
	./venv/bin/python src/run.py

install:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

uninstall:
	rm -Rf ./venv
