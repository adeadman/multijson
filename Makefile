init:
	virtualenv venv -p python3
	./venv/bin/pip install pip --upgrade
	./venv/bin/pip install -r requirements-test.txt

clean:
	rm -rf ./venv *.egg-info .tox
	find . -name "*.pyc" -exec rm -rf {} \;

test:
	tox

publish:
	pip install twine
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*
	rm -fr build dist .egg multijson.egg-info
