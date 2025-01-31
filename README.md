# Mypy type stubs for Matplotlib

This is a [PEP-561][pep-561]-compliant stub-only package,
which provides type information for [matplotlib][matplotlib].
The [mypy][mypy] type checker (or pytype or PyCharm) can [recognize][mypy-docs] the types in these packages by installing this package.

### NOTE: This is a work in progress

Many functions are already typed, and things can still be missing.
Chances are, you will see a message from `mypy` claiming that a function does not exist when it does exist.
If you encounter missing functions, I would be delighted for you to send a PR.
If you are unsure of how to type a function, I can discuss it.

## Installing

You can get this package only from Github, following the instructions below
Publishing to PyPi _may_ follow.

To get the most up-to-date version, install it directly from GitHub:

```bash
pip install git+https://github.com/stdedos/data-science-types
```

Or clone the repository somewhere and do `pip install -e .`.

## Philosophy

The goal is not to recreate the APIs exactly.
The main goal is to have *useful* checks on our code.
Often the actual APIs in the libraries is more permissive than the type signatures in our stubs;
but this is (usually) a feature and not a bug.

## Contributing

We always welcome contributions.
All pull requests are subject to CI checks.
We check for compliance with `mypy` and that the file formatting conforms to our Black specification.

You can install these dev dependencies via

```bash
pip install -e '.[dev]'
```

This will also install NumPy, pandas, and Matplotlib to be able to run the tests.

### Running CI locally (recommended)

We include a script for running the CI checks that are triggered when a PR is opened.
To test these out locally, you need to install the type stubs in your environment.
Typically, you would do this with:

```bash
pip install -e .
```

Then use the `check_all.sh` script to run all tests:

```bash
./check_all.sh
```

Below we describe how to run the various checks individually,
but `check_all.sh` should be easier to use.

### Checking compliance with `mypy`

The settings for `mypy` are specified in the `mypy.ini` file in the repository.
Just running:

```bash
mypy tests
```

from the base directory should take these settings into account.
We enforce 0 `mypy` errors.

### Formatting with black

We use [Black][black] to format the stub files.
First, install `black` and then run:

```bash
black .
```
from the base directory.

### Pytest

```bash
python -m pytest -vv tests/
```

### Flake8

```bash
flake8 *-stubs
```

## License

[Apache 2.0](LICENSE)


[pep-561]: https://www.python.org/dev/peps/pep-0561/
[matplotlib]: https://matplotlib.org
[mypy]: http://www.mypy-lang.org/
[mypy-docs]: https://mypy.readthedocs.io/en/latest/installed_packages.html
[black]: https://github.com/psf/black
