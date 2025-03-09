"""Module types tests.

make test T=test_types.py
"""
from . import TestBase


class TestTypes(TestBase):
    """Tests types module."""

    def test_float2str(self):
        """Check float2str function."""
        from pipeline_materials_file.types import float2str

        assert float2str(None) == ''
