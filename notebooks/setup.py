from pathlib import Path
import sys
import os

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

if Path.cwd() != ROOT:
    os.chdir(ROOT)