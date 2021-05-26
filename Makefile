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
