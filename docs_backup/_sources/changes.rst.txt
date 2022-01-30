=========
Changelog
=========

This is a record of all past PLYMI releases and what went into them,
in reverse chronological order.

----------
2021-02-28
----------

Fixes a syntax error (missing colons) in a code snippet in `a subsection about conditional expressions <https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/ConditionalStatements.html#if,-else,-and-elif>`_.


----------
2021-01-31
----------

Upgrades the tools used to build PLYMI:

- sphinx 3.4.3
- nbsphinx 0.8.1
- jupytext 1.9.1
- sphinx-rtd-theme 0.5.1

Adds a reading comprehension problem in `the section on type-hinting <https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Writing_Good_Code.html#Type-Hinting>`_
to show that ``jedi`` provides annotation-informed autocompletion abilities in notebooks.


----------
2021-01-30
----------

Updated the discussion of `computing pairwise differences <https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/Broadcasting.html#An-Advanced-Application-of-Broadcasting:-Pairwise-Distances>`_
to account for potential floating-point edge cases that can produce "NaNs" as a result.

There is currently an incompatibility between ``jedi 0.18.0`` and IPython, which breaks autocompletion. See `here <https://github.com/ipython/ipython/issues/12740>`_ for more details.
Added temporary callout boxes to the `informal introduction to Python <https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Informal_Intro_Python.html>`_ and to
the `introduction to Jupyter notebooks <https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Jupyter_Notebooks.html>`_, which instruct readers to remedy this by downgrading jedi.

Fixed a missing plot in the `introduction to Jupyter <https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Jupyter_Notebooks.html>`_ section.

Reformatted the `section on IDEs <https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Getting_Started_With_IDEs_and_Notebooks.html>`_ and added a description of PyLance.

Add link to `PLYMI's discussion board <https://github.com/rsokl/Learning_Python/discussions>`_.

----------
2021-01-24
----------

Added a brief `discussion of Python versions <https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/GettingStartedWithPython.html#Understanding-Different-Versions-of-Python>`_. Thanks `@samaocarpenter <https://github.com/samaocarpenter>`_!

Fixed typos `#160 <https://github.com/rsokl/Learning_Python/pull/160>`_ `#158 <https://github.com/rsokl/Learning_Python/pull/158>`_
`#155 <https://github.com/rsokl/Learning_Python/pull/155>`_


----------
2020-06-17
----------

Various typo fixes. Thanks to Darshan and David!


----------
2020-05-10
----------

Various typo fixes. Thanks to Patrick O'Shea and David Mascharka!


----------
2020-04-11
----------

Updated some of the "backend" technologies behind PLYMI: upgraded sphinx and nbsphinx.

Fixed a broken subsection header: "Converting a Boolean Index-Array to Integer Index-Arrays: numpy.where" will now appear in the navigation bar under Module 3, Advanced Indexing.


----------
2020-04-02
----------

Fixed a mistake in `Working with Files <https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/WorkingWithFiles.html>`_ where the
reported syntax for invoking ``Path.mkdir()`` was incorrect.


----------
2020-02-16
----------

Several various typo/grammar fixes. Thank you to the readers who reported these and to `@davidmascharka <https://github.com/davidmascharka>`_


----------
2019-12-14
----------

We're finally keeping a formal changelog! This update includes our first discussion of features that were introduced in Python 3.8. Also includes various typo/grammar fixes.

~~~~~~~~~~~
New Content
~~~~~~~~~~~

- `Module 1 - Jupyter Notebooks: <https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Jupyter_Notebooks.html>`_ included a brief discussion of Jupyter lab

- `Module 1 - Setting Up a Development Environment: <https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Getting_Started_With_IDEs_and_Notebooks.html>`_ Updated IDE discussion to reflect recent improvements to VSCode for Python.

- `Module 5 - Writing Good Code: <https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Writing_Good_Code.html#Using-the-typing-Module>`_ Added ``typing.Literal``, which was introduced in Python 3.8, to the discussion of type-hints .

- `Module 5 - Writing Good Code: <https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Writing_Good_Code.html#Using-the-typing-Module>`_ ``pyright`` is now listed alongside ``mypy`` as a tool for doing static type analysis.

