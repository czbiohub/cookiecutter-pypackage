cookiecutter-pypackage
======================

Cookiecutter template for a Python package. See <https://github.com/audreyr/cookiecutter>.


![](figures/cookiecutter_create_project.gif)

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
  sections of th
- e License and documentation
- Adds MacOS, Python, and JetBrains files to gitignore

Usage
-----


### 1. Generate a Python package project:

    cookiecutter https://github.com/czbiohub/cookiecutter-pypackage.git

This will give you a "quiz" to ask you your name, the name of the project,
release date and so on. Pressing "Enter" will use the default values.


Example output:

```
(base)
 ✘  Wed 27 Mar - 17:13  ~/code 
  cookiecutter https://github.com/czbiohub/cookiecutter-pypackage.git
You've downloaded /Users/olgabot/.cookiecutters/cookiecutter-pypackage before. Is it okay to delete and re-download it? [yes]: y
full_name [Rosalind Franklin]: Olga Botvinnik
email [olga.botvinnik@czbiohub.org]:
organization [Chan Zuckerberg Biohub]:
github_username [czbiohub]:
project_name [Python Boilerplate]: Python Boilerplate Test01
repo_name [examplepy]:
project_short_description [Python Boilerplate contains all the boilerplate you need to create a Python package.]:
release_date [2019-03-27]:
year [2019]:
license [MIT]:
version [0.1.0]:
```

### 2. Change to the newly created directory and initialize git

E.g. if your project is named `examplepy`

```
cd examplepy
```
Initialize git and add files:

```
git init
git add -A .
git commit -m "First commit"
```

Example output:

```
(base)
 Wed 27 Mar - 17:18  ~/code 
  cd examplepy
(base)
 Wed 27 Mar - 17:19  ~/code/examplepy 
  git init
Initialized empty Git repository in /Users/olgabot/code/examplepy/.git/
(base)
 Wed 27 Mar - 17:31  ~/code/examplepy   master ✔ 16☀ 
  git add -A .
(base)
 Wed 27 Mar - 17:31  ~/code/examplepy   master 40✚ ⚑ 
  git commit -m "First commit"
[master (root-commit) d1b241d] First commit
 40 files changed, 1923 insertions(+)
 create mode 100644 .editorconfig
 create mode 100644 .gitignore
 create mode 100644 .travis.yml
 create mode 100644 AUTHORS.md
 create mode 100644 CONTRIBUTING.md
 create mode 100644 HISTORY.md
 create mode 100644 LICENSE
 create mode 100644 MANIFEST.in
 create mode 100644 Makefile
 create mode 100644 README.md
 create mode 100644 conda_requirements.txt
 create mode 100644 docs/CHANGELOG_sphinx_deployment.md
 create mode 100644 docs/LICENSE_sphinx_deployment
 create mode 100644 docs/Makefile
 create mode 100644 docs/README_sphinx_deployment.md
 create mode 100644 docs/authors.rst
 create mode 100755 docs/conf.py
 create mode 100644 docs/contributing.rst
 create mode 100644 docs/history.rst
 create mode 100644 docs/index.rst
 create mode 100644 docs/installation.rst
 create mode 100644 docs/make.bat
 create mode 100644 docs/readme.rst
 create mode 100644 docs/releases/v0.1.0.rst
 create mode 100644 docs/rsync_exclude
 create mode 100644 docs/sphinx_deployment.mk
 create mode 100644 docs/tutorial.rst
 create mode 100644 docs/usage.rst
 create mode 100755 examplepy/__init__.py
 create mode 100644 examplepy/commandline.py
 create mode 100644 examplepy/hello.py
 create mode 100644 examplepy/os_utils.py
 create mode 100755 examplepy/examplepy.py
 create mode 100755 examplepy/tests/__init__.py
 create mode 100644 examplepy/tests/conftest.py
 create mode 100644 examplepy/tests/test_os_utils.py
 create mode 100755 examplepy/tests/test_examplepy.py
 create mode 100644 requirements.txt
 create mode 100644 setup.cfg
 create mode 100755 setup.py
```

### Create the remote repository on GitHub

Go to [github.com]([https://github.com](https://github.com/) ) and click the
plus sign ("+") to create a repository under the `czbiohub` organization. Since
via `cookiecutter` we already have a README and LICENSE, we don't need those
files. We'll want to check the box for Travis-CI integration to run the tests
for the code automatically.

![Example inputs for creating a repository](figures/create_repository.png)

### Push the newly created Python package to GitHub

After the repository is created, now we need to push the files we created
locally to the remote repository.

![](figures/github_repository_created_now_what.png)

```
git remote add origin https://github.com/czbiohub/examplepy.git
git push -u origin master
```



### Check out the `hello` subcommand of your program!

This comes pre-canned with an example command line subcommand and how to test it.


### Add autogenerated documentation

[Read The Docs](https://readthedocs.org/) is a great way to host and generate
your documentation. The


### Release your package!

Once you're ready to push your code to PyPI, release your package the standard
Python way. Here's a release checklist:
<https://gist.github.com/olgabot/5990987>
