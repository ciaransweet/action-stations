.PHONY: install
install:
	npm install
	poetry install
	echo "\r\nUSE THIS FOR IDE COMPLETION:\r\n\r\n$$(poetry env info -p)"

.PHONY: lint
lint:
	poetry run flake8 cdk/ src/ tests/
	poetry run isort --check-only --profile black cdk/ src/ tests/
	poetry run black --check --diff cdk/ src/ tests/

.PHONY: format
format:
	poetry run isort --profile black cdk/ src/ tests/
	poetry run black cdk/ tests/

.PHONY: unit-tests
unit-tests:
	poetry run pytest -s tests/unit/

.PHONY: diff
diff:

