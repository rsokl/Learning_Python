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

# Introducing the Pytest Framework

Thus far, the process of running tests is a entirely manual one. It is time for us to arranging our test functions into a proper "test suite" and to learn to leverage [the pytest framework](https://docs.pytest.org/en/latest/) to run them.
We will begin by reorganizing our source code to create an installable [package](https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Modules_and_Packages.html#Packages).
We will then learn how to structure and run a test suite for this Python package, using pytest.

The pytest framework does much more than just run tests;
for instance, it will enrich the assertions in our tests to produce verbose, informative error messages.
Furthermore it provides valuable means for enhancing our tests via mechanisms like fixtures and parameterizing decorators.
Ultimately, all of this functionality helps to eliminate manual aspects from the testing process. 


## Organizing a Test Suite

It's time to create a proper test suite.
Before proceeding any further, we should reread the material presented in [Module 5 - Import: Modules and Packages](https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Modules_and_Packages.html) and recall the essentials of import statements, modules, and Python packages.
This material serves as the foundation for this section.

Let's create the a Python package, which we will call `plymi_mod6`, with the following directory structure:

```
- setup.py     # script responsible for installing `plymi_mod6` package
- plymi_mod6/  # directory containing source code of `plymi_mod6` package
    |-- __init__.py
    |-- basic_functions.py
    |-- numpy_functions.py
- tests/            # test-suite for `plymi_mod6` package (to be run using pytest)
    |-- conf.py     # optional configuration file for pytest
    |-- test_basic_functions.py
    |-- test_numpy_functions.py
```

A reference implementation of this package can be found [in this GitHub repository](https://github.com/rsokl/plymi_mod6).


## Links to Official Documentation

- [pytest](https://docs.pytest.org/en/latest/)


## Reading Comprehension Solutions
