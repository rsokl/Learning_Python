import subprocess
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='Convert notebooks to md '
                                             'using jupytext.')
parser.add_argument('dir', metavar='d', type=str, nargs=1,
                    help='directory in which notebooks will be '
                         'found/converted')


args = parser.parse_args()

directory = Path(args.dir[0])

assert directory.is_dir()
notebooks = sorted(directory.glob("*.ipynb"))
for nb in notebooks:
    print(f"Converting {nb.name}")
    subprocess.run(["jupytext", "--to", "markdown", str(nb)])
