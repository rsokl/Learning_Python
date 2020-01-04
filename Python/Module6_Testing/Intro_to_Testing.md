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
   :keywords: test, automated, unit, assert  
<!-- #endraw -->

# Introduction to Testing

This section will show us just how simple it is to write rudimentary tests. We need only recall some of Python's basic scoping rules and introduce ourselves to the `assert` statement to write a genuine test function. That being said, we will quickly encounter some important questions to ponder. How do we know that our tests work? And, how do we know that our tests are effective? These questions will drive us deeper into the world of testing. 

Before we hit the ground running, let's take a moment to consider some motivations for testing out code.

<!-- #region -->
## Why Should We Write Tests?

The fact of the matter is that it is intuitive for most people to test their code to some extent.
After writing, say, a new function, it is only natural to contrive an input to feed it, and to check that the function returns the output that we expected.
To the extent that one would want to see evidence that their code works, we need not motivate the importance of testing.

Less obvious are the massive benefits that we stand to gain from automating this testing process.
And by "automating", we mean taking the test scenarios that we were running our code through, and encapsulating them in their own functions that can be run from end-to-end.
We will accumulate these test functions into a "test suite" that we can run quickly and repeatedly.

There are plenty of practical details ahead for us to learn, so let's expedite this discussion and simply list some of the benefits that we can expect to reap from writing a robust test suite:

**It saves us lots of time**:

