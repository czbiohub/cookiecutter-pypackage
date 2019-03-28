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
  sections of th
- e License and documentation
- Adds MacOS, Python, and JetBrains files to gitignore

Usage
-----


### 1. Generate a Python package project:

    cookiecutter https://github.com/czbiohub/cookiecutter-pypackage.git

This will give you a "quiz" to ask you your name, the name of the project,
release date and so on. Pressing "Enter" will use the default values.

### 2. Change to the newly created directory

E.g. if your project is named `python_boilerplate_test01`

```
cd python_boilerplate_test01
```

### Initialize a git repository and add files

```
git init
git add -A .
git commit -m "First commit"
```


### Create the remote repository on GitHub

![](figures/create_repository.png)

```
git remote add origin https://github.com/czbiohub/python_boilerplate_test01.git
git push -u origin master
```


Example output:

```
(base)
 Wed 27 Mar - 17:18  ~/code 
  cd python_boilerplate_test01
(base)
 Wed 27 Mar - 17:19  ~/code/python_boilerplate_test01 
  git init
Initialized empty Git repository in /Users/olgabot/code/python_boilerplate_test01/.git/
(base)
 Wed 27 Mar - 17:31  ~/code/python_boilerplate_test01   master ✔ 16☀ 
  git add -A .
(base)
 Wed 27 Mar - 17:31  ~/code/python_boilerplate_test01   master 40✚ ⚑ 
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
 create mode 100755 python_boilerplate_test01/__init__.py
 create mode 100644 python_boilerplate_test01/commandline.py
 create mode 100644 python_boilerplate_test01/hello.py
 create mode 100644 python_boilerplate_test01/os_utils.py
 create mode 100755 python_boilerplate_test01/python_boilerplate_test01.py
 create mode 100755 python_boilerplate_test01/tests/__init__.py
 create mode 100644 python_boilerplate_test01/tests/conftest.py
 create mode 100644 python_boilerplate_test01/tests/test_os_utils.py
 create mode 100755 python_boilerplate_test01/tests/test_python_boilerplate_test01.py
 create mode 100644 requirements.txt
 create mode 100644 setup.cfg
 create mode 100755 setup.py
(base)
 Wed 27 Mar - 17:31  ~/code/python_boilerplate_test01   master ✔ 
  git remote add origin https://github.com/czbiohub/python_boilerplate_test01.git
git push -u origin master
Counting objects: 45, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (35/35), done.
Writing objects: 100% (45/45), 22.78 KiB | 3.80 MiB/s, done.
Total 45 (delta 0), reused 0 (delta 0)
	To https://github.com/czbiohub/python_boilerplate_test01.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin by rebasing.
```

Then:

-   Create a repo and put it there.
-   Add the repo to your Travis CI account.
-   Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
-   Release your package the standard Python way. Here's a release checklist: <https://gist.github.com/olgabot/5990987>
