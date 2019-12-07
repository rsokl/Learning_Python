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

This section will introduce us to the critically-important and often-overlooked process of testing code. We will begin by taking time to understand the basic motivations behind writing tests. Next, we will study the basic anatomy of a test-function, including its nucleus: the `assert` statement. Armed with the ability to write a rudimentary test, we will welcome, with open arms, the powerful testing framework [pytest](https://docs.pytest.org/). This will inform how to structure our tests alongside our Python project that we are developing, and will allow us to incisively run our tests with the press of a single button. Furthermore, it will allow us to greatly streamline and even begin to automate some of our tests. Finally, we will take a step back to consider some strategies for writing effective tests. Among these is a methodology that is near and dear to my heart: property-based testing. This will take us down a bit of a rabbit hole, where we will find the powerful property-based testing library [Hypothesis](https://hypothesis.readthedocs.io/) waiting to greet us (adorned with the mad Hatter's cap and all).

## Why Should We Write Tests?
With great power comes great responsibility: tests help us be responsible for the code that we create and that others will (hopefully) use.

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
