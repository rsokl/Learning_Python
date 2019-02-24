---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.0'
      jupytext_version: 1.0.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# A Quick Guide to Formatting
This section provides a brief overview of the code formatting style that will be used throughout this text. You are not expected to understand the details of the code, here. This merely provides a guide for what is to come. 

Any code that is included in-line within plain text will be formatted distinctly as so: "the variable `x` was updated...". Such items will be distinguished with backticks wherever such formatting is not available. Take for example the following commented line within Python code:

# ```python
# the variable `x` will be updated
# ```

Python code will be displayed within distinct, colorized code blocks. These will typically begin with a comment, which is meant to serve as a caption that summarizes the purpose of the code block:

# ```python
# demonstrating a basic for-loop
cnt = 0
for i in range(10):
    cnt += 1

#`cnt` is now 10
# ```

The symbol `>>>` appears within code blocks to indicate "console-style" code, which distinguishes between code being entered by a user and the resulting output. The purpose of this is that it allows us to easily display the result of a computation without having to rely on calling the `print` function. For instance, the following code assigns the integer `1` to the variable `x`, and then displays the result of `x + 2`:

# ```python
# demonstrating the distinction of
# input and output via >>>

>>> x = 1
>>> x + 2
3
# ```

The code blocks throughout a given section of the text should be understood to be persistent even if there is a mix of "pure" code blocks and "console-style" code blocks. For example, a function may be defined at the beginning of a section, and then referenced throughout the rest of that section:
# ```python
# defining an example function
def my_func(x):
    return x**2
# ```

We can spend some time talking about `my_func` and then see it in action:
# ```python
# demonstrating `my_func`
>>> my_func(10.)
100.
# ```

Lastly, the input and output of an iPython console and a Jupyter notebook alike is displayed as follows:

```python
2 + 3
```
