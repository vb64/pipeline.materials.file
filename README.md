# Pipeline materials file for static integrity calculation

## Installation

```bash
pip install pipeline-materials-file
```

## Usage

```python
from pipeline_materials_file import Materials
from pipeline_csv.csvfile import File
from pipeline_csv.csvfile.row import Row

deftable = File(1000)
deftable.data = [
  Row.as_weld(1000),
  Row.as_thick(1010, 105),
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

data.to_csv('materials.csv')

```

## Development

```
$ git clone git@github.com:vb64/pipeline.material.git
$ cd pipeline.material
$ make setup PYTHON_BIN=/path/to/python3
$ make tests
```
