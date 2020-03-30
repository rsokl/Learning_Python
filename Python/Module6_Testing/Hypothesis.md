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
# Introduction to Testing with Hypothesis

It is often the case that the process of *describing our data* is by far the heaviest burden that we must bear when writing tests. This process of assessing "what variety of values should I test?", "have I thought of all the important edge-cases?", and "how much is 'enough'?" will crop up with nearly every test that we write.
Indeed, these are questions that you may have been asking yourself when writing `test_count_vowels_basic` and `test_merge_max_mappings` in the previous sections of this module.

[Hypothesis](https://hypothesis.readthedocs.io/) is a powerful Python library that empowers us to write a _description_ (specification, to be more precise) of the data that we want to use to exercise our test.
It will then *generate* test cases that satisfy this description and will run our test on these cases.
Ultimately, this an extremely powerful tool for enabling us to write high-quality automated tests for our code.

Hypothesis can be installed via conda:

```shell
conda install hypothesis
```

or pip:

```shell
pip install hypothesis
```


## A Simple Example Using Hypothesis

Let's look at a simple example of Hypothesis in action.
In the preceding section, we learned to use pytest's parameterization mechanism to test properties of code over a set of values.
For example, we wrote the following trivial test:

```python
import pytest

# A simple parameterized test that only tests a few, conservative inputs.
# Note that this test must be run by pytest to work properly
@pytest.mark.parametrize("size", [0, 1, 2, 3])
def test_range_length(size):
    assert len(range(size)) == size
```

which tests the property that `range(n)` has a length of `n` for any non-negative integer value of `n`.
Well, it isn't *really* testing this property for all non-negative integers; clearly it is only testing the values 0-3, as indicated by the `parametrize` decorator.
We should probably also check much larger numbers and perhaps traverse various orders of magnitude (i.e. factors of ten) in our parameterization scheme.
No matter what set of values we land on, it seems like we will have to eventually throw our hands up and say "okay, that seems good enough."

Instead of manually specifying the data to pass to `test_range_length`, let's use Hypothesis to simply describe the data:
<!-- #endregion -->

<!-- #region -->
```python
# A basic introduction to Hypothesis

from hypothesis import given

# Hypothesis provides so-called "strategies" for us
# to describe our data
import hypothesis.strategies as st

# Using hypothesis to test any integer value in [0, 10 ** 10]
@given(size=st.integers(min_value=0, max_value=1E10))
def test_range_length(size):
    assert len(range(size)) == size
```
<!-- #endregion -->

<!-- #region -->
Here we have specified that the value of `size` in our test *should be able to take on any integer value within* $[0, 10^{10}]$.
We did this by using the `integers` "strategy" that is provided by Hypothesis: `st.integers(min_value=0, max_value=1E10)`.
When we execute the resulting test (which can simply be run within a Jupyter cell or via pytest), this will trigger Hypothesis to generate test cases based on this specification;
by default, Hypothesis will generate 100 test cases - an amount that we can configure - and will execute our test function for each one of them.

```python
# Running this test once will trigger Hypothesis to
# generate 100 values based on the description of our data,
# and it will execute the test using each one of those values
>>> test_range_length()
```

With great ease, we were able to replace our pytest-parameterized test, which only very narrowly tested the property at hand, with a much more robust, Hypothesis-driven test.
This will be a recurring trend: we will generally produce much more robust tests by _describing_ our data with Hypothesis, rather than manually specifying test values.

The rest of this section will be dedicated to learning about the Hypothesis library and how we can leverage it to write powerful tests.
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-warning">

**Hypothesis is _very_ effective...**: 

You may be wondering why, in the preceding example, I arbitrarily picked $10^{10}$ as the upper bound to the integer-values to feed to the test.
Initially, I didn't write the test that way.
Instead, I wrote the more general test:

```python
# `size` can be any non-negative integer
@given(size=st.integers(min_value=0))
def test_range_length(size):
    assert len(range(size)) == size
```

which places no formal upper bound on the integers that Hypothesis will generate.
However, this test immediately found an issue (I hesitate to call it an outright bug):

```python
Falsifying example: test_range_length(
    size=9223372036854775808,
)

----> 3     assert len(range(size)) == size

OverflowError: Python int too large to convert to C ssize_t
```

This reveals that the CPython implementation of the built-in `len` function is such that it can only handle non-negative integers smaller than $2^{63}$ (i.e. it will only allocate 64 bits to represent a signed integer - one bit is used to store the sign of the number).
Hypothesis revealed this by generating the failing test case `size=9223372036854775808`, which is exactly $2^{63}$.
I did not want this error to distract from what is otherwise merely a simple example, but it is very important to point out.

Hypothesis has a knack for catching these sorts of unexpected edge cases.
Now we know that `len(range(size)) == size` _does not_ hold for "arbitrary" non-negative integers!
(This overflow behavior is now documented in the [CPython source code](https://github.com/python/cpython) because it was discovered while writing this material 😄).


</div>
<!-- #endregion -->

<!-- #region -->
## The `given` Decorator

Hypothesis' [given decorator](https://hypothesis.readthedocs.io/en/latest/details.html#the-gory-details-of-given-parameters) is responsible for:

 - drawing values from Hypothesis' so-called "strategies" for describing input data for our test function
 - running the test function many times (up to 100 times, by default) given different input values drawn from the strategy
 - "shrinking" the drawn inputs to identify simple fail cases: if an error is raised by the test function during one of the many executions, the `given` decorator will attempt to "shrink" (i.e. simplify) the inputs that produce that same error before reporting them to the user
 - reporting the input values that caused the test function to raise an error


Let's see the `given` decorator in action by writing a simple "test" for which `x` should be integers between 0 and 10, and `y` should be integers between 20 and 30.
To do this we will make use of the `integers` Hypothesis strategy.
Let's include a bad assertion statement – that `y` can't be larger than 25 – to see how Hypothesis reports this fail case.
Note that we aren't really testing any code here, we are simply exercising some of the tools that Hypothesis provides us with.

```python
from hypothesis import given 
import hypothesis.strategies as st

# using `given` with multiple parameters
# `x` is an integer drawn from [0, 10]
# `y` is an integer drawn from [20, 30]
@given(x=st.integers(0, 10), y=st.integers(20, 30))
def test_demonstrating_the_given_decorator(x, y):
    assert 0 <= x <= 10
    
    # `y` can be any value in [20, 30]
    # this is a bad assertion: it should fail!
    assert 20 <= y <= 25
```

See that the names of the parameters specified in `given` — `x` and `y` in this instance — must match those in the signature of the test function.

To run this test function, we simply call `test_demonstrating_the_given_decorator()`.
Note that, unlike with a typical function, we do not pass values for `x` and `y` to this function – *the* `given` *decorator will pass these values to the function for us*.
Executing this `given`-decorated function will prompt Hypothesis to draw 100 pairs of values for `x` and `y`, according to their respective strategies, and the body of the test will be executed for each such pair.

```python
# running the test
>>> test_demonstrating_the_given_decorator()
Falsifying example: test_demonstrating_the_given_decorator(
    x=0, y=26,
)
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-29-ea20353bbef5> in test_demonstrating_the_given_decorator(x, y)
     10     # `y` can be any value in [20, 30]
     11     # this is a bad assertion: it should fail!
---> 12     assert 20 <= y <= 25

AssertionError: 

```

(Note: some of the "Traceback" error message has been removed to improve legibility)

See that the error message here indicates that Hypothesis identified a "falsifying example", or a set of input values, `x=0` and `y=26`, which caused our test function to raise an error. The proceeding "Traceback" message indicates that it is indeed the second assertion statement that is responsible for raising the error.

### Shrinking: Simplifying Falsifying Inputs

The `given` decorator strives to report the "simplest" set of input values that produce a given error.
It does this through the process of "shrinking".
Each of Hypothesis' strategies has its own prescribed shrinking behavior.
For the `integers` strategy, this means identifying the integer closest to 0 that produces the error at hand.
For instance, `x=12` and `y=29` may have been the first drawn values to trigger the assertion error.
These values were then incrementally reduced by the `given` decorator until `x=0` and `y=26` were identified as the smallest set of values to reproduce this fail case.

We can print out the examples that Hypothesis generated:

```
x=0   y=20 - PASSED
x=0   y=20 - PASSED
x=0   y=20 - PASSED
x=9   y=20 - PASSED
x=9   y=21 - PASSED
x=3   y=20 - PASSED
x=3   y=20 - PASSED
x=9   y=26 - FAILED
x=3   y=26 - FAILED
x=6   y=26 - FAILED
x=10  y=27 - FAILED
x=7   y=27 - FAILED
x=3   y=30 - FAILED
x=3   y=23 - PASSED
x=10  y=30 - FAILED
x=3   y=27 - FAILED
x=3   y=27 - FAILED
x=2   y=27 - FAILED
x=0   y=27 - FAILED
x=0   y=26 - FAILED
x=0   y=21 - PASSED
x=0   y=25 - PASSED
x=0   y=22 - PASSED
x=0   y=23 - PASSED
x=0   y=24 - PASSED
x=0   y=26 - FAILED
```

See that Hypothesis has to do a semi-random search to identify the boundaries of the fail case; it doesn't know if `x` is causing the error, or if `y` is the culprit, or if it is specific *combinations* of `x` and `y` that causes the failure!
Despite this complexity, the pairs of variables are successfully shrunk to the simplest fail case.
<!-- #endregion -->

<div class="alert alert-warning">

**Hypothesis will Save Falsifying Examples**: 

Albeit an advanced detail, it is important to note that Hypothesis does not have to search for falsifying examples from scratch every time we run a test function.
Instead, Hypothesis will save a database of falsifying examples associated with each of your project's test functions.
The database is saved under `.hypothesis` in whatever directory your test functions were run from.

This ensures that, once Hypothesis finds a falsifying example for a test, the falsifying example will be passed to your test function each time you run it, until it no longer raises an error in your code (e.g. you update your code to fix the bug that was causing the test failure). 
</div>


<div class="alert alert-info"> 

**Reading Comprehension: Understanding How Hypothesis Works**

Define the `test_demonstrating_the_given_decorator` function as above, complete with the failing assertion, and add a print statement to the body of the function, which prints out the value for `x` and `y`.

Run the test once and make note of the output that is printed. Consider copying and pasting the output to a notepad for reference. Next, rerun the test multiple times and make careful note of the printed output. What do you see? Is the output different from the first run? Does it differ between subsequent runs? Try to explain this behavior.

In your file browser, navigate to the directory from which you are running this test; if you are following along in a Jupyter notebook, this is simply the directory containing said notebook. You should see a `.hypothesis` directory. As noted above, this is the database that contains the falsifying examples that Hypothesis has identified. Delete the `.hypothesis` directory and try re-running your test? What do you notice about the output now? You should also see that the `.hypothesis` directory has reappeared. Explain what is going on here.

</div>



<div class="alert alert-info"> 

**Reading Comprehension: Fixing the Failing Test**

Update the body of `test_demonstrating_the_given_decorator` so that it no longer fails. Run the fixed test function. How many times is the test function actually be executed when you run it?

</div>



## Describing Data: Hypothesis Strategies

Hypothesis provides us with so-called "strategies" for describing our data.
We are already familiar with the `integers` strategy;
Hypothesis' core strategies are all located in the `hypothesis.strategies` module.
The official documentation for the core strategies can be found [here](https://hypothesis.readthedocs.io/en/latest/data.html).

Here, we will familiarize ourselves with these core strategies and will explore some of the powerful methods that can be used to customize their behaviors.

<!-- #region -->
### Drawing examples from strategies

Hypothesis provides a useful mechanism for developing an intuition for the data produced by a strategy: a strategy, once initialized, has a `.example()` method that will randomly draw a representative value from the strategy. For example:

```python
# demonstrating usage of `<strategy>.example()`
>>> st.integers(-1, 1).example()
-1

>>> st.integers(-1, 1).example()
1
```

**Note: the** `.example()` **mechanism is only meant to be used for pedagogical purposes. You should never use this in your test suite**
because (among other reasons) `.example()` biases towards smaller and simpler examples than `@given`, and lacks the features to ensure any test failures are reproducible.

We will be leveraging the `.example()` method throughout the rest of this section to help provide an intuition for the data that Hypothesis' various strategies generate.
<!-- #endregion -->

<!-- #region -->
### Exploring Strategies

There are a number critical Hypothesis strategies for us to become familiar with. It is worthwhile to peruse through all of Hypothesis' [core strategies](https://hypothesis.readthedocs.io/en/latest/data.html#core-strategies), but we will take time to highlight a few here.

#### `st.booleans ()`

[st.booleans()](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.booleans) generates either `True` or `False`. This strategy will shrink towards `False`

```python
>>> st.booleans().example()
False
```
<!-- #endregion -->

<!-- #region -->

#### `st.lists ()`

[st.lists](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.lists) accepts *another* strategy, which describes the elements of the lists being generated. You can also specify:
 - bounds on the length of the list
 - if we want the elements to be unique
 - a mechanism for defining "uniqueness"

For example, the following strategy describes lists whose length varies from 2 to 10, and whose entries are integers on the domain $[-10, 20]$:

```python
>>> st.lists(st.integers(-10, 20), min_size=2, max_size=10).example()
[-10, 0, 5]
```

**`st.lists(...)` is the strategy of choice anytime we want to generate sequences of varying lengths with elements that are, themselves, described by strategies**.
<!-- #endregion -->

<!-- #region -->
#### `st.floats()`

[st.floats](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.floats) is a powerful strategy that generates all variety of floats, including `math.inf` and `math.nan`. You can also specify:
 - whether `math.inf` and `math.nan`, respectively, should be included in the data description
 - bounds (either inclusive or exclusive) on the floats being generated; this will naturally preclude `math.nan` from being generated
 - the "width" of the floats; e.g. if you want to generate 16-bit or 32-bit floats vs 64-bit
   (while Python's `float` is (usually) 64-bit, `width=32` ensures that the generated values can
   always be losslessly represented in 32 bits.  This is mostly useful for NumPy arrays.)

For example, the following strategy 64-bit floats that reside in the domain $[-100, 1]$:

```python
>>> st.floats(-100, 1).example()
0.3670816313319896
```
<!-- #endregion -->

<!-- #region -->
#### `st.tuples()`

The [st.tuples](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.tuples) strategy accepts $N$ Hypothesis strategies, and will generate length-$N$ tuples whose elements are drawn from the respective strategies that were specified as inputs.

For example, the following strategy will generate length-3 tuples whose entries are: integers, booleans, and floats:

```python
>>> st.tuples(st.integers(), st.booleans(), st.floats()).example()
(4628907038081558014, False, -inf)
```
<!-- #endregion -->

<!-- #region -->
#### `st.text()`

The [st.text](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.text) accepts an "alphabet" – a collection of string-characters – from which it will construct strings of varying lengths, whose bounds can be specified by the user.

For example, the following strategy will strings of lowercase vowels from length 2 to length 10:

```python
>>> st.text("aeiouy", min_size=2, max_size=10).example()
'oouoyoye'
```
<!-- #endregion -->

<!-- #region -->
#### `st.just()`

[st.just](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.just) is a strategy that "just" returns the value that you fed it. This is a convenient strategy that helps us to avoid having to manipulate our data before using it.

Suppose that we want a strategy that describes the shape of an array (i.e. a tuple of integers) that contains 1-20 two-dimensional vectors. E.g. `(5, 2)` is the shape of the array containing five two-dimensional vectors. We can leverage `st.just`, in conjunction with `st.integers` and `st.tuples`, towards this end:

```python
>>> st.tuples(st.integers(1, 20), st.just(2)).example()
(7, 2)
```
<!-- #endregion -->

<!-- #region -->
#### `st.one_of()`

The [st.one_of](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.one_of) allows us to specify a collection of strategies and any given datum will be drawn from "one of" them. E.g.

```python
# demonstrating st.one_of()
st.one_of(st.integers(), st.lists(st.integers()))
```

will draw values that are *either* integers or list of integers:

```python
>>> st.one_of(st.integers(), st.lists(st.integers())).example()
144

>>> st.one_of(st.integers(), st.lists(st.integers())).example()
[0, -22]
```

The "pipe" operator, `|` can be used between strategies, to chain `st.one_of` calls:

```python
# Using the pipe operation, | , in place of `st.one_of`
# This strategy generates integers or floats
# or lists that contain just the word "hello"

>>> (st.integers() | st.floats() | st.lists(st.just("hello"))).example()
['hello', 'hello']

>>> (st.integers() | st.floats() | st.lists(st.just("hello"))).example()
0
```
<!-- #endregion -->

<!-- #region -->
#### `st.sampled_from`

[st.sampled_from](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.sampled_from) accepts a collection of objects (anything that has a length and supports integer-based indexing is a collection; e.g. lists, tuples, strings, and numpy arrays). The strategy will return values that are sampled from this collections.

For example, the following strategy will sample from a list either `0`, `"a"`, or `(2, 2)`

```python
>>> st.sampled_from([0, "a", (2, 2)]).example()
'a'
```
<!-- #endregion -->

<div class="alert alert-info"> 

**Reading Comprehension: Exploring other Core Strategies**

Review the [rest of Hypothesis' core strategies](https://hypothesis.readthedocs.io/en/latest/data.html#core-strategies).
Write down a strategy, and print out a representative example, that describes the the data according to each of the following conditions:

   1. Dictionaries of arbitrary size whose keys are positive-values integers and whose values are `True` or `False.
   2. Length-4 strings whose elements are only lowercase vowels
   3. Permutations of the list `[1, 2, 3, 4]`

</div>


<!-- #region -->
<div class="alert alert-info">

**Reading Comprehension: Improving our tests using Hypothesis**

We will be writing improved tests for the basic functions – `count_vowels` and `merge_max_mappings` – by leveraging Hypothesis.
This reading comprehension question will require more substantial work than usual.
That being said, the experience that we will gain from this will be well worth the work.
Keep in mind that solutions are included at the end of this page, and that these can provide guidance if we get stuck.

Part 1: Testing correctness by construction

Write a hypothesis-driven test for the `count_vowels`; include this test in `test/test_basic_functions`.
This is a test function where we can explicit construct a string in parts: its non-vowel characters, non-y vowels, and y-vowels.
And thus, by constructing a string with a known number of vowel and non-vowel characters, we can know what the output of `count_vowels` *should* be for that input, and we can thus test for correctness in this way.
We will want to read about the [st.text()](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.text) strategy to construct the different parts of the string.
The standard library's built-in `string` module provides a string of all printable characters (`string.printable`).

We should ask ourselves: How general are input strings that we are constructing? Are there regular patterns in the strings that might prevent our test from identifying edge case bugs in `count_vowels`?


Part 2: Property-based testing

Write a hypothesis-driven test for `merge_max_mappings` ; include this test in `test/test_basic_functions`.
Here, we can't simply contrive the inputs to `merge_max_mappings` in a general way and know what its output should be – we would have to re-implement the function to do that.
Instead, we should *test the expected properties* of the merged dictionary.
For example, one such property is that the merged dictionary should only contain maximum values.
Another property would be that all of the keys among the input dictionaries should be present in the merged dictionary.
Take some time to think of other such properties that we should test for.
Ultimately we want to arrive at a comprehensive set of properties to test for such that we can be confident that our merged dictionary is correct.

We will want to use [st.dictionaries()](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.dictionaries) to describe the inputs to `merge_max_mappings`.
Although dictionary keys can be any hashable object, suffice it to use both integers and text for the keys, and integers for the dictionary values in this test, for simplicity's sake.


**We must remember to temporarily mutate our original functions to verify that these tests can actually catch bugs!**

Once we have added these tests to our test suite, we should re-run the entire test suite using `pytest tests` and check that our new Hypothesis-based tests are among the tests being run.
</div>

<!-- #endregion -->

<!-- #region -->
## Extending the Functionality of Strategies

Hypothesis strategies can be enriched through the use of two methods: `.map()` and `.filter()`.
These will permit us to leverage Hypothesis' core strategies to describe much more distinctive and diverse varieties of data.
We also will see that there is a `st.data()` strategy, which will enable us to draw from strategies interactively from within our tests.


### The `.map` method

Hypothesis strategies have the `.map` method, which permits us to [perform a mapping on the data](https://hypothesis.readthedocs.io/en/latest/data.html#mapping) being produced by a strategy.
This is achieved by passing the `.map` method a function (or any "callable");
upon drawing a value from a strategy, Hypothesis will feed that value to the function held by `.map()`, and the strategy
will return the value that was returned by the function.
In this way the strategy's output is automatically "mapped" to a transformed value via the function that we provided.

For example, if we want to draw only even-valued integers, we can simply use the following mapped strategy:

```python
# demonstrating the `.map()` method

def make_even(x): 
    return 2 * x

# `even_integers` is now a strategy that will only return even
# valued integers. This is achieved by ensuring that any integer
# drawn by `st.integers()` is "mapped" to an even value
# via the function x -> 2 * x
even_integers = st.integers().map(make_even)
```

```python
>>> even_integers.example()
-15414
```
<!-- #endregion -->

<!-- #region -->
#### A Brief Aside: Lambda Expressions

Python has a syntax, which we have yet to discuss, that permits us to conveniently define functions "on the fly".
A "lambda expression" is a syntax for defining a simple one-line function, making that function available for use in-place.
The key here is that, whereas standard functions first must be formally defined before they can be referenced in code, *a lambda expression can be written wherever a function is expected*.

For example, we can simplify the above mapping example by defining our mapping-function _within_ the `.map()` method:

```python
# Using a lambda expression to define a function
# "on the fly"
even_integers = st.integers().map(lambda x: 2 * x)
```

```python
>>> even_integers.example()
220
```

In general, the syntax for defining a lambda expression is:

```
lambda <comma-separated variable names>: <expression using variables>
```

Note that lambda expressions are restricted compared to typical function definitions: they do not permit default values or keyword arguments in their signatures, and a lambda's "body" must fit on one line.

Here are some examples of lambda expressions:

```python
# function definition
def add(x, y):
    return x + y

>>> add(2, 3)
5

# equivalent lambda expression
>>> (lambda x, y: x + y)(2, 3)
5

# function definition
def get_first_and_last_items(x):
    return x[0], x[-1]

>>> get_first_and_last_items(range(11))
(0, 10)

# equivalent lambda expression
>>> (lambda x: x[0], x[-1])(range(11))
(0, 10)
```

We will make keen use of lambdas in order to enrich our Hypothesis strategies. 
<!-- #endregion -->

<div class="alert alert-info"> 

**Reading Comprehension: Using the `.map` method to create a sorted list**

Using the `.map()` method, construct a Hypothesis strategy that produces a sorted list of integers.
Generate some examples from your strategy and check that they are sorted (we may have to generate quite a few examples to see a diverse set of values)

</div>


<div class="alert alert-info"> 

**Reading Comprehension: Getting creative with the `.map` method**

Construct a Hypothesis strategy that produces either the string `"cat"` or the string `"dog"`.
Then, write a test that uses this strategy;
it should simply test that either `"cat"` or `"dog"` was indeed produced by the strategy.
Run the test.

</div>


<!-- #region -->
### The `.filter` method

Hypothesis strategies can also [have their data filtered](https://hypothesis.readthedocs.io/en/latest/data.html#filtering) via the `.filter` method. 
`.filter` takes a function (or any "callable") that accepts as input the data generated by the strategy, and returns:

 - `True` if the data should pass through the filter
 - `False` if the data should be rejected by the filter

Consider, for instance, that you want to generate all integers other than `0`.
You can write the filtered strategy:

```python
# Demonstrating the `.filter()` method
non_zero_integers = st.integers().filter(lambda x: x != 0)
```

The `.filter` method is not magic – it is not able to "just know" how to avoid generating all barred values. 
A strategy that filters our too much data will prompt Hypothesis to raise an error.
For example, let's try to filter `st.integers()` so that it only produces values on $[10, 20]$.

```python
# Using `.filter()` to filter out a large proportion of generated
# values will result in an error
@given(st.integers().filter(lambda x: 10 <= x <= 20))
def test_aggressive_filter(x):
    pass
```

```python
>>> test_aggressive_filter()
---------------------------------------------------------------------------
FailedHealthCheck

FailedHealthCheck: It looks like your strategy is filtering out a lot of data. Health check found 50 filtered examples but only 2 good ones. This will make your tests much slower, and also will probably distort the data generation quite a lot. You should adapt your strategy to filter less. This can also be caused by a low max_leaves parameter in recursive() calls
See https://hypothesis.readthedocs.io/en/latest/healthchecks.html for more information about this. If you want to disable just this health check, add HealthCheck.filter_too_much to the suppress_health_check settings for this test
```

Clearly, in this instance, we should have simply used the strategy `st.integers(min_value=10, max_value=20)`.
<!-- #endregion -->

<!-- #region -->
### Drawing From Strategies Within a Test

We will often need to draw from a Hypothesis strategy in a context-dependent manner within our test.
Suppose, for example, that we want to describe two lists of integers, but we want to be sure that the second list is longer than the first.
[We can use the st.data() strategy to use strategies "interactively"](https://hypothesis.readthedocs.io/en/latest/data.html#drawing-interactively-in-tests) in this sort of way.

Let's see it in action.
Suppose that we want to generate two non-empty lists of integers, `x` and `y`, but we want to ensure that the values stored in `y` values are *larger than all of the values in* `x`.
The following test shows how we can leverage Hypothesis to describe these lists

```python
# We want all of `y`'s entries to be larger than `max(x)`
from typing import List

# Defining our test function:
#  - `x` is a non-empty list of integers.
#  - `data` is an object provided by Hypothesis that permits us
#     to draw interactively from other strategies within our test
@given(x=st.lists(st.integers(), min_size=1), data=st.data())
def test_two_constrained_lists(x, data):
    # We pass `data.draw(...)` a hypothesis strategy - it will draw a value from it.
    # Thus `y` is a non-empty list of integers, whose values are guaranteed to be
    # larger than `max(x)`
    y = data.draw(st.lists(st.integers(min_value=max(x) + 1), min_size=1), label="y")

    largest_x = max(x) 
    assert all(largest_x < item for item in y)
```
```python
# Running the test
>>> test_two_constrained_lists()
```
<!-- #endregion -->

The `given` operator is told to pass two values to our test: 

 - `x`, which is a list of integers drawn from strategies
 - `data`, which is an instance of the [st.DataObject](https://hypothesis.readthedocs.io/en/latest/_modules/hypothesis/strategies/_internal/core.html#DataObject) class; this instance is what gets drawn from the `st.data()` strategy

The only thing that you need to know about `st.DataObject` is that it's `draw` method expects a hypothesis search strategy, and that it will immediately draw a value from said strategy during the test.
You can also, optionally, pass a string to  `label` argument to the `draw` method.
This simply permits you to provide a name for the item that was drawn, so that any stack-trace that your test produces is easy to interpret.


<div class="alert alert-info">

**Reading Comprehension: Drawing from a strategy interactively**

Write a test that is fed a list (of varying length) of non-negative integers.
Then, draw a [set](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_III_Sets_and_More.html#The-%E2%80%9CSet%E2%80%9D-Data-Structure) of non-negative integers whose sum is at least as large as the sum of the list.
Assert that the  expected inequality between the sums hold.
Run the test.

Hint: use the `.filter()` method.

</div>



## The `example` Decorator

As mentioned before, Hypothesis strategies will draw values (pseudo)*randomly*.
Thus our test will potentially encounter different values every time it is run.
There are times where we want to be sure that, in addition the values produced by a strategy, specific values will tested. 
These might be known edge cases, critical use cases, or regression cases (i.e. values that were representative of passed bugs). 
Hypothesis provides [the example decorator](https://hypothesis.readthedocs.io/en/latest/reproducing.html#providing-explicit-examples), which is to be used in conjunction with the `given` decorator, towards this end.

Let's suppose, for example, that we want to write a test whose data are pairs of perfect-squares (e.g. 4, 16, 25, ...), and that we want to be sure that the pairs `(100, 144)`, `(16, 25)`, and `(36, 36)` are tested *every* time the test is run.
Let's use `example` to guarantee this.

<!-- #region -->
```python
# Using the `example` decorator to ensure that specific examples
# will always be passed as inputs to our test function

from hypothesis import example

# A hypothesis strategy that generates integers that are
# perfect squares
perfect_squares = st.integers().map(lambda x: x ** 2)


def is_square(x):
    """Returns True if `x` is a perfect square"""
    return int(x ** 0.5) == x ** 0.5


@example(a=36, b=36)
@example(a=16, b=25)
@example(a=100, b=144)
@given(a=perfect_squares, b=perfect_squares)
def test_pairs_of_squares(a, b):
    assert is_square(a)
    assert is_square(b)
```
```python
# running the test
>>> test_pairs_of_squares()
```
<!-- #endregion -->

Executing this test runs 103 cases: the three specified examples and one hundred pairs of values drawn via `given`.


## Links to Official Documentation

- [Hypothesis](https://hypothesis.readthedocs.io/)
- [The given decorator](https://hypothesis.readthedocs.io/en/latest/details.html#the-gory-details-of-given-parameters)
- [The Hypothesis example database](https://hypothesis.readthedocs.io/en/latest/database.html)
- [Core strategies](https://hypothesis.readthedocs.io/en/latest/data.html#core-strategies)
- [The .map method](https://hypothesis.readthedocs.io/en/latest/data.html#mapping)
- [The .filter method](https://hypothesis.readthedocs.io/en/latest/data.html#filtering)
- [Using data() to draw interactively in tests](https://hypothesis.readthedocs.io/en/latest/data.html#drawing-interactively-in-tests)
- [The example decorator](https://hypothesis.readthedocs.io/en/latest/reproducing.html#providing-explicit-examples)



## Reading Comprehension Solutions

<!-- #region -->
**Understanding How Hypothesis Works: Solution**

Define the `test_demonstrating_the_given_decorator` function as above, complete with the failing assertion, and add a print statement to the body of the function, which prints out the value for `x` and `y`.

```python
@given(x=st.integers(0, 10), y=st.integers(20, 30))
def test_demonstrating_the_given_decorator(x, y):
    print(x, y)
    assert 0 <= x <= 10

    # `y` can be any value in [20, 30]
    # this is a bad assertion: it should fail!
    assert 20 <= y <= 25
```

Run the test once and make note of the output that is printed. Consider copying and pasting the output to a notepad for reference. Next, rerun the test multiple times and make careful note of the printed output. What do you see? Is the output different from the first run? Does it differ between subsequent runs? Try to explain this behavior.

> The printed outputs between the first and second run differ. The first set out outputs is typically longer than that of the second run. After the second run, the printed outputs are always the exact same. What is happening here is that Hypothesis has to search for the falsifying example during the first run. Once it is identified, the example is recorded in the `.hypothesis` database. All of the subsequent runs are simply re-running this saved case, which is why their inputs are not changing.

In your file browser, navigate to the directory from which you are running this test; if you are following along in a Jupyter notebook, this is simply the directory containing said notebook. You should see a `.hypothesis` directory. As noted above, this is the database that contains the falsifying examples that Hypothesis has identified. Delete the `.hypothesis` directory and try re-running your test? What do you notice about the output now? You should also see that the `.hypothesis` directory has reappeared. Explain what is going on here.

> Deleting `.hypothesis` removes all of the falsifying examples that Hypothesis found for tests that were run from this particular directory. Thus running the test again means that Hypothesis has to find the falsifying example again from scratch. Once it does this, it creates a new database in `.hypothesis`, which is why this directory "reappears".
<!-- #endregion -->

<!-- #region -->
**Fixing the Failing Test: Solution**

Update the body of `test_demonstrating_the_given_decorator` so that it no longer fails.

> We simply need to fix the second assertion statement, specifying the bounds on `y`, so that it agrees with what is being drawn from the `integers` strategy.

```python
@given(x=st.integers(0, 10), y=st.integers(20, 30))
def test_demonstrating_the_given_decorator(x, y):
    assert 0 <= x <= 10
    assert 20 <= y <= 30
```

Run the fixed test function. How many times is the test function actually be executed when you run it?

> The `given` decorator, by default, will draw 100 sets of example values from the strategies that are passed to it and will thus execute the decorated test function 100 times.

```python
# no output (the function returns `None`) means that the test passed
>>> test_demonstrating_the_given_decorator()
```
<!-- #endregion -->

<!-- #region -->
**Exploring other Core Strategies: Solution**

Dictionaries of arbitrary size whose keys are positive-values integers and whose values are `True` or `False.

```python
>>> st.dictionaries(st.integers(min_value=1), st.booleans()).example()
{110: True, 19091: True, 136348032: False, 78: False, 9877: False}
```

Length-4 strings whose elements are only lowercase vowels

```python
>>> st.text(alphabet="aeiou", min_size=4, max_size=4).example()
'uiai'
```

Permutations of the list `[1, 2, 3, 4]`

```python
>>> st.permutations([1, 2, 3, 4]).example()
[2, 3, 1, 4]
```
<!-- #endregion -->

**Improving our tests using Hypothesis: Solution**

Part 1: Testing correctness by construction

Write a hypothesis-driven test for the `count_vowels`; include this test in `test/test_basic_functions`.
This is a test function where we can explicit construct a string in parts: its non-vowel characters, non-y vowels, and y-vowels.
And thus, by constructing a string with a known number of vowel and non-vowel characters, we can know what the output of `count_vowels` *should* be for that input, and we can thus test for correctness in this way.
We will want to read about the [st.text()](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.text) strategy to construct the different parts of the string.
The standard library's built-in `string` module provides a string of all printable characters (`string.printable`).

We should ask ourselves: How general are input strings that we are constructing? Are there regular patterns in the strings that might prevent our test from identifying edge case bugs in `count_vowels`?

<!-- #region -->
```python
from string import printable
from random import shuffle

import hypothesis.strategies as st
from hypothesis import given, note

# a list of all printable non-vowel characters
_not_vowels = "".join([l for l in printable if l.lower() not in set("aeiouy")])


@given(
    not_vowels=st.text(alphabet=_not_vowels),
    vowels_but_not_ys=st.text(alphabet="aeiouAEIOU"),
    ys=st.text(alphabet="yY"),
)
def test_count_vowels_hypothesis(not_vowels, vowels_but_not_ys, ys):
    """
    Constructs an input string with a known number of:
       - non-vowel characters
       - non-y vowel characters
       - y characters
    
    and thus, by constructions, we can test that the output
    of `count_vowels` agrees with the known number of vowels
    """
    # list of characters
    letters = list(not_vowels) + list(vowels_but_not_ys) + list(ys)
    
    # We need to shuffle the ordering of our characters so that
    # our input string isn't unnaturally patterned; e.g. always 
    # have its vowels at the end
    shuffle(letters)
    in_string = "".join(letters)
    
    # Hypothesis provides a `note` function that will print out
    # whatever input you give it, but only in the case that the
    # test fails.
    # This way we can see the exact string that we fed to `count_vowels`,
    # if it caused our test to fail
    note("in_string: " + in_string)
    
    # testing that `count_vowels` produces the expected output
    # both including and excluding y's in the count
    assert count_vowels(in_string, include_y=False) == len(vowels_but_not_ys)
    assert count_vowels(in_string, include_y=True) == len(vowels_but_not_ys) + len(ys)
```
<!-- #endregion -->

Part 2: Property-based testing

Write a hypothesis-driven test for `merge_max_mappings` ; include this test in `test/test_basic_functions`.
Here, we can't simply contrive the inputs to `merge_max_mappings` in a general way and know what its output should be – we would have to re-implement the function to do that.
Instead, we should *test the expected properties* of the merged dictionary.
For example, one such property is that the merged dictionary should only contain maximum values.
Another property would be that all of the keys among the input dictionaries should be present in the merged dictionary.
Take some time to think of other such properties that we should test for.
Ultimately we want to arrive at a comprehensive set of properties to test for such that we can be confident that our merged dictionary is correct.

We will want to use [st.dictionaries()](https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.dictionaries) to describe the inputs to `merge_max_mappings`.
Although dictionary keys can be any hashable object, suffice it to use both integers and text for the keys, and integers for the dictionary values in this test, for simplicity's sake.

<!-- #region -->
```python
@given(
    dict1=st.dictionaries(
        keys=st.integers(-10, 10) | st.text(), values=st.integers(-10, 10)
    ),
    dict2=st.dictionaries(
        keys=st.integers(-10, 10) | st.text(), values=st.integers(-10, 10)
    ),
)
def test_merge_max_mappings_hypothesis(dict1, dict2):
    merged_dict = merge_max_mappings(dict1, dict2)
    
    # property: `merged_dict` contains all of the keys among
    # `dict1` and `dict2`
    assert set(merged_dict) == set(dict1).union(dict2), \
        "novel keys were introduced or lost"

    # property: `merged_dict` only contains values that appear
    # among `dict1` and `dict2`
    assert set(merged_dict.values()) <= set(dict1.values()).union(
        dict2.values()
    ), "novel values were introduced"

    # property: `merged_dict` only contains key-value pairs with
    # the largest value represented among the pairs in `dict1`
    # and `dict2`
    assert all(dict1[k] <= merged_dict[k] for k in dict1) and \
           all(dict2[k] <= merged_dict[k] for k in dict2), \
        "`merged_dict` contains a non-max value"

    # property: `merged_dict` only contains key-value pairs that
    # appear among `dict1` and `dict2`
    for k, v in merged_dict.items():
        assert (k, v) in dict1.items() or \
               (k, v) in dict2.items(), \
            "`merged_dict` did not preserve the key-value pairings"
```
<!-- #endregion -->

**Using the `.map` method to create a sorted list: Solution**

Using the `.map()` method, construct a Hypothesis strategy that produces a sorted list of integers.
Generate some examples from your strategy and check that they are sorted (we may have to generate quite a few examples to see a diverse set of values)

<!-- #region -->
```python
# Note that the built-in `sorted` function can be supplied 
# directly to the `.map()` method - there is no need to define
# a function or use a lambda expression here
sorted_list_of_ints = st.lists(st.integers()).map(sorted)
```
```python
>>> sorted_list_of_ints.example()
[-27120, 97, 12805]
```
<!-- #endregion -->


**Getting creative with the `.map` method: Solution**

Construct a Hypothesis strategy that produces either the string `"cat"` or the string `"dog"`.
Then, write a test that uses this strategy;
it should simply test that either `"cat"` or `"dog"` was indeed produced by the strategy.
Run the test

<!-- #region -->
```python
# We "hijack" the `st.booleans()` strategy, which only generates 
# `True` or `False`, and use the `.map` method to transform these
# two outputs to `"cat"` or `"dog"`.
#
# This is only one of many ways that you could have created this
# strategy
cat_or_dog = st.booleans().map(lambda x: "cat" if x else "dog")

@given(cat_or_dog)
def test_cat_dog(x):
    assert x in {"cat", "dog"}
```    
```python
# running the test
>>> test_cat_dog()
```
<!-- #endregion -->

<!-- #region -->
**Drawing from a strategy interactively: Solution**

Write a test that is fed a list (of varying length) of non-negative integers.
Then, draw a [set](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_III_Sets_and_More.html#The-%E2%80%9CSet%E2%80%9D-Data-Structure) of non-negative integers whose sum is at least as large as the sum of the list.
Assert that the  expected inequality between the sums hold.
Run the test.


Hint: use the `.filter()` method.
<!-- #endregion -->

<!-- #region -->
```python
@given(the_list=st.lists(st.integers(min_value=0)), data=st.data())
def test_interactive_draw_skills(the_list, data):
    the_set = data.draw(
        st.sets(elements=st.integers(min_value=0)).filter(
            lambda x: sum(x) >= sum(the_list)
        )
    )
    assert sum(the_list) <= sum(the_set)
```
```python
# running the test
>>> test_interactive_draw_skills()
```
<!-- #endregion -->
