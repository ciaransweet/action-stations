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
	poetry run black cdk/ src/ tests/

.PHONY: unit-tests
unit-tests:
	poetry run pytest -s tests/unit/

.PHONY: diff
diff:
	poetry run dotenv run npx cdk diff --app cdk/app.py || true

.PHONY: deploy
deploy:
	poetry run dotenv run npx cdk deploy --app cdk/app.py --require-approval never --outputs-file example-5-outputs.json

.PHONY: destroy
destroy:
	poetry run dotenv run npx cdk destroy --app cdk/app.py --force
	rm example-5-outputs.json

.PHONY: put-message
put-message:
	@poetry run dotenv run sh -c 'python3 src/put_message.py $$IDENTIFIER example-5-outputs.json $$SECRET'
