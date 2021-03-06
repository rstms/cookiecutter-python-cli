#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{%- else %}
import unittest
{%- endif -%}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
{%- endif %}

from {{ cookiecutter.project_slug }} import __version__{% if cookiecutter.command_line_interface|lower == 'click' %}, cli{% endif %}, {{ cookiecutter.project_slug }}

{%- if cookiecutter.use_pytest == 'y' %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
{%- if cookiecutter.command_line_interface|lower == 'click' %}


def test_version():
    """Test reading version and module name"""
    assert {{ cookiecutter.project_slug }}.__name__ == "{{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}"
    assert __version__
    assert isinstance(__version__, str)


def test_cli():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code != 0, result
    assert result.exception, result
    assert "{{ cookiecutter.project_slug }}" in str(result.exception), result

    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0, result
    assert "Show this message and exit." in result.output, result
{%- endif %}
{%- else %}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
{%- if cookiecutter.command_line_interface|lower == 'click' %}

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli)
        assert result.exit_code != 0, result
        assert result.exception, result
        assert "{{ cookiecutter.project_slug }}.cli" in str(result.exception), result
        help_result = runner.invoke(cli, ["--help"])
        assert help_result.exit_code == 0, result
        assert "--help  Show this message and exit." in help_result.output, result
{%- endif %}
{%- endif %}
