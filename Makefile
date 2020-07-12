build:
	python3 setup.py build

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

install:
	python3 setup.py build
	python3 setup.py install

sdist:
	python3 setup.py sdist bdist_wheel

start_server:
	python3 -m coffeehouse_languagedetection --start-server