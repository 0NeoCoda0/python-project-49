install:
	poetry install

brain-games:
	poetry run brain-games

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

build:
	poetry build

all: install build publish package-install brain-games
