"""Materials toml stuff."""


class MaterialsToml:
    """Materials of pipline in toml format."""

    file_name = "materials.toml"
    encoding = 'utf-8'

    def __init__(self, default_material):
        """Make new material list."""
        self.default_material = default_material

        self.materials = {}
        if default_material:
            self.materials[default_material.name] = default_material

        # self.pipe_types = {}
        # self.pipe_numbers = {}

    def get_material(self, _pipe_type, _pipe_thick, _pipe_number):
        """Return material for pipe with given properties."""
        return self.default_material
