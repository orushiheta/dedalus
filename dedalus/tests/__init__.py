"""Dedalus testing module."""

import pytest
import pathlib


file = pathlib.Path(__file__)
root = file.parent

def test():
    """Run tests."""
    pytest.main(['--benchmark-disable', str(root)])

def bench():
    """Run benchmarks."""
    pytest.main(['--benchmark-only', str(root)])

