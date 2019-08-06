# script for prepping docs/ from new sphinx build
# docs/ -> docs_backup/
# _build/ -> docs/
# ensures nojekyll and CNAME are in place

from pathlib import Path
import shutil
root = Path(".")

assert (root/"docs").is_dir()
assert (root/"Python"/"_build").is_dir()
shutil.copyfile(root/"docs"/"CNAME", root/"Python"/"_build"/"CNAME")

assert (root/"Python"/"_build"/".nojekyll").is_file()

if (root/"docs_backup").is_dir():
    shutil.rmtree(root/"docs_backup")
shutil.move(root/"docs", root/"docs_backup")
shutil.copytree(root/"Python"/"_build", root/"docs")

assert (root/"docs"/".nojekyll").is_file()
assert (root/"docs"/"CNAME").is_file()