> After you have devised a test scenario for your code, it may only take us a second or so to run it; perhaps we need only run a couple of Jupyter notebook cells to verify the output of our code.
> This, however, will quickly become unwieldy as we write more code and devise more test scenarios.
> Soon we will be dissuaded from running our tests except for on rare occasions.
> 
> With a proper test suite, we can run all of our test scenarios with the push of a button, and a series of green check-marks (or red x's...) will summarize the health of our project (insofar as our tests serve as good diagnostics).
> This, of course, also means that we will find and fix bugs much faster!
> In the long run, our test suite will afford us the ability to aggressively exercise (and exorcise) our code at little cost.

**It increases the "shelf life" of our code:**

> If you've ever dusted off a project that you haven't used for years (or perhaps only months or weeks...), you might know the tribulations of getting old code to work.
> Perhaps, in the interim, new versions of our project's dependencies, like PyTorch or Matplotlib, were released and have incompatibilities with our project's code.
> And perhaps _we can't even remember_ all of the ways in which our project is supposed to work.
> Our test suite provides us with a simple and incisive way to dive back into our work.
> It will point us to any potential incompatibilities that have accumulated over time.
> It also provides us with a large collection of detailed use-cases of our code;
> we can read through our tests and remind ourselves of the inner-workings of our project.


**It will inform the design and usability of our project for the better:**

> Although it may not be obvious from the outset, writing testable code leads to writing better code.
> This is, in part, because the process of writing tests gives us the opportunity to actually _use_ our code under varied circumstances.
> The process of writing tests will help us suss out cumbersome function interfaces, brittle statefulness, and redundant capabilities in our code. Ultimately, if _we_ find it frustrating to use our code within our tests, then surely others will find the code frustrating to use in applied settings.

**It makes it easier for others to contribute to a project:**

> Having a healthy test suite lowers the barrier to entry for a project. 
> A contributor can rely on our project's tests to quickly check to see if their changes to our code have broken the project or changed any of its behavior in unexpected ways.

This all sounds great, but where do we even start the process of writing a test suite? 
Let's begin by seeing what constitutes a basic test function.
<!-- #endregion -->

<!-- #region -->
## Writing Our First Tests

### Our "Source Code"
We need some code to test. For the sake of this introduction, let's borrow a couple of functions that may look familiar from previous modules.
These will serve as our "source code"; i.e. these are functions that we have written for our project and that need to be tested. 

```python
# Defining functions that we will be testing

def count_vowels(x, include_y=False):
    """Returns the number of vowels contained in `x`.
    
    The vowel 'y' is included optionally.
    
    Parameters
    ----------
    x : str
        The input string

    include_y : bool, optional (default=False)
        If `True` count y's as vowels

    Returns
    -------
    vowel_count: int

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


def merge_max_mappings(dict1, dict2):
    """ Merges two dictionaries based on the largest value
    in a given mapping.

    Parameters
    ----------
    dict1 : Dict[str, float]
    dict2 : Dict[str, float]

    Returns
    -------
    merged : Dict[str, float]
        The dictionary containing all of the keys common
        between `dict1` and `dict2`, retaining the largest
        value from common mappings.
    
    Examples
    --------
    >>> x = {"a": 1, "b": 2}
    >>> y = {"b": 100, "c": -1}
    >>> merge_max_mappings(x, y)
    {'a': 1, 'b': 100, 'c': -1}
    """
    # `dict(dict1)` makes a copy of `dict1`. We do this 
    # so that updating `merged` doesn't also update `dict1`
    merged = dict(dict1)
    for key, value in dict2.items():
        if key not in merged or value > merged[key]:
            merged[key] = value
    return merged
```

As always, it is useful for us to follow along with this material in a Jupyter notebook.
We ought to take time to define these functions and run inputs through them to make sure that we understand what they are doing.
Testing code that we don't understand is a lost cause!
<!-- #endregion -->
<!-- #region -->
### The Basic Anatomy of a Test

Let's write a test for `count_vowels`. For our most basic test, we can simply call `count_values` under various contrived inputs and *assert* that it returns the expected output.
The desired behavior for this test function, upon being run, is to:

- Raise an error if any of our assertions *failed* to hold true.
- Complete "silently" if all of our assertions hold true (i.e. our test function will simply [return None](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Functions.html#The-return-Statement))

Here, we will be making use of Python's `assert` statements, whose behavior will be easy to deduce from the context of this test alone.
We will be formally introduced to the `assert` statement soon.

```python
# Writing a rudimentary test function for `count_vowels`

def test_count_vowels_basic():
    assert count_vowels("aA bB yY", include_y=False) == 2
    assert count_vowels("aA bB yY", include_y=True) == 4
```

To run this test, we simply call the function:

```python
# running our test function
>>> test_count_vowels_basic()  # passes: returns None | fails: raises error
```

As described above, the fact our function runs and simply returns `None` (i.e. we see no output when we run this test in a console or notebook cell) means that our code has passed this test. We've written and run our very first test! It certainly isn't the most robust test, but it is a good start.

Let's look more carefully at the structure of `test_count_vowels_basic`.
Note that this function doesn't take in any inputs;
thanks to [Python's scoping rules](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Scope.html), we can reference our `count_vowels` function within our test as long as it is defined in the same "namespace" as `test_count_vowels_basic`.
That is, we can either define `count_vowels` in the same .py file (or Jupyter notebook, if you are following along with this material in a notebook) as `test_count_vowels_basic`, or we can [import](https://www.pythonlikeyoumeanit.com/Module5_OddsAndEnds/Modules_and_Packages.html#Import-Statements) `count_vowels`, from wherever it is defined, into the file containing our test.
The latter scenario is by far the most common one in practice. 
More on this later.

<!-- #endregion -->

<div class="alert alert-warning">

**Takeaway**: 

A "test function" is designed to provide an encapsulated "environment" (namespace to be more precise) in which we can exercise parts of our source code and assert that the code behaves as-expected. The basic anatomy of a test function is such that it:

- contains one or more `assert` statements, each of which will raise an error if our source code misbehaves 
- simply returns `None` if all of the aforementioned assertions held true
- can be run end-to-end simply by calling the test function without passing it any parameters; we rely on Python's scoping rules to call our source code within the body of the test function without explicitly passing anything to said test function

</div>


<div class="alert alert-info"> 

**Reading Comprehension: Adding Assertions to a Test**

Add an additional assertion to the body of `test_count_vowels_basic`, which tests that `count_vowels` handles empty-string (`""`) input appropriately.
Make sure to run your updated test to see if it passes.

</div>


<div class="alert alert-info"> 

**Reading Comprehension: The Basic Anatomy of a Test**

Write a rudimentary test function for `merge_max_mappings`. This should adhere to the basic structure of a test function that we just laid out. See if you can think of some "edge cases" to test, which we may have overlooked when writing `merge_max_mappings`.

</div>

<!-- #region -->
## The `assert` Statement
With our first test functions under our belt, it is time for us to clearly understand how `assert` statements work and how they should be used.

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

When an assertion statement is executed, the built-in `bool` function is called on the object that is returned by `<expression>`; if `bool(<expression>)` returns `False`, then an `AssertionError` is raised.
If you included a string in the assertion statement - separated from `<expression>` by a comma - then this string will be printed as the error message.

See that the assertion statement: 
```python
assert expression, error_message
```

is effectively shorthand for the following code (barring some additional details):

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

Write two assertion statements with the respective behaviors:

- asserts that `a_list` is _not_ empty
- asserts that the number of vowels in `a_string` is less than `a_number`; include an error message that prints the actual number of vowels

</div>
<!-- #endregion -->

<!-- #region -->
#### What is the Purpose of an Assertion?
In our code, an assertion should be used as _a statement that is true unless there is a bug in our code_.
It is plain to see that the assertions in `test_count_vowels_basic` fit this description.
However, it can also be useful to include assertions within our source code itself.
For instance, we know that `count_vowels` should always return a non-negative integer for the vowel-count, and that it is illogical for this count to exceed the number of characters in the input string.
We can explicitly assert that this is the case:

```python
# an example of including an assertion within our source code

def count_vowels(x: str, include_y: bool = False) -> int:
    vowels = set("aeiouAEIOU")
    if include_y:
        vowels.update("yY")
    count = sum(1 for char in x if char in vowels)
    
    # This assertion should always be true: it is asserting that 
    # the internal logic of our function is correct
    assert isinstance(count, int) and 0 <= count <= len(x)
    return count
```

Note that this assertion *is not meant to check if the user passed bad inputs for* `x` *and* `include_y`.
Rather, it is meant to assert that our own internal logic holds true.

Admittedly, the `count_vowels` function is simple enough that the inclusion of this assertion is rather pedantic.
That being said, as we write increasingly sophisticated code, we will find that this sort of assertion will help us catch bad internal logic and oversights within our code base.
We will also see that keen use of assertions can make it much easier for us to write good tests.
<!-- #endregion -->

## Testing Our Tests

It is surprisingly easy to unwittingly write a broken test: a test that always passes, or a test that simply doesn't exercise our code in the way that we had intended.
Broken tests are insidious; they are alarms that fail to sound when they are supposed to.
They create misdirection in the bug-finding process and can mask problems with our code.
**Thus a critical step in the test-writing process is to intentionally mutate the function of interest - to corrupt its behavior so that we can verify that our test works.**
Once we confirm that our test does indeed raise an error as-expected, we restore the function to its original form and re-run the test and see that it passes. 

A practical note: we ought to mutate our function in a way that is trivial to undo. We can make use of code-comments towards this end.
All [IDEs](https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Getting_Started_With_IDEs_and_Notebooks.html) have the ability to "block-comment" selected code.
In order to block-comment code in a Jupyter notebook code cell, highlight the lines of code and press `CTRL + /`.
The same key-combination will also un-comment a highlighted block of commented code.



<div class="alert alert-info"> 

**Reading Comprehension: Testing Your Test via Manual Mutation**

Temporarily change the body of `count_vowels` such that the second assertion in `test_count_vowels_basic` raises an error.
Run the test to confirm that the second assertion raises,
and then restore `count_vowels` to its original form.
Finally, rerun the test to see that `count_vowels` once again passes all of the assertions.
    
Repeat this process given the test that you wrote for `merge_max_mappings`.
Try breaking the function such that it always merges in values from `dict2`, even if those values are smaller.

</div>



## Our Work, Cut Out

We see now that the concept of a "test function" isn't all that fancy.
Compared to other code that we have written, writing a function that simply runs a hand full of assertions is far from a heavy lift for us.
Of course, we must be diligent and take care to test our tests, but we can certainly manage this as well.
With this in hand, we should take stock of the work and challenges that lie in our path ahead.

It is necessary that we evolve beyond manual testing.
There are multiple facets to this observation.
First, we must learn how to organize our test functions into a test suite that can be run in one fowl swoop.
Next, it will become increasingly apparent that a test function often contain large amounts of redundant code shared across its litany of assertions.
We will want to "parametrize" our tests to distill them down to their most concise and functional forms.
Finally, and most importantly, it may already be evident that the process of contriving known inputs and outputs to use in our tests is a highly manual and tedious process; furthermore, it is a process that will become increasingly cumbersome as our source code becomes more sophisticated.
To combat this, we will seek out alternative, powerful testing methodologies, including property-based testing.


## Links to Official Documentation

- [The assert statement](https://docs.python.org/3/reference/simple_stmts.html?highlight=assert#the-assert-statement)


## Reading Comprehension Solutions

<!-- #region -->
**Adding Assertions to a Test: Solution**

Add an additional assertion to the body of `test_count_vowels_basic`, which tests whether `count_vowels` handles the empty-string (`""`) case appropriately.
Make sure to run your updated test to see if it passes.

```python
def test_count_vowels_basic():
    # test basic strings with uppercase and lowercase letters
    assert count_vowels("aA bB yY", include_y=False) == 2
    assert count_vowels("aA bB yY", include_y=True) == 4
    
    # test empty strings
    assert count_vowels("", include_y=False) == 0
    assert count_vowels("", include_y=True) == 0
```

```python
# running the test in a notebook-cell: the function should simply return
# `None` if all assertions hold true
>>> test_count_vowels_basic()
```
<!-- #endregion -->

<!-- #region -->
**The Basic Anatomy of a Test: Solution**

Write a rudimentary test function for `merge_max_mappings`.

> Let's test the use case that is explicitly documented in the Examples section of the function's docstring.
> We can also test cases where one or both of the inputs are empty dictionaries. 
> These can often be problematic edge cases that we didn't consider when writing our code. 

```python
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

```python
# running the test (seeing no errors means the tests all passed)
>>> test_merge_max_mappings()
```
<!-- #endregion -->

<!-- #region -->
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

Assert that the number of vowels in `a_string` is fewer than `a_number`; include an error message that prints the actual number of vowels:

```python
>>> assert count_vowels(a_string) < a_number, f"Number of vowels, {count_vowels(a_string)}, exceeds {a_number}"
```

> Note that we make use of an [f-string](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Formatting-strings) as a convenient means for writing an informative error message.
<!-- #endregion -->

<!-- #region -->
**Testing Your Test via Manual Mutation: Solution**

Temporarily change the body of `count_vowels` such that the _second_ assertion in `test_count_vowels_basic` raises an error.
> Let's comment out the `if include_y` block in our code. This should prevent us from counting y's, and thus should violate the second assertion in our test.

```python
# Breaking the behavior of `include_y=True`
def count_vowels(x: str, include_y: bool = False) -> int:
    vowels = set("aeiouAEIOU")
    # if include_y:
    #    vowels.update("yY")
    return sum(1 for char in x if char in vowels)
```

```python
# the second assertion should raise an error
>>> test_count_vowels_basic()
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-5-32301ff829e9> in <module>
----> 1 test_count_vowels_basic()

<ipython-input-4-99ef0ca3d859> in test_count_vowels_basic()
      1 def test_count_vowels_basic():
      2     assert count_vowels("aA bB yY", include_y=False) == 2
----> 3     assert count_vowels("aA bB yY", include_y=True) == 4

AssertionError: 
```

> See that the error output, which is called a "stack trace", indicates with an ASCII-arrow that our second assertion is the one that is failing.
> Thus we can be confident that that assertion really does help to ensure that we are counting y's correctly.

Restore `count_vowels` to its original form and rerun the test to see that `count_vowels` once again passes all of the assertions.

> We simply un-comment out the block of code and rerun our test.

```python
# Restore the behavior of `include_y=True`
def count_vowels(x: str, include_y: bool = False) -> int:
    vowels = set("aeiouAEIOU")
    if include_y:
        vowels.update("yY")
    return sum(1 for char in x if char in vowels)
```

```python
# confirming that we restored the proper behavior in `count_vowels`
>>> test_count_vowels_basic()
```
<!-- #endregion -->
