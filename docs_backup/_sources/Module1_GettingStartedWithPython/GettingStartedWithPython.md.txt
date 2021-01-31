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
   :description: Topic: Basic description of the Python programming language, Difficulty: Easy, Category: Background
   :keywords: python, install, basics, scripts, interpreter, foundations, versions
<!-- #endraw -->

<!-- #region -->
# Introducing the Python Programming Language

In this section we will learn

 - What Python is.
 - What it means to "install Python" on your computer.
 - How one writes and executes Python code.

## What is Python?
**Python is a programming language**. That is, it provides us with a strict set of grammatical rules that correspond to well-defined instructions that a computer will obey. The tremendous value of this is that we can write text documents that are relatively simple and intuitive for humans to read, and yet can inform the computer to perform precise operations. Python **code** is simply text that conforms to the Python language.

For example, the following text obeys the rules of the Python language:

```python
x = 2 + 3
print('2 + 3 = {}'.format(x))
```

According to the Python language, it will instruct the computer to:

 - compute 2 + 3
 - assign the resulting value (5) to a variable `x`, in memory
 - access the value of `x`, and print to the computer's screen: '2 + 3 = 5'

<!-- #endregion -->

<!-- #region -->
An example of code that **does not** obey Python's rules is:

```python
x = 2 ~ 3
```
because character `~` has no meaning in the Python language when it is placed between two integers.

To "learn Python" thus entails learning the grammatical rules specified by the Python language, and the computer instuctions that they map to. Additionally, you will want to familiarize yourself with many of the convenient tools that are "pre-written" and come with the Python language; they are part of the so-called standard library.

Given this basic understanding of what the Python programming language is, we now want to know how to use our Python code to send instructions to the computer. The most basic way of doing this is to:

 - Write a Python "script": a text file containing Python code.
 - Pass this text file to a **Python interpreter**, which will instruct the computer to carry out the operations described by the code.

<!-- #endregion -->

## Python Scripts
You can save the the valid code from the preceding section in a text file using a simple text editor, and *voilà* you have written a **Python script**: a text file containing Python code. It is standard to save this text file using the suffix `.py` (e.g. `my_code.py`), rather than the familiar `.txt` (e.g. `my_text.txt`). There is nothing special about the `.py` suffix; it simply helps differentiate files that contain Python code from run-of-the-mill text files, which contain plain English.

Although you can use simple text editors to write Python scripts (e.g. notepad (Win), TextEdit (Mac), nano (Linux)), there are much more sophisticated editors that provide an "integrated development environment" (IDE) for writing code. An IDE, configured to support Python, will warn you if you have written code that violates Python's grammar rules, similar to the way word processing software warns you if you have made a spelling mistake. More on IDEs in a later section. 

<div class="alert alert-warning">

**WARNING**: 

Do not use word processing programs, like Microsoft Word, to write code. They will "silently" change the characters written in your file, such as the type of quotation marks being used. This will cause errors in your code. 
</div>

Now that you have a Python script, how do you get the computer to read it and follow its instructions? You will need to install a **Python interpreter** on your computer to accomplish this. This is what people mean, whether they know it or not, when they tell you to "install Python" on your computer.


## What is a Python Interpreter and What Does it Mean to "Install Python"?

A Python interpreter is any computer program that is capable of doing the following:

 - Read in a text file (e.g. `my_code.py`).
 - Parse the text and determine if it obeys the rules of the Python language (the interpreter will raise an error if the rules are not obeyed).
 - Translate the parsed text into instructions, according to the Python language's specifications.
 - Instruct the computer to carry out the tasks.
 - As a whole, a Python script is executed from top-to-bottom by the interpreter.

