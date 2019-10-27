"""
Utilities for accessing the PLYMI source material and making conversions using jupytext
"""

from pathlib import Path
from typing import Dict, List, Union, Callable
import shutil

try:
    from tqdm import tqdm
except ImportError:
    tqdm = lambda x: x


__all__ = [
    "get_all_markdown_files",
    "get_all_notebook_files",
    "convert_all_ipynb_to_markdown",
    "convert_all_markdown_to_ipynb",
    "build_to_doc",
]

all_source_dirs = [
    Path("Module1_GettingStartedWithPython"),
    Path("Module2_EssentialsOfPython"),
    Path("Module2_EssentialsOfPython") / "Problems",
    Path("Module3_IntroducingNumpy"),
    Path("Module3_IntroducingNumpy") / "Problems",
    Path("Module4_OOP"),
    Path("Module5_OddsAndEnds"),
]


def _get_jupytext_version():
    import jupytext

    return jupytext.__version__


def get_all_markdown_files(root) -> Dict[str, List[Path]]:
    dirs = get_source_dirs_from_root(root)
    return {str(d): sorted(d.glob(f"*.md")) for d in dirs}


def get_all_notebook_files(root) -> Dict[str, List[Path]]:
    dirs = get_source_dirs_from_root(root)
    return {str(d): sorted(d.glob(f"*.ipynb")) for d in dirs}


def get_source_dirs_from_root(root: Path) -> List[Path]:
    if not isinstance(root, Path):
        root = Path(root)
    assert root.is_dir()

    dirs = [root / d for d in all_source_dirs]  # type: List[Path]

    bad = [d for d in dirs if not d.is_dir()]
    if bad:
        raise AssertionError(f"{','.join(bad)} are not a directories")
    return dirs


def _convert_all(
    *,
    root: Union[str, Path],
    file_getter: Callable[[Path], Dict[str, List[Path]]],
    verbose,
    destination_format: str,
):
    import subprocess

    assert destination_format in {"markdown", "notebook"}

    print(f"Using jupytext version: {_get_jupytext_version()}")

    for dir, files in file_getter(root).items():
        if verbose:
            print(f"Processing directory: {dir}")
        for file in tqdm(files):
            subprocess.run(["jupytext", "--to", destination_format, str(file)])


def convert_all_markdown_to_ipynb(root: Union[str, Path], verbose: bool = True):
    return _convert_all(
        root=root,
        verbose=verbose,
        file_getter=get_all_markdown_files,
        destination_format="notebook",
    )


def convert_all_ipynb_to_markdown(root: Union[str, Path], verbose: bool = True):
    return _convert_all(
        root=root,
        verbose=verbose,
        file_getter=get_all_notebook_files,
        destination_format="markdown",
    )


def build_to_doc(root: Path):
    """
    Copy all files from docs/ to docs_backup/
    Copy all files from Python/_build/ to docs/

    Checks for .nojekyll and CNAME files

    Parameters
    ----------
    root : pathlib.Path
        The path to the top-level directory containing the Python/ dir."""
    if not isinstance(root, Path):
        root = Path(root)

    assert (root / "docs").is_dir()
    assert (root / "Python" / "_build").is_dir()
    shutil.copyfile(root / "docs" / "CNAME", root / "Python" / "_build" / "CNAME")

    assert (root / "Python" / "_build" / ".nojekyll").is_file()

    if (root / "docs_backup").is_dir():
        shutil.rmtree(root / "docs_backup")
    shutil.move(root / "docs", root / "docs_backup")
    shutil.copytree(root / "Python" / "_build", root / "docs")

    assert (root / "docs" / ".nojekyll").is_file()
    assert (root / "docs" / "CNAME").is_file()
