#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_hello
----------------------------------

Tests for `{{ cookiecutter.repo_name }}` module.
"""

from click.testing import CliRunner


def test_hello():
    from {{ cookiecutter.repo_name }}.hello import hello

    runner = CliRunner()
    result = runner.invoke(hello, input="Rosalind Franklin")

    assert result.exit_code == 0
    assert result.output.count("Hello Rosalind Franklin") == 5


def test_hello_name():
    from {{ cookiecutter.repo_name }}.hello import hello

    runner = CliRunner()
    result = runner.invoke(hello, ["--name", "Rosalind"])

    assert result.exit_code == 0
    assert result.output.count("Hello Rosalind") == 5


def test_hello_count():
    from {{ cookiecutter.repo_name }}.hello import hello

    runner = CliRunner()
    result = runner.invoke(hello, ["--count", "10",
                                   "--name", "Rosalind"])

    assert result.exit_code == 0
    assert result.output.count("Hello Rosalind") == 10
