from pathlib import Path


import model

PACKAGE_ROOT = Path(model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
print(PACKAGE_ROOT)
print(ROOT)