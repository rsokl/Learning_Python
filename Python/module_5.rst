Module 5: Odds and Ends
=====================================
This module contains materials that are extraneous to the essentials of Python as a language and of NumPy, but are nonetheless critical to doing day-to-day work using these tools. 

The first section introduces matplotlib, a library that allows us to plot and visually inspect data. Here, we will specifically learn how to leverage matplotlib's object-oriented API, as opposed to its functional API, for creating scatter plots, line plots, histograms, and image plots.

The next section presents the "best practices" for working with files in Python. This includes reading from and writing to files within a context manager. We will learn to leverage the powerful `pathlib.Path` class to work with paths in elegant and platform-independent ways. Finally, we review some critical file utilities, like searching for files with `glob`, saving files with `pickle`, saving NumPy arrays.

Moving forward, we will study Python's packaging system, which gives us insight into what the `import` statement is all about. This naturally leads us to consider what it actually means to install a Python package on one's machine. We will review the `pip` and `conda` package managers, which are the two prominent means for installing and managing Python packages on one's machine. This is section will be critical for anyone interesting in maturing from a Jupyter notebook-only Python user to someone who can craft their own installable Python project. It will also greatly improve your ability to troubleshoot Python-related technical issues on your machine.

More sections will be added to this module down the road.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Module5_OddsAndEnds/Matplotlib.ipynb
   Module5_OddsAndEnds/WorkingWithFiles.ipynb
   Module5_OddsAndEnds/Modules_and_Packages.ipynb


   
