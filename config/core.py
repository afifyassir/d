from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent

print(PACKAGE_ROOT)
print(ROOT)