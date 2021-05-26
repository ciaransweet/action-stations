# Example 3 - Manual Invocation

## TL;DR:

Example 3 is a simple workflow which `cat`s a text file depending on whether the workflow was invoked manually or not.

## Code

The example contains two files: `hello-manual.txt` and `hello-other.txt`.

## Workflow

Within [`.github/workflows/example-3-manual-invocation.yaml`](../.github/workflows/example-3-manual-invocation.yaml), we're defining one job, which has the following steps:

* Checkout the code
* Cat Hello

**Cat Hello** will `cat` either `hello-manual.txt` or `hello-other.txt` depending on if the value of `GITHUB_EVENT_NAME` is `workflow_dispatch` or not.

This workflow **only** runs when either a commit is pushed to the `main` branch, or when a pull request is raised against the `main` branch, **OR** when you manually invoke it via a button on the GitHub UI:

![Workflow Dispatch UI](./workflow_dispatch_ui.png)

This is different to re-running a flow, which will only run with the exact same state it did previously.
