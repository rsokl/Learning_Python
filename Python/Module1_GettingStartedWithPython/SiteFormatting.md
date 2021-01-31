---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.9.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #raw raw_mimetype="text/restructuredtext" -->
.. meta::
   :description: Topic: Overview of formatting in Python Like You Mean It, Difficulty: Easy, Category: Instructions
   :keywords: overview, formatting, background, code block, console style
<!-- #endraw -->

<!-- #region -->
# A Quick Guide to Formatting
This section provides a brief overview of the code formatting style that will be used throughout this text. You are not expected to understand the details of the code, here. This merely provides a guide for what is to come. 

Any code that is included in-line within plain text will be formatted distinctly as so: "the variable `x` was updated...". Such items will be distinguished with backticks wherever such formatting is not available. Take for example the following commented line within Python code:

```python
# the variable `x` will be updated
```

Python code will be displayed within distinct, colorized code blocks. These will typically begin with a comment, which is meant to serve as a caption that summarizes the purpose of the code block:

```python
# demonstrating a basic for-loop
cnt = 0
for i in range(10):
    cnt += 1

#`cnt` is now 10
```

The symbol `>>>` appears within code blocks to indicate "console-style" code, which distinguishes between code being entered by a user and the resulting output. The purpose of this is that it allows us to easily display the result of a computation without having to rely on calling the `print` function. For instance, the following code assigns the integer `1` to the variable `x`, and then displays the result of `x + 2`:

```python
# demonstrating the distinction of
# input and output via >>>

>>> x = 1
>>> x + 2
3
```

The code blocks throughout a given section of the text should be understood to be persistent even if there is a mix of "pure" code blocks and "console-style" code blocks. For example, a function may be defined at the beginning of a section, and then referenced throughout the rest of that section:
```python
# defining an example function
def my_func(x):
    return x**2
```

We can spend some time talking about `my_func` and then see it in action:
```python
# demonstrating `my_func`
>>> my_func(10.)
100.
```

Lastly, the input and output of an iPython console and a Jupyter notebook alike is displayed as follows:

```python
2 + 3
```

## Running Code Snippets from this Site

In PLYMI, we typically precede every code snippet with one or more commented lines.
This is useful because it makes a page more "skimmable", since the code snippets essentially come with
descriptive, self-explanatory captions.
That being said, there is a downside to this. 

Python terminals don't like having multiple comment lines precede an input-prompt.
E.g. if you paste and run the following code into a terminal

```python
# demonstrating the distinction of
# input and output via >>>

>>> x = 1
```

you will get a syntax error.
To fix this issue, simply exclude the comments when you copy this block to your clipboard.
Running

```python
>>> x = 1
```

will work without any issue.
Keep this in mind if you ever find yourself having trouble running code that you copied from this site.
<!-- #endregion -->
