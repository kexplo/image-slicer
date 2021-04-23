.PHONY: init test lint format build

CODE = image_slicer

poetry.lock:
	$(MAKE) init

init:
	poetry install

test: poetry.lock
	poetry run pytest

lint: poetry.lock
	poetry run black --line-length=79 --check --diff $(CODE)
	poetry run flake8 image_slicer --count --show-source --statistics

format: poetry.lock
	poetry run black --line-length=79 $(CODE)

build: poetry.lock
	poetry build
