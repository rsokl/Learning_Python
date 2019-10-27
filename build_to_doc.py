# script for prepping docs/ from new sphinx build
# docs/ -> docs_backup/
# _build/ -> docs/
# ensures nojekyll and CNAME are in place

from pathlib import Path

from plymi import build_to_doc
build_to_doc(Path("."))

