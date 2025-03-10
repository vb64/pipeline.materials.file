"""Module toml tests.

make test T=test_toml.py
"""
import toml
from pipeline_material import PipeMaterial
from . import TestBase


class TestToml(TestBase):
    """Tests toml module."""

    def test_materials_toml(self):
        """Check key property."""
        from pipeline_materials_file.toml import MaterialsToml
        from pipeline_materials_file.types import PipeType

        matoml = MaterialsToml(None)
        assert matoml is not None
        assert matoml.default_material is None
        assert not matoml.materials
        assert matoml.get_material(PipeType.DIRECT, 100, '') is None

        steel = PipeMaterial("Сталь", 295)
        assert steel.smys == 295
        matoml = MaterialsToml(steel)
        assert matoml.default_material.name == "Сталь"
        assert len(matoml.materials) == 1
        assert matoml.get_material(PipeType.DIRECT, 100, '').name == "Сталь"

        fname = self.build("dflt.toml")
        assert matoml.save(fname) is not None

        data = None
        with open(fname, 'r', encoding=MaterialsToml.encoding) as inp:
            data = toml.load(inp)
        assert len(data) == 2
        # print("#", data)
