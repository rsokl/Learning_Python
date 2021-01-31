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
   :description: Topic: Informal Introduction to Python, Difficulty: Easy, Category: Tutorial
   :keywords: python, installation, script, introduction, ipython, console, quick introduction
<!-- #endraw -->

# An Informal Introduction to Python

<div class="alert alert-warning">

**Before You Start This Section**: 

In the following section we will be using IPython or a Jupyter notebook to run our code.
Presently, there is an incompatibility with these programs and a Python package called `jedi`, which typically is responsible for performing auto-completions in our code (when prompted by hitting `<TAB>`, which we will be doing below).
It is really useful!

First, let's check to see if we have an incompatible version of `jedi` installed.
In your terminal (before starting a Python/IPython/Jupyter session), run
    
```
conda list
```

And look for the line that starts with `jedi`
    
```
jedi                      0.18.0
```

If you see that you have version `0.18.0` installed (as above), then you will want to downgrade it.
In the same terminal, run the following command

```
conda install jedi=0.17.2
```
You should be all set once you have followed the prompts and the installation has completed!
    
Note that you will need to repeat this process if you [create a new conda environment](https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Installing_Python.html#A-Brief-Introduction-to-Conda-Environments) with IPython/Jupter installed in it.
</div>

Now that you have the Anaconda distribution of Python installed on your machine, let's write some simple Python code! We are going to forego writing a full Python script for now, and instead make use of a convenient tool for doing quick code scratchwork. The IPython console was installed as a part of Anaconda; it will allow us to build incrementally off of snippets of code, instead of having to execute an entire script all at once. 

Let's open an IPython console. Open your terminal if you are a Mac/Linux user, or start `cmd.exe` if you are a Windows user. Now type `ipython` into the console and hit `<Enter>`. You should see the following display on your screen:

![IPython console example](attachments/ipython_0.PNG)

We can type small pieces of Python code into this console, and then simply hit `<Enter>` to have the CPython interpreter execute our code immediately within the IPython console!

Let's acquaint ourselves with Python's numbers, strings, and lists. In doing so, we will learn about the Python standard library, and how to make use of its modules, like the math module. IPython's autocompletion and documentation-display utilities will provide a nice means for exploring the library and the functionality built into the different types of Python objects. A quick glimpse at Python's strings and lists will hint at the common interface Python provides for working with sequences of objects, while highlighting some of the nice features of these all-important data types. 

## Dabbling with Numbers 
Time to execute some Python code that performs simple arithmetic. Typing `2 + 3` into the IPython console and hitting the `<ENTER>` key, you should see the following input and output in the console:

```python
2 + 3
```

This console session is persistent, meaning that we can define a variable and then reference it in our code later on within this console session. Let's define the variable `x` and assign it to the integer `10` (please follow along in the IPython console)

```python
x = 10
```

We can check the contents of `x` in this console by simply entering `x` in the next line and hitting `<ENTER>`:

```python
x
```

Now, let's use `x` in a quadratic equation $x^{2} + 2x + 3$, and compute this total.

```python
x**2 + 2*x + 3
```

Python's "standard library", the various tools and functions that come packaged as part of the core language, includes plenty of familiar mathematical functions. As a matter of organization, Python stores these mathematical functions away in a module named "math". To make use of this math module, we must import it into our code. 

```python
import math
```

Having imported it, the term `math` now refers to the math module in our code. IPython provides a nice way for us to see a list of all the functions that are provided by the math module. To utilize this, type into the console `math.` (note the trailing period) and then hit `<TAB>`. You should see this list appear:


![Displaying the contents of the math module](attachments/ipython_math.PNG)


In general, hitting `<TAB>` will cue IPython to try to autocomplete code for you. This menu displays all the valid things that you could type after `math.`. Looking at the functions starting with "s", we see `sqrt()`. This is the square root function. To see autocompletion in action, type `math.sq` and then hit `<TAB>`. You should see the code autocomplete to `math.sqrt`.

Let's use this function to compute $\sqrt{100}$:

```python
math.sqrt(100)
```

You might wonder why the result displayed as `10.0` and not simply as `10`; in Module 2 we will see that these are two different *types* of numbers in the Python language. The former is called a floating-point number, indicating the presence of its decimal point, whereas the latter is an integer. The `math.sqrt` function is defined such that it always returns its results as floating-point numbers.

In the case that we want to make frequent use of a certain function from the math module, it'd be nice to avoid having to type out the math module prefix, `math.`, repeatedly. We can accomplish this by importing an individual function from the math module. Let's import the factorial function from the math module.

```python
from math import factorial
```

We can now make use of the `factorial` function in our code. Recall that 5-factorial is $5! = 5\times 4\times 3\times 2\times 1 = 120$  

```python
factorial(5)
```

## Messing with Strings
In the context of code, written text is referred to as a string of characters, or string for short. Python is an excellent language for doing text-processing work as it provides many convenient, efficient functions for working with strings. 

To begin, we simply form a string by typing characters between quotation marks:

```python
"the cat in the hat"
```

Single quotes also work:

```python
'the dog in the sash'
```

If you use single quotes to form a string, then that string is able to contain the double-quote as a character (and vice versa):

```python
'He picked up the phone, "Hello? What do you want?" Bob was a rather impolite dude.'
```

There are designated special characters that allow us to affect the way a string is formatted when it is printed to the string. For example, if `\n` ever occurs in a string, it is treated as a single character that indicates a line-break. This will only manifest if such a string is fed to the built-in `print` function, which informs the computer to print text to a user's screen.

Let's create a string that will display as three separate lines, when printed to the screen.

```python
print("I like to talk to dogs.\nI like to talk to cats.\nWhat's my deal?")
```

Of course, strings are useful beyond merely containing text! Let's explore some ways to manipulate strings. First, we'll write a string and assign it to a variable named `sentence`:

```python
sentence = "Who would have thought that we were robots all along?"
```

Let's see how many characters are in this string by checking the "length" of this sequence of characters:

```python
len(sentence)
```

We can access the first 4 characters in the string, the last 6 characters, or a few characters in the middle by "slicing" the string:

```python
sentence[:4]
```

```python
sentence[-6:]
```

```python
sentence[5:22]
```

We can also check to see if some other string is contained within our string. Is the string `"robot"` contained within `sentence`?

```python
"robot" in sentence
```

As a quick way to check out the built-in functions that strings have available to them, we can make use of IPython's autocompletion feature once again. Type `sentence.` (including the trailing period) and then hit `<TAB>`. A menu of functions should appear as so:


![Built-in functions for a string](attachments/ipython_string.PNG)


Let's use the count function to tally the number of lowercase w's in `sentence`

```python
sentence.count('w')
```

Let's see what the replace function does. IPython provides a great utility for looking up the documentation for a function by simply putting two question marks after the function name. For example:

![Looking up documentation for a function](attachments/ipython_doc1.PNG)

Putting our newfound understanding of the string's replace function, let's replace "robot" with "computer":

```python
sentence.replace("robot", "computer")
```

## Playing with Lists
A list is one of several types of containers that are built into Python's standard library. It can hold a sequence of Python objects. We can create a list of numbers: 

```python
[-1, 1/3, 10*2, 7-1]
```

A list can contain any type of Python object; it can store a mix of numbers, strings, other lists, and much more!

```python
[1, 2, "a", 0.5, "apple and orange"]
```

You can join lists together, which is known as concatenation.

```python
[1, 2, 3] + ["a", "b", "c"]
```

Like a string, a list is sequential in nature and we can access the items in a list by specifying its position in the sequence. This is known as "indexing" the list; the index of the first item in a sequence is always 0.

```python
my_list = [10, 20, 30, 40, 50, 60]
```

```python
my_list[0]
```

```python
my_list[1]
```

Negative integers can be used to index relative to the end (right-side) of the list.

```python
my_list[-1]
```

You can change an entry in a list by assigning it to a new value.

```python
-5 in my_list
```

```python
my_list[1] = -5
```

```python
my_list
```

```python
-5 in my_list
```

We can also access multiple items in a list at once by slicing the list, like we did with the string.

```python
my_list[:3]
```

This slice can be used to update the first three entries of the list

```python
my_list[:3] = "abc"
```

```python
my_list
```

To wrap up this quick demo, let's append an new entry to the end of this list.

```python
my_list.append("moo")
```

```python
my_list
```
