#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.repo_name }}
----------------------------------

Tests for `{{ cookiecutter.repo_name }}` module.
"""

import pytest


class Test{{ cookiecutter.repo_name|capitalize }}(object):

    def test___init__(self, one_hundred):
        assert 100 == one_hundred
