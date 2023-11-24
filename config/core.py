from pathlib import Path
from typing import Optional, Sequence

from pydantic import BaseModel
from strictyaml import YAML, load

import model

PACKAGE_ROOT = Path(model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
print(PACKAGE_ROOT)
print(ROOT)