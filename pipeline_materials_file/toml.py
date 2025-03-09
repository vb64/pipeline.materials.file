"""Materials toml stuff."""


class MaterialsToml:
    """Materials of pipline in toml format."""

    file_name = "materials.toml"
    encoding = 'utf-8'

    def __init__(self):
        """Make new material list."""
        self.materials = {}
        self.default = None
        self.pipe_types = {}
        self.pipe_numbers = {}
