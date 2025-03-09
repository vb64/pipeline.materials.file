"""Module csv tests.

make test T=test_csv.py
"""
from . import TestBase


class TestCsv(TestBase):
    """Tests csv module."""

    def test_key(self):
        """Check key property."""
        from pipeline_materials_file import Material, PipeType

        mat = Material()
        mat.type_id = PipeType.DIRECT
        mat.thick = 100
        assert mat.key == (100, PipeType.DIRECT)

    def test_from_deftable(self):
        """Class from_deftable/to_csv methods."""
        from pipeline_csv import TypeHorWeld
        from pipeline_csv.orientation import Orientation
        from pipeline_csv.csvfile import File
        from pipeline_csv.csvfile.row import Row
        from pipeline_materials_file import Materials

        deftable = File(1000)
        deftable.data = [
          Row.as_weld(1000),
          Row.as_thick(1010, 105),
          Row.as_seam(1020, TypeHorWeld.HORIZONTAL, Orientation(3, 0), None),
          Row.as_weld(12000),
          Row.as_thick(12010, 110),
          Row.as_weld(24000),
          Row.as_thick(12010, 110),
          Row.as_weld(36000),
        ]

        warnings = []
        data = Materials.from_deftable(deftable, warnings)

        assert len(data.data) == 2
        assert not warnings

        data.to_csv(self.build('material_out.csv'))

        pipes = list(deftable.get_tubes())
        assert len(pipes) == 3
        material = data.for_pipe(pipes[0])
        assert material.thick == 105
        assert material.pipe_count == 1

    def test_from_csv(self):
        """Class from_csv method."""
        from pipeline_materials_file import Materials

        materials = Materials.from_csv(self.fixture('materials01.csv'))
        assert len(materials.data) == 2

        material = list(materials.data.values())[0]
        assert material.name == 'Сталь'
        assert material.smys > 0
        assert material.smts > 0
        assert material.toughness > 0
        assert material.type_id == 0
        assert material.thick > 0
        assert material.steel_class == ''
        assert material.pipe_count > 0

        materials = Materials.from_csv(self.fixture('not_exist.csv'))
        assert not materials.data
