"""Module toml tests.

make test T=test_toml.py
"""
from . import TestBase


class TestToml(TestBase):
    """Tests toml module."""

    def test_materials_toml(self):
        """Check key property."""
        from pipeline_materials_file.toml import MaterialsToml

        assert MaterialsToml() is not None
