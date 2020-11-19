publish:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload --skip-existing --repository pypi dist/*