The first Python interpeter was written in the programming language C, and is known as CPython. Accordingly, **the CPython interpreter is the official interpreter of the Python language**. Any new rules/features that are introduced to the Python language are guaranteed be implemented in the [CPython code base](https://github.com/python/cpython).

<div class="alert alert-warning">

**Note**: 

Python interpreters have been in written in programming languages other than C, like in Java (Jython) and Go (Grumpy). These are not guaranteed to be up-to-date with the latest specifications of the Python language, and are rarely used in comparison to the CPython interpreter.
</div>

<div class="alert alert-warning">

**About Installing Python**: 

Do not download and install Python from python.org. There isn't anything wrong with this, but a later section will provide you with explicit instructions for installing Python on your machine. 

</div>

If you "install Python on your computer" from [python.org](https://www.python.org/downloads/release/python-363/), you are essentially downloading an executable program onto your machine that operates as a Python interpreter. On Windows, for instance, this program is called `python.exe`. This program is the result of the aforementioned CPython code, and it is capable of performing the all of the tasks of a Python interpreter. Additionally, you are downloading a large suite of useful tools and functions that you can utilize in your code. This is known as the Python standard library; take a moment to look over its contents [here](https://docs.python.org/3/library/index.html#the-python-standard-library). 

Once you have a Python interpreter installed on your machine, using it to execute a Python script is quite simple. Assume for the sake of simplicity that the `python` interpreter program and `my_script.py` are in the same directory (a.k.a 'folder') in your computer. Then, in a terminal (`cmd.exe` for Windows) you can execute the following command:

```shell
python my_script.py
```

this will instruct the Python interpreter program `python` to read your text file `my_script.py`, ensure that your code obeys all of the grammatical rules specified by the Python language, and then send instructions to your computer in accordance with the code that it reads. If your script simply contains the code `print("hello world")`, then the text `hello world` will appear in your terminal window, as expected.

In practice, you will be able to simply execute `python my_script.py` in any directory, and your computer will know where to look to find the `python` program. This will be set up during the installation process.

It may be confusing to think that the Python language is interpreted by using a program written in another language. How, then, is that language interpreted? The answer, in the case of CPython, is that C code need not be interpreted; programs exist for Windows, Mac, and Linux that can translate C code directly into machine instructions. 

<!-- #region -->
## Why Python?

Python has become a hugely popular programming language. In fact, it is likely the [most popular introductory language at universities](https://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-u-s-universities/fulltext). First and foremost, its syntax is designed to be intuitive and readable. For example, the following Python code sums the numbers 0-9, and prints the result:
```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(a))
```

This can be reproduced by the following C++ code, which is arguably less-intuitive:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<int> a = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::cout << std::accumulate(a.begin(), a.end(), 0) << std::endl;
}
```

As such, Python is a language that is conducive to rapidly prototyping and testing code. Additionally, it is open-sourced: it is free to use, anyone can participate in improving/maintaining the language, and many people create new libraries that add tremendous functionality to the language. Thus, Python has become exceptionally popular especially among scientists, engineers, and other researchers.

We will be relying heavily on Python and a library for doing optimized numerical computations, called NumPy, throughout this course.
<!-- #endregion -->

<!-- #region -->
## Understanding Different Versions of Python

New versions of Python come out periodically, bringing new features and fixes. 
You can keep track of what's new in Python by [bookmarking and checking this page every few months](https://docs.python.org/3/whatsnew/index.html).
As we take on coding projects in Python, whether it be for work, school, or a personal hobby, it is important that we remain aware of
the ways in which the language is changing, and that we take care to write code that will remain functional in the future.

All Python version numbers use the `A.B.C` format, in accordance with [semantic versioning](https://semver.org/). 
The three numbers denote major releases, minor releases, and patches.
For example, as of writing this, the current release of Python is version `3.9.1`.

The first number denotes major releases to the language. 
When a major release comes out, it means that older code will not necessarily work with the new release, and vice versa. 
For example, the following code worked in Python 2 but no longer works because the `xrange` function was removed from the language
upon the release of Python 3.

```python
# `xrange` was a frequently-used function in Python 2, but
# was removed from the language in Python 3 in favor of `range`. 
# Thus the following code does not work in any version of Python 3.
count = 0
for i in xrange(10):
    count = count + 1
```

The most current major release is Python 3; Python 2 is no longer supported by any bug or security fixes and should not be used.
All releases in the near future will be improvements to Python 3, and thus they will come in the form of minor releases and patches.

The second number denotes a minor release. 
A minor release will be compatible with code from the preceding release, but it might add new features to the language that are not backwards-compatible.
For example, Python 3.6 introduced [formatted string literals](https://docs.python.org/3/whatsnew/3.6.html#pep-498-formatted-string-literals), which are 
commonly referred to as "f-strings".
Thus as of Python 3.6 you could write code like

```python
# Python 3.6 introduced the "f-string" feature, which is not
# backwards compatible with Python 3.5
>>> f"one plus two is {1 + 2}"
'one plus two is 3'
```

but this code would not run in Python 3.5.X.

The third and final number denotes a patch, which generally means bug fixes and performance improvements. 
All code within the same minor release will run on all other patches within that minor release
For example, all Python 3.7.8 code is compatible with a Python 3.7.1 interpreter, and vice versa. 
Patches are released fairly often, and their changes only occur 'under the hood'.
[Here is a list of changes](https://docs.python.org/3/whatsnew/changelog.html#python-3-9-1-final) were introduced by the patch level increment from Python 3.9.0 to Python 3.9.1;
few of these would affect our day-to-day experience with using Python (which isn't to say that they aren't important!).

In simpler terms, major releases are neither backward nor forward compatible.
Minor releases are forward compatible but not necessarily fully backward compatible, and patches are both forward and backward compatible.

<!-- #endregion -->

## Summary

- Python is a programming language - it provides us with a simple set of grammatical rules that allow us to write human-readable text, which can be translated unambiguously to instruct a computer to perform tasks.
- Python code is text that conforms to the Python language.
- A Python script is a text file containing Python code. Traditionally such a file will be saved using the suffix `.py`.
- A Python interpreter is a program that is capable of reading and parsing a text file, and translating the code into machine instructions, as specified by the Python language.
- To "install Python" onto you machine boils down to saving a functioning Python interpreter onto your machine.
- The official Python interpreter is a program written in the language C, and is known as the CPython interpreter.
- The "standard library" is a large collection of tools and functions that comes packaged with the CPython interpreter.
