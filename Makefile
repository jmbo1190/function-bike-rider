install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=hellocli test_hello.py

format:
	black *.py
	
lint:
	pylint --disable=R,C hello.py hellocli.py
	
copy-jpg:
	aws s3 cp ../*.jpg s3://cloud-comp-found-function-bike-rider
	
copy-jpg-back:
	aws s3 cp s3://cloud-comp-found-function-bike-rider .. --recursive --exclude "*" --include "*.jpg"

all: install lint format test