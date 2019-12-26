---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #raw raw_mimetype="text/restructuredtext" -->
.. meta::
   :description: Topic: Writing tests for your code, Difficulty: Easy, Category: Section
   :keywords: test, automated, pytest, parametrize, fixture, suite  
<!-- #endraw -->

# The pytest Framework

Thus far, our process for running tests has been a entirely manual one. It is time for us to arrange our test functions into a proper "test suite" and to learn to leverage [the pytest framework](https://docs.pytest.org/en/latest/) to run them.
We will begin by reorganizing our source code to create an installable [Python package](https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Modules_and_Packages.html#Packages).
We will then learn how to structure and run a test suite for this Python package, using pytest.

The pytest framework does much more than just run tests;
for instance, it will enrich the assertions in our tests to produce verbose, informative error messages.
Furthermore it provides valuable means for enhancing our tests via mechanisms like fixtures and parameterizing decorators.
Ultimately, all of this functionality helps to eliminate manual and redundant aspects of the testing process.

Note: It can be useful to [create a separate conda environment](https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Installing_Python.html#A-Brief-Introduction-to-Conda-Environments) for the sake of this lesson, so that we can work through this material starting from a blank slate.
Be sure to activate that environment and install NumPy and Jupyter notebook: `conda install numpy notebook`  

Let's install pytest. Installing from [the conda-forge channel](https://conda-forge.org/) will install the most up-to-date version of pytest. In a terminal where conda can be accessed, run:

```shell
conda install -c conda-forge pytest
```

Or, pytest is installable via pip:

```shell
pip install pytest
```


<div class="alert alert-warning">

**Regarding Alternative Testing Frameworks** (a note from the author of PLYMI): 

When sifting through tutorials, blogs, and videos about testing in Python, it is common to see `pytest` presented alongside, and  on an equal footing with, the alternative testing frameworks: `nose` and `unittest`. 
This strikes me as... bizarre.
    
`unittest` is the testing framework that comes with the Python standard library.
As a test runner, its design is clunky, archaic, and, ironically, un-pythonic.
While [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) provides extremely valuable functionality for advanced testing, all of its functionality can be leverage via pytest. 
    
`nose`, which simply extends the functionality of `unittest`, **is no longer being maintained**.
There is a project, "Nose2", which is carrying the torch of `nose`. However, this is a fledgling project by comparison to `pytest` (as of writing this, `pytest` was downloaded 12 million times last month versus `nose2`'s 150 thousand downloads).
    
The takeaway here is that, when it comes to picking a testing framework for Python, `pytest` is the clear choice.
Any discussion that you come across to the contrary is likely outdated.
</div>

<!-- #region -->
## Creating a Python Package with Tests

It's time to create a proper test suite.
Before proceeding any further, we should reread the material presented in [Module 5 - Import: Modules and Packages](https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Modules_and_Packages.html) and recall the essentials of import statements, modules, and Python packages.
This material serves as the foundation for this section.

### Organizing our Source Code
Let's create the a Python package, which we will call `plymi_mod6`, with the following directory structure:

```
project_dir/     # the "parent directory" houses our source code, tests, and all other relevant files
  - setup.py     # script responsible for installing `plymi_mod6` package
  - plymi_mod6/  # directory containing source code of `plymi_mod6` package
      |-- __init__.py
      |-- basic_functions.py
      |-- numpy_functions.py
  - tests/        # test-suite for `plymi_mod6` package (to be run using pytest)
      |-- conf.py # optional configuration file for pytest
      |-- test_basic_functions.py
      |-- test_numpy_functions.py
```

A reference implementation of this package can be found [in this GitHub repository](https://github.com/rsokl/plymi_mod6).
Populate the _basic_functions.py_ file with the two functions that we were using as our source code in the previous section: `count_vowels` and `merge_max_mappings`.
In in the _numpy_functions.py_ module, add the `pairwise_dists` function that appears in [Module 3's discussion of optimized pairwise distances](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/Broadcasting.html#Optimized-Pairwise-Distances).
Don't forget to include `import numpy as np` in your script in accordance with how `pairwise_dists` calls NumPy functions. 

We have arranged these functions so that they can be imported from the _basic_functions_ module and the _numpy_functions_ module, respectively, which reside in our `plymi_mod6` package.
Let's fill out our _setup.py_ script and install this package so that we can import it regardless of our current working directory. The content of _setup.py_ will be:

```python
from setuptools import find_packages, setup

setup(
    name="plymi_mod6",
    packages=find_packages(exclude=["tests", "tests.*"]),
    version="1.0.0",
    author="Your Name",
    author_email="your.email@email.com",
    description="A template Python package for learning about testing",
    install_requires=["numpy >= 1.10.0"],
    tests_require=["pytest", "hypothesis"],
    python_requires=">=3.6",
)
```

This setup file dictates that a user must have Python 3.6+ installed - we will bar Python 3.5 and below so that we are free to make use of [f-strings](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Formatting-strings) in our code, which were introduced in Python 3.6. Additionally, we will require pytest and hypothesis for running tests; the latter library will be introduced in a later section.

Finally, let's install our package locally [in development mode](https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Modules_and_Packages.html#Installing-Your-Own-Python-Package).
Navigate to the directory containing _setup.py_ and run:

```shell
python setup.py develop
```

Now, we should be able to start a python console, IPython console, or Jupyter notebook in any directory and import our package:

```python
# checking that we can import our `plymi_mod6` package
>>> from plymi_mod6.basic_functions import count_vowels
>>> count_vowels("Happy birthday", include_y=True)
5
```
<!-- #endregion -->

<!-- #region -->
## Populating Our Test Suite

pytest's system for "test discovery" is quite simple:
pytest need only be pointed to a directory with .py files in it, and it will find all of the functions in these files _whose names start with the word "test"_ and it will run all such functions.

Thus, let's populate the file _test_basic_functions.py_ with the functions `test_count_vowels_basic` and `test_merge_max_mappings`, which we wrote in the previous section of this module. 
E.g. our test 

```python
# we import the functions we are testing
from plymi_mod6.basic_functions import count_vowels, merge_max_mappings


def test_count_vowels_basic():
    # test basic strings with uppercase and lowercase letters
    assert count_vowels("aA bB yY", include_y=False) == 2
    assert count_vowels("aA bB yY", include_y=True) == 4

    # test empty strings
    assert count_vowels("", include_y=False) == 0
    assert count_vowels("", include_y=True) == 0


def test_merge_max_mappings():
    # test documented behavior
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 20, "c": -1}
    expected = {'a': 1, 'b': 20, 'c': -1}
    assert merge_max_mappings(dict1, dict2) == expected

    # test empty dict1
    dict1 = {}
    dict2 = {"a": 10.2, "f": -1.0}
    expected = dict2
    assert merge_max_mappings(dict1, dict2) == expected

    # test empty dict2
    dict1 = {"a": 10.2, "f": -1.0}
    dict2 = {}
    expected = dict1
    assert merge_max_mappings(dict1, dict2) == expected

    # test both empty
    dict1 = {}
    dict2 = {}
    expected = {}
    assert merge_max_mappings(dict1, dict2) == expected

```

As described before, `count_vowels` and `merge_max_mappings` must both be imported from our `plymi_mod6` package, so that our in the same namespace as our tests.
A reference implementation of _test_basic_functions.py_ can be viewed [here](https://github.com/rsokl/plymi_mod6/blob/master/tests/test_basic_functions.py).
Finally, add a dummy test - a test function that will always pass - to _test_basic_numpy.py_.
We will remove this later.

Without further ado, let's run our test suite! In our terminal, with the appropriate conda environment active, we navigate to the root directory of the project, which contains the `tests/` directory, and run `pytest tests/`.
Following output should appear:
<!-- #endregion -->

```
$ pytest tests/
============================= test session starts =============================
platform win32 -- Python 3.7.5, pytest-5.3.2, py-1.8.0, pluggy-0.12.0
rootdir: C:\Users\plymi_user\plymi_root_dir
collected 3 items                                                              

tests\test_basic_functions.py ..                                         [ 66%]
tests\test_basic_numpy.py .                                              [100%]

============================== 3 passed in 0.04s ==============================
```


This output indicates that three test-functions were found across two files and that all of the tests "passed"; i.e. the functions ran without raising any errors.
The first two tests are located in `tests/test_basic_functions.py`; the two dots indicate that two functions were run, and the `[66%]` indicator simply denotes that the test-suite is 66% (two-thirds) complete.
The proceeding reading comprehension problem will lead us to see what looks like for pytest to report a failing test.


<div class="alert alert-info"> 

**Reading Comprehension: Running a Test Suite**

Temporarily add a new "broken" test to `tests/test_basic_functions.py`.
The name that you give this test should adhere to pytest's simple rules for test-discovery.
Design the test function so that is sure to fail when it is run.

Rerun your test suite and compare its output to what you saw before - is it easy to identify which test failed and what caused it to fail?
Make sure to remove this function from your test suite once you are finished answering this question. 

</div>



We can also direct pytest to run the tests in a specific .py file. E.g. executing:

```shell
pytest tests/test_basic_functions.py
```

will cue pytest to only run the tests in _test_basic_functions.py_.

A key component to leveraging tests effectively is the ability to exercise ones tests repeatedly and rapidly with little manual overhead.
Clearly, pytest is instrumental towards this end - this framework made the process of organizing and running our test suite exceedingly simple!
That being said, there will certainly be occasions when we want to run a _specific_ test function.
Suppose, for instance, that we are writing a new function, and repeatedly want to run one of our tests that is pointing to a bug in our work-in-progress.
We can leverage pytest in conjunction with [an IDE](https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Getting_Started_With_IDEs_and_Notebooks.html) to run our tests in such incisive ways.


## Utilizing pytest within an IDE

Both [PyCharm and VSCode](https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Getting_Started_With_IDEs_and_Notebooks.html) can be configured to make keen use of pytest.
The following images show a couple of the enhancements afforded to us by PyCharm.
The IDEs will "discover" tests, and provide us with the ability to run individual tests.
For example, in the following image, the green "play button" allows us to run `test_count_vowels_basic`.

<!-- #raw raw_mimetype="text/html" -->
<div style="text-align: center">
<p>
<img src="../_images/individual_test.PNG" alt="Running an individual test in PyCharm" width="600">
</p>
</div>
<!-- #endraw -->

Furthermore, IDEs can provide a rich tree view of all the tests that are being run.
This is especially useful as our test suite grows to contain a considerable number of tests.
In the following image, we see that `test_version` is failing - we can click on the failing test in this tree-view, and our IDE will navigate us directly to the failing test. 

<!-- #raw raw_mimetype="text/html" -->
<div style="text-align: center">
<p>
<img src="../_images/test_tree_view.PNG" alt="Viewing an enchanced tree-view of your test suite" width="600">
</p>
</div>
<!-- #endraw -->

The first step for leveraging these features in your IDE is to enable the pytest framework in the IDE.
The following links point to detailed instructions for configuring pytest with PyCharm and VSCode, respectively:

- [Here for PyCharm](https://www.jetbrains.com/help/pycharm/pytest.html)
- [Here for VSCode](https://code.visualstudio.com/docs/python/testing)

These include advanced details, like running tests in parallel, which are beyond the scope of this material.


## Links to Official Documentation

- [pytest](https://docs.pytest.org/en/latest/)
- [Testing in PyCharm](https://www.jetbrains.com/help/pycharm/pytest.html)
- [Testing in VSCode](https://code.visualstudio.com/docs/python/testing)


## Reading Comprehension Solutions

<!-- #region -->
**Running a Test Suite: Solution**

> Let's add the test function `test_broken_function` to our test suite.
> We must include the word "test" in the function's name so that pytest will identify it as a test to run.
> There are limitless ways in which we can make this test fail; we'll introduce a trivial false-assertion:

```python
def test_broken_function():
    assert [1, 2, 3] == [1, 2]
```

> After introducing this broken test into _test_basic_functions.py_ , running our tests should result in the following output:

```
$ pytest tests/
============================= test session starts =============================
platform win32 -- Python 3.7.5, pytest-5.3.2, py-1.8.0, pluggy-0.12.0
rootdir: C:\Users\plymi_user\plymi_root_dir
collected 4 items                                                              

tests\test_basic_functions.py ..F                                        [ 75%]
tests\test_basic_numpy.py .                                              [100%]

================================== FAILURES ===================================
____________________________ test_broken_function _____________________________

    def test_broken_function():
>       assert [1, 2, 3] == [1, 2]
E       assert [1, 2, 3] == [1, 2]
E         Left contains one more item: 3
E         Use -v to get the full diff

tests\test_basic_functions.py:40: AssertionError
========================= 1 failed, 3 passed in 0.07s =========================
```

> Four tests were "discovered" and run by pytest. The pattern `..F` indicates that the first two tests in _test_basic_functions_ passed and the third test failed.
> It then indicates which test failed, and specifically that the assertion was false because a length-2 list cannot be equal to a length-3 list.
<!-- #endregion -->
