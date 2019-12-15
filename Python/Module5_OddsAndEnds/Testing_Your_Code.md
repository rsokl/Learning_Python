---
jupyter:
  jupytext:
    formats: ipynb,md
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
   :description: Topic: Writing tests for your code, Difficulty: Medium, Category: Section
   :keywords: test, pytest, automated, unit, integration, property-based, hypothesis  
<!-- #endraw -->

# Testing Your Code

This section will introduce us to the critically-important and often-overlooked process of testing code. 
We will begin by considering some driving motivations for writing tests.
Next, we will study the basic anatomy of a test-function, including the `assert` statement, which serves as the nucleus of our test functions.
Armed with the ability to write a rudimentary test, we will welcome, with open arms, the powerful testing framework [pytest](https://docs.pytest.org/).
This will inform how we structure our tests alongside our Python project that we are developing; with pytest, we can incisively run our tests with the press of a single button.
Furthermore, it will allow us to greatly streamline and even begin to automate some of our tests.
Finally, we will take a step back to consider some strategies for writing effective tests.
Among these is a methodology that is near and dear to my heart: property-based testing.
This will take us down a bit of a rabbit hole, where we will find the powerful property-based testing library [Hypothesis](https://hypothesis.readthedocs.io/) waiting to greet us (adorned with the mad Hatter's cap and all).



## Why Should We Write Tests?
With great power comes great responsibility: tests help us be responsible for the code that we create and that others will (hopefully) use.

The fact of the matter is that everyone already tests their code to some extent.
After coding, say, a new function, it is only natural to contrive an input to feed it, and to check that it returns the output that you expected.
To the extent that anyone would want to see evidence that their code works, we need not motivate the importance of testing.

Less obvious is the massive benefits that we stand to gain from formalizing this testing process.
And by "formalizing", we mean taking the test scenarios that we were running our code through, and encapsulating them in their own functions that can be run from end-to-end.
We will accumulate these functions into a "test suite" that we can run quickly and repeatedly.

There are plenty of practical details ahead for us to learn, so let's expedite this discussion and simply list some of the benefits that we can expect to reap from writing a robust test suite:

- It saves us lots of time:
  > After you have devised a test scenario for your code, it may only take us a second or so to run it - perhaps we need only run a couple of Jupyter notebook cells to check the output.
  > However, this will quickly become unwieldy as we write more code and devise more test scenarios.
  > Soon we will be dissuaded from running our tests except for on rare occasions.
  > With a proper test suite, we can run all of our test scenarios with the push of a button, and a series of green check-marks (or red x's...) will summarize the health of our project (insofar as our tests serve as good diagnostics).
  > This, of course, also means that we will find and fix bugs much faster!
  > In the long run, our test suite will afford us the ability to aggressively exercise (and exorcise) our code at little cost.
- It increases the "shelf life" of our code:
  > If you've ever dusted off a project that you haven't used for years (or perhaps only months or weeks...), you might know the tribulations of getting old code to work.
  > Perhaps, in the interim, new versions of our project's dependencies, like PyTorch or Matplotlib, were released and have incompatibilities with our project's code.
  > And perhaps _we can't even remember_ all of the ways in which our project is supposed to work.
  > Our test suite provides us with a simple and incisive way to dive back into our work.
  > It will point us to any potential incompatibilities that have accumulated over time.
  > It also provides us with a large collection of detailed use-cases of our code;
  > we can read through our tests remind ourselves of the inner-workings of our project.
- It will inform the design and usability of our project for the better:
  > Although it may not be obvious from the outset, writing testable code leads to writing better code.
  > This is, in part, because the process of writing tests gives us the opportunity to actually _use_ our code under varied circumstances.
  > The process of writing tests will help us suss out cumbersome function interfaces, brittle statefulness, and redundant capabilities in our code. If _we_ find it frustrating to use our code within our tests, then surely others will find it frustrating to use in applied settings.
- It makes it easier for others to contribute to a project:
  > Having a healthy test suite lowers the barrier to entry for a project. 
  > A contributor can make improvements to the project and quickly check to see if they have broken it or changed any of its behavior.

This all sounds great, but where do we even start the process writing a test suite? 
Let's begin by seeing what constitutes a basic test function.

<!-- #region -->
## The Basic Anatomy of a Test Function
Let's write a function that tests the following `count_values` code:

```python
# Defining a function that we will be testing

def count_vowels(x: str, include_y: bool = False) -> int:
    """Returns the number of vowels contained in `x`

    Examples
    --------
    >>> count_vowels("happy")
    1
    >>> count_vowels("happy", include_y=True)
    2
    """
    vowels = set("aeiouAEIOU")
    if include_y:
        vowels.update("yY")
    return sum(1 for char in x if char in vowels)
```

(Note that we will be making use of [type hinting](https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Writing_Good_Code.html#Type-Hinting) to help document the interfaces of our functions.
You may want to briefly review the linked material if this is unfamiliar to you)

For our most basic test, we can simply call `count_values` under various contrived inputs and *assert* that it returns the expected output.
The desired behavior for this test function, upon being run, is to:

- Raise an error if any of our assertions *failed* to hold true.
- Complete "silently" if all of our assertions hold true (i.e. our test function will simply [return None](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Functions.html#The-return-Statement))

```python
# Writing a test function for `count_vowels`

def test_count_vowels_basic():
    assert count_vowels("aA bB yY", include_y=False) == 2
    assert count_vowels("aA bB yY", include_y=True) == 4
```

To run this test, we simply call the function:

```python
# running our test function
>>> test_count_vowels_basic()
```

As described above, the fact our function runs, simply returning `None` without raising any errors, means that our code has passed this test. We've written and run our very first test!

Let's look more carefully at the structure of `test_count_vowels_basic`.
Note that this function doesn't take in any inputs;
thanks to [Python's scoping rules](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Scope.html), we can reference our `count_vowels` function within our test as long as it is defined in the same "namespace" as `test_count_vowels_basic`.
That is, we can either define `count_vowels` in the same .py file (or Jupyter notebook, if you are following along with this material in a notebook) as `test_count_vowels_basic`, or we can [import](https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Modules_and_Packages.html#Import-Statements) `count_vowels` from wherever it is defined, and into the file containing our test.
The latter scenario is by far the most common one in practice. 
More on this later.

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: The Basic Anatomy of a Test**

Add an additional assertion to the body of `test_count_vowels_basic`, which tests whether `count_vowels` handles the empty-string (`""`) case appropriately.
Make sure to run your updated test to see if it passes.

</div>
<!-- #endregion -->

With our first test function under our belt, it is time for us understand how `assert` statements work and how they should be used. 
<!-- #endregion -->

<!-- #region -->
### Assert Statements
Similar to `return`, `def`, or `if`, the term `assert` is a reserved term in the Python language. 
It has the following specialized behavior:

```python
# demonstrating the rudimentary behavior of the `assert` statement

# asserting an expression whose boolean-value is `True` will complete "silently"
>>> assert 1 < 2

# asserting an expression whose boolean-value is `False` raises an error
>>> assert 2 < 1
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-5-c82711d5fe4d> in <module>
----> 1 assert 2 < 1

AssertionError: 

# we can include an error message with our assertion
>>> assert 0 in [1, 2, 3], "0 is not in the list"
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-8-e72fb36dc785> in <module>
----> 1 assert 0 in [1, 2, 3], "0 is not in the list"

AssertionError: 0 is not in the list
```

The general form of an assertion statement is:

```python
assert <expression> [, <error-message>] 
```

In an assertion statement, `bool` is called on the object that is returned by `<expression>` - if `bool(<expression>)` returns `False`, then an `AssertionError` is raised.
If you included a string in the assertion statement - separated from `<expression>` by a comma - then this string will be printed as the error message.

See that the assertion statement: 
```python
assert expression, error_message
```

is effectively shorthand for the following code:

```python
# long-form equivalent of: `assert expression, error_message`
if bool(expression) is False:
    raise AssertionError(error_message)
```

<!-- #endregion -->
<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: Assertions**

Given the following objects:

```python
a_list = []
a_number = 22
a_string = "abcdef"
```

Write two assertion statements, each one with the corresponding behavior:

- asserts that `a_list` is _not_ empty
- asserts that the number of vowels in `a_string` is less than `a_number`; include and error message that prints the actual number of vowels

</div>
<!-- #endregion -->

<!-- #region -->
#### What is the Purpose of an Assertion?
In our code, an assertion should be used as _a statement that is true unless there is a bug our code_.
It is plain to see that the assertions in `test_count_vowels_basic` fit this description.
However, it can also be useful to include assertions within our source code itself.

For instance, we know that `count_vowels` should always return a non-negative integer, and that this count should not exceed the number of characters in the input string.
We can explicitly assert that this is the case:

```python
# an example of including an assertion within our source code

def count_vowels(x: str, include_y: bool = False) -> int:
    """Returns the number of vowels contained in `x`

    Examples
    --------
    >>> count_vowels("happy")
    1
    >>> count_vowels("happy", include_y=True)
    2
    """
    vowels = set("aeiouAEIOU")
    if include_y:
        vowels.update("yY")
    count = sum(1 for char in x if char in vowels)
    
    # This statement should always be true: it is not checking for 
    # bad input from a user, it is asserting that the internal logic 
    # of our function is correct
    assert isinstance(count, int) and 0 <= count <= len(x)
    return count
```

Note that this assertion *is not meant to check if the user passed bad inputs for* `x` *and* `include_y`.
Rather, it is meant to assert that our own internal logic holds true.

Admittedly, the `count_vowels` function is simple enough that the inclusion of this assertion is rather pedantic.
That being said, as we write increasingly sophisticated code, we will find that the inclusion of assertions will help us catch bad internal logic and oversights within our code base.
<!-- #endregion -->

<!-- #endregion -->

## Links to Official Documentation



<!-- #region -->
## Reading Comprehension Solutions

**The Basic Anatomy of a Test: Solution**

Add an additional assertion to the body of `test_count_vowels_basic`, which tests whether `count_vowels` handles the empty-string (`""`) case appropriately.
Make sure to run your updated test to see if it passes.

```python
def test_count_vowels_basic():
    assert count_vowels("aA bB yY", include_y=False) == 2
    assert count_vowels("aA bB yY", include_y=True) == 4
    assert count_vowels("", include_y=True) == 0
```

```python
# running the test in a notebook-cell: the function should simply return
# `None` if all assertions hold true
>>> test_count_vowels_basic()
```

**Assertions: Solution**
```python
a_list = []
a_number = 22
a_string = "abcdef"
```

Assert that `a_list` is _not_ empty:

```python
>>> assert a_list
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-10-2eba8294859e> in <module>
----> 1 assert a_list

AssertionError: 
```

> You may have written `assert len(a_list) > 0` - this is also correct.
> However, recall that calling `bool` on any sequence (list, tuple, string, etc.) will return `False` if the sequence is empty.
> This is a reminder that an assertion statement need not include an explicit logical statement, such as an inequality - that `bool` will be called on whatever the provided expression is.

Assert that the number of vowels in `a_string` is fewer than `a_number`; include and error message that prints the actual number of vowels:

```python
>>> assert count_vowels(a_string) < a_number, f"Number of vowels, {count_vowels(a_string)}, exceeds {a_number}"
```

> Note that we make use of an [f-string](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Formatting-strings) as a convenient means for writing an informative error message.

<!-- #endregion -->
