cookiecutter-pypackage
======================

Cookiecutter template for a Python package. See <https://github.com/audreyr/cookiecutter>.

-   Free software: MIT License
- Python package setup with setup.py
-   [pytest](https://docs.pytest.org/en/latest/ ) testing setup
-   [Travis-CI](http://travis-ci.org/): Ready for Travis Continuous Integration testing
    - Tests Python 3.6 and 3.7
    - Installs [miniconda](https://docs.conda.io/en/latest/miniconda.html) on
      Travis
-   [Sphinx](http://sphinx-doc.org/) docs: Documentation ready for generation with, for example, [ReadTheDocs](https://readthedocs.org/)
- Python [Click](https://click.palletsprojects.com/en/7.x/) library for simple
  command line interfaces with support for "git-like" subcommands
- [Colorama](https://pypi.org/project/colorama/) for colorful command line
  outputs
- [tqdm](https://tqdm.github.io/) for progress bars
- Specifies "Chan Zuckerberg Biohub" as the organization in the copyright
  sections of the License and documentation
- Adds MacOS, Python, and JetBrains files to gitignore

Usage
-----

Generate a Python package project:

    cookiecutter https://github.com/czbiohub/cookiecutter-pypackage.git

Then:

-   Create a repo and put it there.
-   Add the repo to your Travis CI account.
-   Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
-   Release your package the standard Python way. Here's a release checklist: <https://gist.github.com/olgabot/5990987>
