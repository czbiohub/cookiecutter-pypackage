cookiecutter-pypackage
======================

Cookiecutter template for a Python package. See <https://github.com/audreyr/cookiecutter>.

-   Free software: BSD license
-   Vanilla testing setup with unittest and python setup.py test
-   [Travis-CI](http://travis-ci.org/): Ready for Travis Continuous Integration testing
-   [Tox](http://testrun.org/tox/) testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4
-   [Sphinx](http://sphinx-doc.org/) docs: Documentation ready for generation with, for example, [ReadTheDocs](https://readthedocs.org/)

Usage
-----

Generate a Python package project:

    cookiecutter https://github.com/olgabot/cookiecutter-pypackage.git

Then:

-   Create a repo and put it there.
-   Add the repo to your Travis CI account.
-   Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
-   Release your package the standard Python way. Here's a release checklist: <https://gist.github.com/olgabot/5990987>

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

### Similar Cookiecutter Templates

-   [Nekroze/cookiecutter-pypackage](https://github.com/Nekroze/cookiecutter-pypackage): A fork of this with a PyTest test runner, strict flake8 checking with Travis/Tox, and some docs and setup.py differences.
-   [tony/cookiecutter-pypackage](https://github.com/tony/cookiecutter-pypackage): Fork with py2.7+3.3 optimizations. Flask/Werkzeug-style test runner, `_compat` module and module/doc conventions. See `README.rst` or the [github comparison view](https://github.com/tony/cookiecutter-pypackage/compare/olgabot:master...master) for exhaustive list of additions and modifications.
-   Also see the [network](https://github.com/olgabot/cookiecutter-pypackage/network) and [family tree](https://github.com/olgabot/cookiecutter-pypackage/network/members) for this repo. (If you find anything that should be listed here, please add it and send a pull request!)

### Fork This / Create Your Own

If you have differences in your preferred setup, I encourage you to fork this to create your own version. Or create your own; it doesn't strictly have to be a fork.

-   Once you have your own version working, add it to the Similar Cookiecutter Templates list above with a brief description.
-   It's up to you whether or not to rename your fork/own version. Do whatever you think sounds good.

### Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if they make my own packaging experience better.
