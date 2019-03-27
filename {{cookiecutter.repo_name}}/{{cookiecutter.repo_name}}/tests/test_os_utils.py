import os

import pytest


def test_sanitize_path():
    from {{ cookiecutter.repo_name }}.os_utils import sanitize_path

    test = sanitize_path('.')
    true = os.path.abspath('.')
    assert test == true


def test_maybe_add_slash():
    from {{ cookiecutter.repo_name }}.os_utils import maybe_add_slash

    test = maybe_add_slash("test-folder")
    assert test == 'test-folder/'


def test_get_stdout_from_command():
    from {{ cookiecutter.repo_name }}.os_utils import get_stdout_from_command
    command = ['echo', 'asdf']
    stdout = get_stdout_from_command(command)
    assert stdout == ['asdf']


def test_get_stdout_stderr_from_command():
    from {{ cookiecutter.repo_name }}.os_utils import get_stdout_stderr_from_command

    command = ['sed', 'asdf']
    stdout, stderr = get_stdout_stderr_from_command(command)
    assert stdout == []
    assert stderr == ['sed: 1: "asdf": command a expects \ followed by text']

