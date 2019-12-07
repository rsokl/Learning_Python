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
As we become capable Python users, we will naturally find ourselves moving away from writing short, trivial programs in favor of creating useful projects. That being said, as our code becomes more complex, how will we know that it all works as expected? Obviously, one will naturally try out their project to verify its behavior. But how often will we take the time to test our projects this way; will it be every time we touch our code? Furthermore, will we run the same test every time, or are there several conditions under which we will run our code? These questions only scratch the surface of the various considerations at play. Here, we will distill the essentials process of writing tests for Python code.

With great power comes great responsibility: tests help us be responsible creators.

```python
x += 2

x+= 4
```
<!-- #endregion -->

```python

```
