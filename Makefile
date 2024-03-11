setup: install build publish package-install brain-games

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

brain-games:
	poetry run brain-games
