# AutoML Template
A template that provides all the tools to ensure the same project setup across all AutoML packages.

Some core features:
* Documentation for code and examples with customized theme
* Code quality tools all configured and ready to use
* Github workflows for testing, documentation and code quality
* Ready for PyPI distribution
* Everything bundled up in a `Makefile` (`make help`)

Just skip to [steps](#steps) for using this, otherwise feel free to learn more by looking through the [details](#details).

## Steps

#### Renaming to your package name
We need make two distinctions
* **name** is how it should appear in the documentation and as a title on PyPi, i.e. "AutoMLTemplate"
* **package-name** is the name of your `"src"` folder and how people should import it, i.e. `automl_template`.

We'll pretend the **name** of your package is "MyPackage" and your **package-name**  is `mypackage`. You'll have to change these in a few locations and search and replace is your friend.
1. The `automl_template` folder gets changed to `mypackage`.
2. In `pyproject.toml`, search-replace `automl_template` to `mypackage`
3. In `Makefile`, you'll find two variables, `NAME` and `PACKAGE_NAME`, change these accordingly.
4. In `.github/workflows/pytest.yml`, change the `env` variable `package-name` from `automl_template` to `mypackage` in .
5. In `.github/workflows/docs.yml`, change the `env` variable `name` from `AutoMLTemplate` to `MyPackage`.
6. In `MANIFEST.in`, use `mypackage` instead of `automl_template`
7. In `mypackage.__init__.py`, fix `package_name="automl_template"` to `package_name="mypackage"`

#### Enabling Docs
Enable github pages by going to the repos `settings` and choosing `main` as your branch. You can leave the default `/root` for the folder.

## Details

#### Package Setup
Most of the basic python packaging is setup for you, this includes the `setup.py` and everything thats required for building a source distribution that can go on PyPi.

#### Makefile
We compiled most of the useful commands into a `Makefile` and it servers as an introduction to see what kind of things are available. All of this is viewable through `make help`.
* `make install-dev` - Installs the package into the current python environment and install `pre-commit`.
* `make check` - Run all the [checkers](#checkers-and-formatting) and [formatter](#checkers-and-formatting) against the code to find potential problems.
* `make format` - Run the [formatters](#checkers-and-formatting) on the code.
* `make docs` - Make the documentation and give the link to it.
* `make test` - Run the tests.
* `make pre-commit` - Manually run pre-commit on your code, this is the same as is run in the workflows.
* `make examples` - Make the examples and give the link to it.
* `make publish` - Publish to TestPyPI and give a small guide on testing and publishing to the real PyPI.
* `make clean` - Clean any build files for doc or distribution


#### Documentation
TODO

#### Github Workflows
There is some basic workflows setup to help get you started. All of these are located in `.github/workflows`
* `pytest.yml` - This runs `pytest` on yours `tests` folder and [uploads the coverage](#codecov) to `codecov` to automatically generate reports on PRs.
* `pre-commit.yml` - This runs `pre-commit` on your files which makes sure they have all been formatted correctly as well as do `mypy` and `pydocstyle` [checking](#checkers-and-formatting).
- `docs.yml` - This uses `sphinx` to build your [documentation](#documentation) and put the `main` branch version online.
- `citation_cff.yml` - This validates any `CITATION.cff` file you may have

#### Checkers and Formatting
We use several tools to make code more consistent across all our repos and to help make everything easier to set up. The configuration for all of these tools can be found in `pyproject.toml` where there should be enough documentation to help out. You can run most of these things manually with `<checker> <file_pattern>`.
* `black` - This formats our code to a stricter version of PEP8 but grantees no actual change to the AST that is produced, i.e. code will always work the same.
* `isort` - This cleans up imports as well as sorts them based on their type. You can configure this more if needed in `pyproject.yaml`.
* `flake8` - This does code checking, making sure that variable names are defined and used or that variables or imported. This has the one exception that it's configured in `.flake8` but this shouldn't be necessary.
* `mypy` - This does static type checking on your code which helps find problems before any code is run. You will hate it before learning to love it. You can disable certain parts of it in `pyproject.toml` for specific files if needed but is not recommended practice if you can avoid it.
* `pydocstyle` - This checks that most functions have some documentation. This uses the `numpy` style of documentation which you can find [here](https://numpydoc.readthedocs.io/en/latest/format.html) but you can configure this in `pyproject.toml`. The default should not be so strict but use your best judgement for how you'd like to configure it.
* `pre-commit` - This runs all of the above every time you commit (if installed with `pre-commit install`). It makes sure that each commit is as clean as and it is exactly what is run on the github servers. You can run this manually using `pre-commit run --all-files` and it is configurable in `.pre-commit-config.yaml`.

#### Codecov
Codecov provides free access to coverage reports on open-source repositories. We have enabled this and it is configurable though `.codecov.yml`. Everytime you make a push that gets tested, `pytest.yml` will have a specific run that uploads test coverage which will then receive a comment on the PR to show you.

To disable this, you can remove the `codecov-test:` step from the `pytest.yml` file.

