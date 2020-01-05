---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.0
  kernelspec:
    display_name: Python [conda env:.conda-jupy] *
    language: python
    name: conda-env-.conda-jupy-py
---

<!-- #raw raw_mimetype="text/restructuredtext" -->
.. meta::
   :description: Topic: Writing tests for your code, Difficulty: Easy, Category: Section
   :keywords: test, automated, pytest, parametrize, fixture, suite, decorator, clean directory  
<!-- #endraw -->

<!-- #region -->
# Describing Data with Hypothesis

It is often the case that the process of *describing our data* is by far the heaviest burden that we must bear when writing tests. This process of assessing "what variety of values should I test?", "have I thought of all the important edge-cases?", and "how much is 'enough'?" will crop up with nearly every test that we write.
Indeed, these are questions that you may have been asking yourself when writing `test_count_vowels_basic` and `test_merge_max_mappings` in the previous sections of this module.

[Hypothesis](https://hypothesis.readthedocs.io/) is a powerful Python library that empowers us to write a _description_ (specifications, to be more precise) of the data that we want to use to exercise our test.
It will then *generate* test cases that satisfy this description and will run our test on these cases.

Let's look at a simple example of Hypothesis in action.
In the preceding section, we learned to use pytest's parameterization mechanism to test properties of code over a set of values.
E.g. we wrote the following trivial test:

```python
import pytest

# A simple parameterized test that only tests a few, conservative inputs.
# Note that this test must be run by pytest to work properly
@pytest.mark.parametrize("size", [0, 1, 2, 3])
def test_range_length(size):
    assert len(range(size)) == size
```

which tests the property that `range(n)` has a length of `n` for any non-negative integer value of `n`.
Well, it isn't *really* testing this property for all non-negative integers; clearly it is only testing the values 0-3.
We should probably also check much larger numbers and perhaps traverse various orders of magnitude (i.e. factors of ten) in our parameterization scheme.
No matter what set of values we land on, it seems like we will have to eventually throw are hands up and say "okay, that seems good enough".

Instead of manually specifying the data to pass to `test_range_length`, let's use Hypothesis to simply describe the data:
<!-- #endregion -->

<!-- #region -->
```python
from hypothesis import given

# Hypothesis provides so-called "strategies" for us
# to describe our data
import hypothesis.strategies as st

# Using hypothesis to test any integer value in [0, 10 ^ 10]
@given(size=st.integers(min_value=0, max_value=1E10))
def test_range_length(size):
    assert len(range(size)) == size
```
<!-- #endregion -->

<!-- #region -->
```python
# Running this test once will trigger Hypothesis to
# generate 100 values based on the description of our data,
# and it will execute the test using each one of those values
>>> test_range_length()
```
<!-- #endregion -->

Here we have specified that the `size` value in our test should take on any integer value within $[0, 10^{10}]$.
We did this by using the `integers` "strategy" that is provided by Hypothesi: `st.integers(min_value=0, max_value=1E10)`.
When we execute the resulting test (which simply be run within a Jupyter cell or via pytest), this will trigger Hypothesis to generate test cases based on this specification;
by default it will generate 100 test cases - an amount that we can configure - and will evaluate our test for each one of them.

With great ease, we were able to replace our pytest-parameterized test, which only very sparsely tested the property at hand, with a much more robust, hypothesis-driven test.
This will be a recurring trend - we will generally produce much more robust tests by _describing_ our data with Hypothesis, rather than manually specifying test values.

<!-- #region -->
<div class="alert alert-warning">

**Hypothesis is very effective...**: 

You may be wondering why, in the preceding example, we arbitrarily picked $10^{10}$ as the upper bound to the integer-values to feed to our test.
I actually didn't write the test that way initially.
Instead, I wrote the more general test:

```python
@given(size=st.integers(min_value=0))
def test_range_length(size):
    assert len(range(size)) == size
```

which places no formal upper bound on the integers that Hypothesis will generate.
But... this found a bug:

```python
Falsifying example: test_range_length(
    size=9223372036854775808,
)

----> 3     assert len(range(size)) == size

OverflowError: Python int too large to convert to C ssize_t
```

</div>
<!-- #endregion -->

```python
@given(size=st.integers(min_value=0))
def test_range_length(size):
    assert len(range(size)) == size
```

```python
test_range_length()
```

## Links to Official Documentation

- [Hypothesis](https://hypothesis.readthedocs.io/)


## Reading Comprehension Solutions



