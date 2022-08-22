"""
Utilities for accessing the PLYMI source material and making conversions using jupytext
"""

import shutil
from pathlib import Path
from typing import Callable, Dict, FrozenSet, List, Tuple, Union

from jupytext.cli import jupytext

try:
    from tqdm import tqdm
except ImportError:
    tqdm = lambda x: x


__all__ = [
    "get_all_markdown_files",
    "get_all_notebook_files",
    "convert_all_ipynb_to_markdown",
    "convert_all_markdown_to_ipynb",
    "convert_src_to_html",
    "build_to_doc",
    "delete_all_notebooks",
    "delete_all_markdown",
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


# The following are names of notebooks that exist natively as PLYMI
# source material. It should be excluded from markdown conversion
excluded_notebook_names = {"Matplotlib.ipynb", "Approximating_pi.ipynb"}


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

    root /= "Python"
    assert root.is_dir()

    dirs = [root / d for d in all_source_dirs]  # type: List[Path]

    bad = [d for d in dirs if not d.is_dir()]
    if bad:
        raise AssertionError(
            "The following directories do not exist: "
            + ("\n".join((str(x) for x in bad)))
        )
    return dirs


def _convert_all(
    *,
    root: Union[str, Path],
    file_getter: Callable[[Path], Dict[str, List[Path]]],
    verbose,
    destination_format: str,
    excluded_file_names: FrozenSet[str] = frozenset(),
):
    assert destination_format in {"markdown", "notebook"}

    print(f"Using jupytext version: {_get_jupytext_version()}")

    for dir, files in file_getter(root).items():
        if verbose:
            print(f"Processing directory: {dir}")
        for file in tqdm(files):
            if file.name in excluded_file_names:
                continue
            jupytext(["--to", destination_format, str(file)])


def test_ipynb_roundtrip_on_all(*, root: Union[str, Path], verbose=True):
    print(f"Using jupytext version: {_get_jupytext_version()}")

    for dir_, files in get_all_notebook_files(
        root
    ).items():  # type: Tuple[str, List[Path]]
        if verbose:
            print(f"Processing directory: {dir_}")
        for file in tqdm(files):  # type: Path
            if file.name in excluded_notebook_names:
                continue
            jupytext(["--to", "md", "--test", str(file)])


def convert_all_markdown_to_ipynb(
    root: Union[str, Path], verbose: bool = True, excluded_file_names=frozenset()
):
    assert all(name.endswith(".md") for name in excluded_file_names)
    return _convert_all(
        root=root,
        verbose=verbose,
        file_getter=get_all_markdown_files,
        destination_format="notebook",
        excluded_file_names=excluded_file_names,
    )


def convert_all_ipynb_to_markdown(
    root: Union[str, Path],
    verbose: bool = True,
    excluded_file_names=frozenset(excluded_notebook_names),
):
    assert all(name.endswith(".ipynb") for name in excluded_file_names)
    return _convert_all(
        root=root,
        verbose=verbose,
        file_getter=get_all_notebook_files,
        destination_format="markdown",
        excluded_file_names=excluded_file_names,
    )


def _delete_all(
    root: Path,
    *,
    file_getter: Callable[[Path], Dict[str, List[Path]]],
    excluded_file_names: FrozenSet[str],
    test: bool,
):
    import os

    assert test in {True, False}

    if test:
        print("Nothing will be deleted unless you pass `test=False`")
    for dir_, files in file_getter(root).items():
        for file in files:
            if file.name in excluded_file_names:
                continue
            if test:
                print(repr(file) + " will be deleted")
            else:
                os.remove(file)


def delete_all_notebooks(
    root, *, excluded_file_names=frozenset(excluded_notebook_names), test=True
):
    assert all(name.endswith(".ipynb") for name in excluded_file_names)
    return _delete_all(
        root,
        file_getter=get_all_notebook_files,
        excluded_file_names=excluded_file_names,
        test=test,
    )


def delete_all_markdown(root, *, excluded_file_names=frozenset(), test=True):
    assert all(name.endswith(".md") for name in excluded_file_names)
    return _delete_all(
        root,
        file_getter=get_all_markdown_files,
        excluded_file_names=excluded_file_names,
        test=test,
    )


def build_to_doc(root: Union[str, Path]):
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
    print("Done. Make sure to commit the changes to `docs/` and `docs_backup/`")


def convert_src_to_html(sphinx_project_root: Union[str, Path]):
    """ Runs::

        python -m sphinx . _build -j4

    in the specified directory

    Parameters
    ----------
    sphinx_project_root : Union[str, Path]
        The directory containing the sphinx conf.py file.
        (E.g. Learning_Python/Python/, if you cloned the
        PLYMI repo).
        """
    import subprocess
    import os
    wd = os.getcwd()
    os.chdir(sphinx_project_root)

    try:
        subprocess.run(["python", "-m", "sphinx", ".", "_build", "-j4"])
    finally:
        os.chdir(wd)
