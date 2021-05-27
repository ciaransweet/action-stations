.PHONY: example-1-install
example-1-install:
	$(MAKE) -C example-1-lint-and-unit-tests install

.PHONY: example-1-lint
example-1-lint:
	$(MAKE) -C example-1-lint-and-unit-tests lint

.PHONY: example-1-format
example-1-format:
	$(MAKE) -C example-1-lint-and-unit-tests format

.PHONY: example-1-unit-tests
example-1-unit-tests:
	$(MAKE) -C example-1-lint-and-unit-tests unit-tests

.PHONY: example-2-install
example-2-install:
	$(MAKE) -C example-2-caching install

.PHONY: example-2-lint
example-2-lint:
	$(MAKE) -C example-2-caching lint

.PHONY: example-2-format
example-2-format:
	$(MAKE) -C example-2-caching format

.PHONY: example-2-unit-tests
example-2-unit-tests:
	$(MAKE) -C example-2-caching unit-tests

.PHONY: example-5-install
example-5-install:
	$(MAKE) -C example-5-cdk-with-environments install

.PHONY: example-5-lint
example-5-lint:
	$(MAKE) -C example-5-cdk-with-environments lint

.PHONY: example-5-format
example-5-format:
	$(MAKE) -C example-5-cdk-with-environments format

.PHONY: example-5-unit-tests
example-5-unit-tests:
	$(MAKE) -C example-5-cdk-with-environments unit-tests

.PHONY: example-5-integration-tests
example-5-integration-tests:
	$(MAKE) -C example-5-cdk-with-environments integration-tests

.PHONY: example-5-diff
example-5-diff:
	$(MAKE) -C example-5-cdk-with-environments diff

.PHONY: example-5-deploy
example-5-deploy:
	$(MAKE) -C example-5-cdk-with-environments deploy

.PHONY: example-5-destroy
example-5-destroy:
	$(MAKE) -C example-5-cdk-with-environments destroy

.PHONY: example-5-put-message
example-5-put-message:
	$(MAKE) -C example-5-cdk-with-environments put-message
