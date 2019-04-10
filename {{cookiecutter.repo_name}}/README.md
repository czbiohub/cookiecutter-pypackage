{{ cookiecutter.project_name }}
================================

[![image](https://img.shields.io/travis/%7B%7B%20cookiecutter.github_organization%20%7D%7D/%7B%7B%20cookiecutter.repo_name%20%7D%7D.svg)](https://travis-ci.org/%7B%7B%20cookiecutter.github_organization%20%7D%7D/%7B%7B%20cookiecutter.repo_name%20%7D%7D)


[![codecov](https://codecov.io/gh/%7B%7B%20cookiecutter.github_organization%20%7D%7D/%7B%7B%20cookiecutter.repo_name%20%7D%7D/branch/master/graph/badge.svg)](https://codecov.io/gh/%7B%7B%20cookiecutter.github_organization%20%7D%7D/%7B%7B%20cookiecutter.repo_name%20%7D%7D)

[![image](https://img.shields.io/pypi/v/%7B%7B%20cookiecutter.repo_name%20%7D%7D.svg)](https://pypi.python.org/pypi/%7B%7B%20cookiecutter.repo_name%20%7D%7D)


What is {{ cookiecutter.repo_name }}?
-------------------------------------

{{ cookiecutter.project_short_description}}

-   Free software: MIT license
-   Documentation: <https://>{{ cookiecutter.github_organization }}.github.io/{{
    cookiecutter.repo_name }}

Installation
------------

To install this code, clone this github repository and use pip to install

```
git clone <https://github.com/>{{ cookiecutter.github_organization }}/{{ cookiecutter.repo_name }}.git 
cd {{ cookiecutter.repo_name }} 

# The "." means "install *this*, the folder where I am now"
pip install . 
```

Usage
-----

Greet a name multiple times!

```
$ {{ cookiecutter.project_name }} hello --name "Rosalind Franklin" --count 10 
```


Features
--------

-   TODO

