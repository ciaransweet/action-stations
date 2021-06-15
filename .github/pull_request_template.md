## What I am changing

<!---

Here you should provide a high level overview of what this PR is doing, for example:

This PR implements adds the Publish step in our CI workflow so that our Python Package is published to PyPi.

We can now install our package with `pip install our-awesome-package` 🎉

Closes #32

-->

## How I did it

<!---

Here you should do a lower-level breakdown of your PR, you should try to point out key changes to any logic and highlight notable features. For example:

* Modified `.github/workflows/ci.yaml` to include the `Publish` step
    * Uses the `our-repo/publish-to-pypi@v1` action
    * Publishes our package under the name `our-awesome-package`
* Adding extra tests in `tests/test_icecream_maker.py`
    * Add test to ensure we get the right flavours
    * Add test to ensure we can order sprinkles AND sauce
    * Refactor `generate_cone` method to be able to take in multiple designs

-->

## How you can test it

<!---

Here you should provide clear instructions to a reviewer on how they can test your changes if they checked out your branch. For example:

To test these changes, you can run:

```bash
$ python -m pytest -s tests/
```

This will run the updated test suite, you should notice:

```bash
======= test session starts ======
platform darwin -- Python 3.8.6, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/me/dev/icecream-factory
collected 3 items

tests/test_icecream_maker.py ...
```

If you want to test the changes to the workflow, you can check that they ran on this PR [here](<A link to the CI run>)

-->
