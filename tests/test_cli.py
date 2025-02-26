"""Tests for the CLI functionality."""

import pytest
from click.testing import CliRunner
from starshipagentic.cli import main

def test_main_help():
    """Test that the main help command works."""
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert 'Starship Agentic' in result.output

def test_version():
    """Test that the version command works."""
    runner = CliRunner()
    result = runner.invoke(main, ['--version'])
    assert result.exit_code == 0
    assert result.output.strip().startswith('main, version')
