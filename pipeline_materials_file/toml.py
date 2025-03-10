"""Materials toml stuff."""
import toml


def material_as_dict(material):
    """Return Material object as dict."""
    return {
      "smys": material.smys,  # if material.smys else "",
      "smts": material.smts,  # if material.smts else "",
      "toughness": material.toughness,  # if material.toughness else "",
    }


class MaterialsToml:
    """Materials of pipline in toml format."""

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

    def save(self, file_name):
        """Save as toml file."""
        data = {
            "materials": {key: material_as_dict(val) for key, val in self.materials.items()},
            "default": {"material": self.default_material.name if self.default_material else ''}
        }
        with open(file_name, 'w', encoding=self.encoding) as out:
            return toml.dump(data, out)
