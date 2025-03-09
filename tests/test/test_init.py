"""Module init tests.

make test T=test_init.py
"""
from . import TestBase


class TestInit(TestBase):
    """Tests init module."""

    def test_float2str(self):
        """Check float2str function."""
        from pipeline_materials_file.types import float2str

        assert float2str(None) == ''
