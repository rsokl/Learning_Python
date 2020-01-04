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
   :keywords: test, automated, pytest, parametrize, fixture, suite, decorator, clean directory  
<!-- #endraw -->

# The pytest Framework

Thus far, our process for running tests has been an entirely manual one. It is time for us to arrange our test functions into a proper "test suite" and to learn to leverage [the pytest framework](https://docs.pytest.org/en/latest/) to run them.
We will begin by reorganizing our source code to create an installable [Python package](https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Modules_and_Packages.html#Packages).
We will then learn how to structure and run a test suite for this Python package, using pytest.

The pytest framework does much more than just run tests;
for instance, it will enrich the assertions in our tests to produce verbose, informative error messages.
Furthermore it provides valuable means for enhancing our tests via mechanisms like fixtures and parameterizing decorators.
Ultimately, all of this functionality helps to eliminate manual and redundant aspects of the testing process.



<div class="alert alert-warning"> 

**Note**

It can be useful to [create a separate conda environment](https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Installing_Python.html#A-Brief-Introduction-to-Conda-Environments) for the sake of this lesson, so that we can work through this material starting from a blank slate.
If you do create a new conda environment, be sure to activate that environment and install NumPy and Jupyter notebook: `conda install numpy notebook` 
</div>



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
While [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) provides extremely valuable functionality for advanced testing, all of its functionality can be leveraged while using pytest as your testing framework. 
    
`nose`, which simply extends the functionality of `unittest`, **is no longer being maintained**.
There is a project, "Nose2", which is carrying the torch of `nose`. However, this is a fledgling project by comparison to `pytest`.
As of writing this, `pytest` was downloaded 12 million times last month versus `nose2`'s 150 thousand downloads.
    
The takeaway here is that, when it comes to picking a testing framework for Python, `pytest` is the clear choice.
Any discussion that you come across to the contrary is likely outdated.
</div>

<!-- #region -->
## Creating a Python Package with Tests

It's time to create a proper test suite.
Before proceeding any further, we should reread the material presented in [Module 5 - Import: Modules and Packages](https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Modules_and_Packages.html) and recall the essentials of import statements, modules, and Python packages.
This material serves as the foundation for this section.

### Organizing our Source Code
Let's create a Python package, which we will call `plymi_mod6`, with the following directory structure:

```
project_dir/     # the "parent directory" houses our source code, tests, and all other relevant files
  - setup.py     # script responsible for installing `plymi_mod6` package
  - plymi_mod6/  # directory containing source code of `plymi_mod6` package
      |-- __init__.py
      |-- basic_functions.py
      |-- numpy_functions.py
  - tests/        # test-suite for `plymi_mod6` package (to be run using pytest)
      |-- conftest.py # optional configuration file for pytest
      |-- test_basic_functions.py
      |-- test_numpy_functions.py
```

A reference implementation of this package can be found [in this GitHub repository](https://github.com/rsokl/plymi_mod6).
Populate the `basic_functions.py` file with the two functions that we were using as our source code in the previous section: `count_vowels` and `merge_max_mappings`.
In the `numpy_functions.py` module, add the `pairwise_dists` function that appears in [Module 3's discussion of optimized pairwise distances](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/Broadcasting.html#Optimized-Pairwise-Distances).
Don't forget to include `import numpy as np` in your script in accordance with how `pairwise_dists` calls NumPy functions. 

We have arranged these functions so that they can be imported from the `basic_functions` module and the `numpy_functions` module, respectively, which reside in our `plymi_mod6` package.
Let's fill out our `setup.py` script and install this package so that we can import it regardless of our current working directory. The content of `setup.py` will be:

```python
from setuptools import find_packages, setup

setup(
    name="plymi_mod6",
    packages=find_packages(exclude=["tests", "tests.*"]),
    version="1.0.0",
    author="Your Name",
    description="A template Python package for learning about testing",
    install_requires=["numpy >= 1.10.0"],
    tests_require=["pytest", "hypothesis"],
    python_requires=">=3.6",
)
```

This setup file dictates that a user must have Python 3.6+ installed - we will bar Python 3.5 and below so that we are free to make use of [f-strings](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Formatting-strings) in our code, which were introduced in Python 3.6. Additionally, we will require pytest and hypothesis for running tests; the Hypothesis library will be introduced in a later section.

Finally, let's install our package locally [in development mode](https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Modules_and_Packages.html#Installing-Your-Own-Python-Package).
Navigate to the directory containing `setup.py` and run:

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
## Populating and Running Our Test Suite

pytest's [system for "test discovery"](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery) is quite simple:
pytest need only be pointed to a directory with files named `test_*.py` in it, and it will find all of the functions in these files _whose names start with the word "test"_ and will run all such functions.

Thus, let's populate the file ``test_basic_functions.py`` with the functions `test_count_vowels_basic` and `test_merge_max_mappings`, which we wrote in the previous section of this module:

```python
# The contents of test_basic_functions.py

# we must import the functions we are testing
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

As described before, `count_vowels` and `merge_max_mappings` must both be imported from our `plymi_mod6` package, so that our functions are in the same namespace as our tests.
A reference implementation of `test_basic_functions.py` can be viewed [here](https://github.com/rsokl/plymi_mod6/blob/master/tests/test_basic_functions.py).
Finally, add a dummy test - a test function that will always pass - to `test_basic_numpy.py`.
We will replace this with a useful test later.

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
The following reading comprehension problem will lead us to see what looks like for pytest to report a failing test.


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

will cue pytest to only run the tests in `test_basic_functions.py`.

A key component to leveraging tests effectively is the ability to exercise ones tests repeatedly and rapidly with little manual overhead.
Clearly, pytest is instrumental towards this end - this framework made the process of organizing and running our test suite exceedingly simple!
That being said, there will certainly be occasions when we want to run a _specific_ test function.
Suppose, for instance, that we are writing a new function, and repeatedly want to run one of our tests that is pointing to a bug in our work-in-progress.
We can leverage pytest in conjunction with [an IDE](https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Getting_Started_With_IDEs_and_Notebooks.html) to run our tests in such incisive ways.


### Utilizing pytest within an IDE

Both [PyCharm and VSCode](https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Getting_Started_With_IDEs_and_Notebooks.html) can be configured to make keen use of pytest.
The following images show a couple of the enhancements afforded to us by PyCharm; comparable features are available in VSCode.
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

- [Running tests in PyCharm](https://www.jetbrains.com/help/pycharm/pytest.html)
- [Running tests in VSCode](https://code.visualstudio.com/docs/python/testing)

These linked materials also include advanced details, like instructions for running tests in parallel, which are beyond the scope of this material but are useful nonetheless.


## Enhanced Testing with pytest

In addition to providing us with a simple means for organizing and running our test suite, pytest has powerful features that will both simplify and enhance our tests.
We will now leverage these features in our test suite.

<!-- #region -->
### Enriched Assertions

A failing "bare" assertion - an `assert` statement without an error message - can be a frustrating thing.
Suppose, for instance, that one of our test-assertions about `count_vowels` fails:

```python
# a failing assertion without an error message is not informative

assert count_vowels("aA bB yY", include_y=True) == 4
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-2-f89f8b6a7213> in <module>
----> 1 assert count_vowels("aA bB yY", include_y=True) == 4

AssertionError: 
```

The problem with this bare assertion is that we don't know what `count_vowels("aA bB yY", include_y=True)` actually returned!
We now have to go through the trouble of starting a python console, importing this function, and calling it with this specific input in order to see what our function was actually returning. An obvious remedy to this is for us to write our own error message, but this too is quite cumbersome when we consider the large number of assertions that we are destined to write.

Fortunately, pytest comes to the rescue: it will "hijack" any failing bare assertion and will _insert a useful error message for us_.
This is known as ["assertion introspection"](https://docs.pytest.org/en/latest/assert.html#assertion-introspection-details).
For example, if the aforementioned assertion failed when being run by pytest, we would see the following output:

```python
# pytest will write informative error messages for us

assert count_vowels("aA bB yY", include_y=True) == 4
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
~\Learning_Python\Python\Module6_Testing\Untitled1.ipynb in <module>
----> 1 assert count_vowels("aA bB yY", include_y=True) == 4

AssertionError: assert 2 == 4
 +  where 2 = <function count_vowels at 0x000001B91B913708>('aA bB yY', include_y=True
```

See that the error message that pytest included for us indicates that `count_vowels("aA bB yY", include_y=True)` returned `2`, when we expected it to return `4`.
From this we might suspect that `count_vowels` is not counting y's correctly.

Here are some more examples of "enriched assertions", as provided by pytest.
See that these error messages even provide useful "diffs", which specify specifically _how_ two similar objects differ, where possible.

```python
# comparing unequal lists
assert [1, 2, 3] == [1, 2]
E         Left contains one more item: 3
E         Full diff:
E         - [1, 2, 3]
E         ?      ---
E         + [1, 2]
```

```python
# comparing unequal dictionaries
assert {"a": 1, "b": 2} == {"a": 1, "b": 3}
E       AssertionError: assert {'a': 1, 'b': 2} == {'a': 1, 'b': 3}
E         Omitting 1 identical items, use -vv to show
E         Differing items:
E         {'b': 2} != {'b': 3}
E         Full diff:
E         - {'a': 1, 'b': 2}
E         ?               ^
E         + {'a': 1, 'b': 3}...
```

```python
# comparing unequal strings
assert "moo" == "moon"
E       AssertionError: assert 'moo' == 'moon'
E         - moo
E         + moon
E         ?    +
```

<!-- #endregion -->

<!-- #region -->
### Parameterized Tests

Looking back to both `test_count_vowels_basic` and `test_merge_max_mappings`, we see that there is a lot of redundancy within the bodies of these test functions.
The assertions that we make within a given test-function share identical forms - they differ only in the parameters that we feed into our functions and their expected output.
Another shortcoming of this test-structure is that a failing assertion will block subsequent assertions from being evaluated.
That is, if the second assertion in a `test_count_vowels_basic` fails, the third and fourth assertions will not be evaluated in that run.
This precludes us from potentially seeing useful patterns among the failing assertions.

pytest provides a useful tool that will allow us to eliminate these structural shortcomings by transforming our test-functions into so-called _parameterized tests_. Let's parametrize the following test:

```python
# a simple test with redundant assertions

def test_range_length_unparameterized():
    assert len(range(0)) == 0
    assert len(range(1)) == 1
    assert len(range(2)) == 2
    assert len(range(3)) == 3
```

This test is checking the property `len(range(n)) == n`, where `n` is any non-negative integer.
Thus the parameter to be varied here is the "size" of the range-object being created.
Let's treat it as such by using pytest to write a parameterized test:

```python
# parameterizing a test
import pytest

# note that this test must be run by pytest to work properly
@pytest.mark.parametrize("size", [0, 1, 2, 3])
def test_range_length(size):
    assert len(range(size)) == size
```

Make note that a pytest-parameterized test must be run using pytest; an error will raise if we manually call `test_range_length()`.
When executed, pytest will treat this parameterized test as _four separate tests_ - one for each parameter value:

```
test_basic_functions.py::test_range_length[0] PASSED                     [ 25%]
test_basic_functions.py::test_range_length[1] PASSED                     [ 50%]
test_basic_functions.py::test_range_length[2] PASSED                     [ 75%]
test_basic_functions.py::test_range_length[3] PASSED                     [100%]
```

See that we have successfully eliminated the redundancy from `test_range_length`;
the body of the function now contains only a single assertion, making obvious the property that is being tested.
Furthermore, the four assertions are now being run independently from one another and thus we can potentially see patterns across multiple fail cases in concert.
<!-- #endregion -->

<!-- #region -->
#### Decorators

The the syntax used to parameterize this test may look alien to us, we have yet to encounter this construct thus far.
`pytest.mark.parameterize(...)` is a _decorator_ - an object that is used to "wrap" a function in order to transform its behavior.
The `pytest.mark.parameterize(...)` decorator wraps our test function so that pytest can call it multiple times, once for each parameter value. 
The `@` character, in this context, denotes the application of a decorator:

```python
# general syntax for applying a decorator to a function

@the_decorator
def the_function_being_decorated(<arguments_for_function>):
    pass
```

For an in-depth discussion of decorators, please refer to [Real Python's Primer on decorators](https://realpython.com/primer-on-python-decorators/#simple-decorators).
<!-- #endregion -->

<!-- #region -->
#### Parameterization Syntax

The general form for creating a parameterizing decorator with *a single parameter*, as we formed above, is:

```python
@pytest.mark.parametrize("<param-name>", [<val-1>, <val-2>, ...])
def test_function(<param-name>):
    ...
```

We will often have tests that require multiple parameters.
The general form for creating the parameterization decorator for $N$ parameters,
each of which assume $J$ values, is:

```python
@pytest.mark.parametrize("<param-name1>, <param-name2>, [...], <param-nameN>", 
                         [(<param1-val1>, <param2-val1>, [...], <paramN-val1>),
                          (<param1-val2>, <param2-val2>, [...], <paramN-val2>),
                          ...
                          (<param1-valJ>, <param2-valJ>, [...], <paramN-valJ>),
                         ])
def test_function(<param-name1>, <param-name2>, [...], <param-nameN>):
    ...
```

For example, let's take the following trivial test:

```python
def test_inequality_unparameterized():
    assert 1 < 2 < 3
    assert 4 < 5 < 6
    assert 7 < 8 < 9
    assert 10 < 11 < 12
```

and rewrite it in parameterized form. 
The decorator will have three distinct parameter, and each parameters, let's simply call them `a`, `b`, and `c`, will take on four values.

```python
# the parameterized form of `test_inequality_unparameterized`
@pytest.mark.parametrize("a, b, c", [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])
def test_inequality(a, b, c):
    assert a < b < c
```
<!-- #endregion -->

<div class="alert alert-warning"> 

**Note**

The formatting for multi-parameter tests can quickly become unwieldy.
It isn't always obvious where one should introduce line breaks and indentations to improve readability.
This is a place where the ["black" auto-formatter](https://black.readthedocs.io/en/stable/) really shines!
Black will make all of these formatting decisions for us - we can write our parameterized tests as haphazardly as we like and simply run black to format our code.
</div>



<div class="alert alert-info"> 

**Reading Comprehension: Parameterizing Tests**

Rewrite `test_count_vowels_basic` as a parameterized test with the parameters: `input_string`, `include_y`, and `expected_count`.

Rewrite `test_merge_max_mappings` as a parameterized test with the parameters: `dict_a`, `dict_b`, and `expected_merged`.

Before rerunning `test_basic_functions.py` predict how many distinct test cases will be reported by pytest. 

</div>


<!-- #region -->
Finally, you can apply multiple parameterizing decorators to a test so that pytest will run _all combinations of the respective parameter values_.

```python
# testing all combinations of `x` and `y`
@pytest.mark.parametrize("x", [0, 1, 2])
@pytest.mark.parametrize("y", [10, 20])
def test_all_combinations(x, y):
    # will run:
    # x=0 y=10
    # x=0 y=20
    # x=1 y=10
    # x=1 y=20
    # x=2 y=10
    # x=2 y=20
    pass
```
<!-- #endregion -->

### Fixtures

The final major pytest feature that we will discuss are "fixtures".
A fixture, roughly speaking, is a means by which we can share information and functionality across our tests.
Fixtures can be defined within our `conftest.py` file, and pytest will automatically "discover" them and make them available for use throughout our test suite in a convenient way.

Exploring fixtures will quickly take us beyond our depths for the purposes of this introductory material, so we will only scratch the surface here.
We can read about advanced details of fixtures [here](https://docs.pytest.org/en/latest/fixture.html#fixture).

Below are examples of two useful fixtures.

<!-- #region -->
```python
# contents of conftest.py

import os
import tempfile

import pytest

@pytest.fixture()
def cleandir():
    """ This fixture will use the stdlib `tempfile` module to
    change the current working directory to a tmp-dir for the
    duration of the test.
    
    Afterwards, the test session returns to its previous working
    directory, and the temporary directory and its contents
    will be automatically deleted.
    
    Yields
    ------
    str
        The name of the temporary directory."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        old_dir = os.getcwd()
        os.chdir(tmpdirname)
        yield tmpdirname
        os.chdir(old_dir)


@pytest.fixture()
def dummy_email():
    """ This fixture will simply have pytest pass the string:
                   'dummy.email@plymi.com'
    to any test-function that has the parameter name `dummy_email` in
    its signature.
    """
    return "dummy.email@plymi.com"
```
<!-- #endregion -->

<!-- #region -->
The first one, `cleandir`, can be used in conjunction with tests that need to write files.
We don't want our tests to leave behind files on our machines; the `cleandir` fixture will ensure that our tests will write files to a temporary directory that will be deleted once the test is complete.

Second is a simple fixture called `dummy_email`.
Suppose that our project needs to interact with a specific email address, suppose it's `dummy.email@plymi.com`, and that we have several tests that need access to this address.
This fixture will pass this address to any test function that has the parameter name `dummy_email` in its signature.

A reference implementation of `conftest.py` in our project can be found [here](https://github.com/rsokl/plymi_mod6/blob/fixtures/tests/conftest.py).
Several reference tests that make use of these fixtures can be found [here](https://github.com/rsokl/plymi_mod6/blob/fixtures/tests/test_using_fixtures.py).

Let's create a file `tests/test_using_fixtures.py`, and write some tests that put these fixtures to use:

```python
# contents of test_using_fixtures.py
import pytest

# When run, this test will be executed within a
# temporary directory that will automatically be
# deleted - along with all of its contents - once
# the test ends.
#
# Thus we can have this test write a file, and we
# need not worry about having it clean up after itself.
@pytest.mark.usefixtures("cleandir")
def test_writing_a_file():
    with open("a_text_file.txt", mode="w") as f:
        f.write("hello world")

    with open("a_text_file.txt", mode="r") as f:
        file_content = f.read()

    assert file_content == "hello world"


# We can use the `dummy_email` fixture to provide
# the same email address to many tests. In this
# way, if we need to change the email address, we
# can simply update the fixture and all of the tests
# will be affected by the update.
#
# Note that we don't need to use a decorator here.
# pytest is smart, and will see that the parameter-name
# `dummy_email` matches the name of our fixture. It will
# thus call these tests using the value returned by our
# fixture

def test_email1(dummy_email):
    assert "dummy" in dummy_email


def test_email2(dummy_email):
    assert "plymi" in dummy_email


def test_email3(dummy_email):
    assert ".com" in dummy_email
```
<!-- #endregion -->

## Links to Official Documentation

- [pytest](https://docs.pytest.org/en/latest/)
- [pytest's system for test discovery](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)
- [Testing in PyCharm](https://www.jetbrains.com/help/pycharm/pytest.html)
- [Testing in VSCode](https://code.visualstudio.com/docs/python/testing)
- [Assertion introspection](https://docs.pytest.org/en/latest/assert.html#assertion-introspection-details)
- [Parameterizing tests](https://docs.pytest.org/en/latest/parametrize.html)
- [Fixtures](https://docs.pytest.org/en/latest/fixture.html#fixture)


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

> After introducing this broken test into `test_basic_functions.py` , running our tests should result in the following output:

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

<!-- #region -->
**Parameterizing Tests: Solution**

A reference implementation for this solution within the `plymi_mod6` project can be found [here](https://github.com/rsokl/plymi_mod6/blob/parameterized/tests/test_basic_functions.py).

The contents of `test_basic_functions.py`, rewritten to use pytest-parameterized tests:

```python
import pytest
from plymi_mod6.basic_functions import count_vowels, merge_max_mappings


@pytest.mark.parametrize(
    "input_string, include_y, expected_count",
    [("aA bB yY", False, 2), ("aA bB yY", True, 4), ("", False, 0), ("", True, 0)],
)
def test_count_vowels_basic(input_string, include_y, expected_count):
    assert count_vowels(input_string, include_y) == expected_count


@pytest.mark.parametrize(
    "dict_a, dict_b, expected_merged",
    [
        (dict(a=1, b=2), dict(b=20, c=-1), dict(a=1, b=20, c=-1)),
        (dict(), dict(b=20, c=-1), dict(b=20, c=-1)),
        (dict(a=1, b=2), dict(), dict(a=1, b=2)),
        (dict(), dict(), dict()),
    ],
)
def test_merge_max_mappings(dict_a, dict_b, expected_merged):
    assert merge_max_mappings(dict_a, dict_b) == expected_merged
```

Running these tests via pytest should produce eight distinct test-case: four for `test_count_vowels_basic` and four for `test_merge_max_mappings`.

```
============================= test session starts =============================
platform win32 -- Python 3.7.5, pytest-5.3.2, py-1.8.0, pluggy-0.12.0
cachedir: .pytest_cache
rootdir: C:\Users\plymi_user\Learning_Python\plymi_mod6_src
collecting ... collected 8 items

test_basic_functions.py::test_count_vowels_basic[aA bB yY-False-2] PASSED [ 12%]
test_basic_functions.py::test_count_vowels_basic[aA bB yY-True-4] PASSED [ 25%]
test_basic_functions.py::test_count_vowels_basic[-False-0] PASSED        [ 37%]
test_basic_functions.py::test_count_vowels_basic[-True-0] PASSED         [ 50%]
test_basic_functions.py::test_merge_max_mappings[dict_a0-dict_b0-expected_merged0] PASSED [ 62%]
test_basic_functions.py::test_merge_max_mappings[dict_a1-dict_b1-expected_merged1] PASSED [ 75%]
test_basic_functions.py::test_merge_max_mappings[dict_a2-dict_b2-expected_merged2] PASSED [ 87%]
test_basic_functions.py::test_merge_max_mappings[dict_a3-dict_b3-expected_merged3] PASSED [100%]

============================== 8 passed in 0.07s ==============================
```

<!-- #endregion -->
