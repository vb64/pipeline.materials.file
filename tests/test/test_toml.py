"""Module toml tests.

make test T=test_toml.py
"""
# from pipeline_material import PipeMaterial
from . import TestBase


class TestToml(TestBase):
    """Tests toml module."""

    def test_materials_toml(self):
        """Check key property."""
        from pipeline_materials_file.toml import MaterialsToml
        from pipeline_materials_file.types import PipeType

        toml = MaterialsToml(None)
        assert toml is not None
        assert toml.default_material is None
        assert not toml.materials
        assert toml.get_material(PipeType.DIRECT, 100, '') is None
