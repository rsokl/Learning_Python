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

<!-- #region -->
# Testing Your Code

This section will introduce us to the critically-important and often-overlooked process of testing code. 
We will begin by considering the basic motivations behind writing tests.
Next, we will study the basic anatomy of a test-function, including its nucleus: the `assert` statement.
Armed with the ability to write a rudimentary test, we will welcome, with open arms, the powerful testing framework [pytest](https://docs.pytest.org/).
This will inform how to structure our tests alongside our Python project that we are developing, and will allow us to incisively run our tests with the press of a single button.
Furthermore, it will allow us to greatly streamline and even begin to automate some of our tests.
Finally, we will take a step back to consider some strategies for writing effective tests.
Among these is a methodology that is near and dear to my heart: property-based testing.
This will take us down a bit of a rabbit hole, where we will find the powerful property-based testing library [Hypothesis](https://hypothesis.readthedocs.io/) waiting to greet us (adorned with the mad Hatter's cap and all).

<!-- #endregion -->

<!-- #region -->
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
  > Perhaps, in the interim, new versions of your project's dependencies, like PyTorch or Matplotlib, were released and have incompatibilities with our project.
  > And perhaps we can't even _remember_ all of the ways in which our project is supposed to work.
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

<!-- #endregion -->

<!-- #region -->
## SCRATCH
As we become capable Python users, we will naturally find ourselves moving away from writing short, trivial programs in favor of creating useful and increasingly-sophisticated projects. It is only naturally try using your code to verify its behavior. You may even devise several scenarios to exercise your project. Clearly this sort of testing need no justification; it is a ubiquitous practice among coders. Less obvious are the major pitfalls associated with this highly-manual means of testing. 

Let's consider some of the pitfalls of casual, manual tests. To do so, consider the following unfortunate scenario: you carefully run your code through several test scenarios and see that 

- 
Fortunately, it is exceedingly easy to convert this casual and flawed testing workflow to one that is far more powerful and efficient.


```python
x += 2

x+= 4
```
<!-- #endregion -->

```python

```
