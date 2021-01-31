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
   :description: Topic: Control flow with for-loops and while-loops, Difficulty: Easy, Category: Section
   :keywords: for-loop, while-loop, break, control flow, basic programming
<!-- #endraw -->

# For-Loops and While-Loops
In this section, we will introduce the essential "for-loop" control flow paradigm along with the formal definition of an "iterable". The utility of these items cannot be understated. Moving forward, you will likely find use for these concepts in nearly every piece of Python code that you write!


<div class="alert alert-warning">

**Note**: 

There are reading-comprehension exercises included throughout the text. These are meant to help you put your reading to practice. Solutions for the exercises are included at the bottom of this page.
</div>

<!-- #region -->
## For-Loops
A "for-loop" allows you to iterate over a collection of items, and execute a block of code once for each iteration. For example, the following code will sum up all the positive numbers in a tuple:
```python
total = 0
for num in (-22.0, 3.5, 8.1, -10, 0.5):
    if num > 0:
        total = total + num
```
The general syntax for a "for-loop" is:

```
for <var> in <iterable>:
    block of code
```

Where `<var>` is any valid variable-identifier and `<iterable>` is any **iterable**. We will discuss iterables more formally in the next section; suffice it to know that every sequence-type object is an iterable. The `for`statement must end in a colon character, and the body the for-loop is [whitespace-delimited](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Introduction.html#Python-Uses-Whitespace-to-Delimit-Scope).

The for-loop behaves as follows:

- Request the next member of the iterable.
- If the iterable is empty, exit the for-loop without running its body.
- If the iterable did produce a member, assign that member to `<var>` (if `<var>` was not previously defined, it becomes defined). 
- Execute the enclosed body of code.
- Go back to the first step.

To be concrete, let's consider the example:
```python
# demonstrating a basic for-loop
total = 0
for item in [1, 3, 5]:
    total = total + item

print(total)  # `total` has the value 1 + 3 + 5 = 9
# `item` is still defined here, and holds the value 5
```

This code will perform the following steps:

1. Define the variable `total`, and assign it the value `0`
2. Iterate on the list, producing value `1`, define the variable `item` and assign it the value `1`
3. Assign `total` the value `0 + 1`
4. Iterate on the list, producing the value `3` and assigning it to `item`
5. Assign `total` the value `1 + 3`
6. Iterate on the list, producing the value `5` and assigning it to `item`
7. Assign `total` the value `4 + 5`
8. Iterate on the list. Having reached its end, a `StopIteration` signal it raised by the list, and the for-loop sequence is exited.
9. Print the value of `total` (9)

#### Potential Pitfall
Note that the variable `item` will persist after the for-loop block is exited. It will reference the last value from the for-loop iteration (in this case `item` has the value 5). That being said, *you should not write code that depends on the iterate-variable, outside of the context of the for-loop*. In the case that you try to loop over an *empty* iterable, the iterate-variable is never defined:

```python
for x in []:         # the iterable is empty - the iterate-variable `x` will not be defined
    print("Hello?")  # this code is never executed
print(x)             # raises an error because `x` was never defined
```

Because we are attempting to iterate over an empty list, `StopIteration` is raised immediately - before the variable `x` is even defined. Thus the code enclosed within the for-loop is never reached, and the subsequent `print(x)` statement will raise a `NameError`, because `x` was never defined!
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: A basic for-loop**

Using a for-loop and an if-statement, print each letter in the string `"abcdefghij"`, if that letter is a vowel.

</div>

<!-- #region -->
## While-Loops
A "while-loop" allows you to repeat a block of code until a condition is no longer true:

```
while <condition>:
    block of code
```

Where `<condition>` is an expression that returns `True` or `False`, or is any object on which `bool` can be called. The "body" of the while-loop is the code indented beneath the while-loop statement.

The while-loop behaves as follows:

- Call `bool(<condition>)` and execute the indented block of code if `True` is returned. Otherwise, "exit" the while-loop, skipping past the indented code.
- If the indented block code is executed, go back to the first step.

To be concrete, let's consider the example:
```python
# demonstrating a basic while-loop
total = 0
while total < 2:
    total += 1  # equivalent to: `total = total + 1`

print(total)  # `total` has the value 2
```

This code will perform the following steps:

1. Define the variable `total`, and assign it the value `0`
2. Evaluate `0 < 2`, which returns `True`: enter the enclosed code-block
3. Execute the code block: assign `total` the value `0 + 1`
4. Evaluate `1 < 2`, which returns `True`: enter the enclosed code-block
5. Execute the code block: assign `total` the value `1 + 1`
6. Evaluate `2 < 2`, which returns `False`: *skip* the enclosed code-block
7. Print the value of `total` (2)

Note that if we started off with `total = 3`, the condition-expression `3 < 2` would evaluate to `False` outright, and the indented body of code would never be reached.

<div class="alert alert-warning">

**Warning!** 

It is possible to write a while-loop such that its conditional statement is always True, in which case your code will run ceaselessly! If this ever happens to you in a Jupyter notebook, either interrupt or restart your kernel.
</div>
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: A basic while-loop**

Given a list of nonzero, positive numbers, `x`, append the sum of that list to the end of it. Do this until the last value in `x` is at least 100. Use a while-loop. 

If you start with `x = [1]`, then by the end of your while-loop `x` should be `[1, 1, 2, 4, 8, 16, 32, 64, 128]`.

</div>

<!-- #region -->
## `break`, `continue`, & `else` clauses on loops
The `continue` and `break` statements can be used within the bodies of both for-loops and while-loops. They provide added means for "short-circuiting" or prematurely exiting a given loop, respectively.

Encountering `break` within a given loop causes that loop to be exited immediately:

```ipython
# breaking out of a loop early
>>> for item in [1, 2, 3, 4, 5]:
...     if item == 3:
...         print(item, " ...break!")
...         break
...     print(item, " ...next iteration")
```
```
1  ...next iteration
2  ...next iteration
3  ...break!
```

An `else` clause can be added to the end of any loop. The body of this else-statement will be executed *only if the loop was not exited via a `break` statement*.

```ipython
# including an else-clause at the end of the loop
>>> for item in [2, 4, 6]:
...     if item == 3:
...         print(item, " ...break!")
...         break
...     print(item, " ...next iteration")
... else:
...     print("if you are reading this, then the loop completed without a 'break'")
```
```
2  ...next iteration
4  ...next iteration
6  ...next iteration
if you are reading this, then the loop completed without a 'break'
```

The `continue` statement, when encountered within a loop, causes the loop-statement to be revisited immediately.
```python
# demonstrating a `continue` statement in a loop
>>> x = 1
>>> while x < 4:
...     print("x = ", x, ">> enter loop-body <<")
...     if x == 2:
...         print("x = ", x, " continue...back to the top of the loop!")
...         x += 1
...         continue
...     x += 1
...     print("--reached end of loop-body--")
```
```
x =  1 >> enter loop-body <<
--reached end of loop-body--
x =  2 >> enter loop-body <<
x =  2  continue...back to the top of the loop!
x =  3 >> enter loop-body <<
--reached end of loop-body--
```
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: conducting flow in a loop**

Loop over a list of integers repeatedly, summing up all of its even values, and adding the content to a total. Repeat this process until the the total exceeds 100, or if you have looped over the list more than 50 times. Print the total only if it exceeds 100.

</div>


## Links to Official Documentation

- ['for' statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
- ['while' statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
- ['break', 'continue', and 'else' clauses](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
- ['pass' statment](https://docs.python.org/3/tutorial/controlflow.html#pass-statements)


## Reading Comprehension Exercise Solutions:

<!-- #region -->
**A basic for-loop: Solution**
```python
for letter in "abcdefghij":
    if letter in "aeiou":
        print(letter)
```

<!-- #endregion -->

<!-- #region -->
**A basic while-loop: Solution**
```python
while x[-1] < 100:
    x.append(sum(x))
```
<!-- #endregion -->

<!-- #region -->
**Conducting flow in a loop: Solution**

```python
x = [3, 4, 1, 2, 8, 10, -3, 0]
num_loop = 0
total = 0

while total < 100:
    for item in x:
        # return to for-loop if 
        # `item` is odd-valued
        if item % 2 == 1:
            continue
        else:
            total += item
    num_loop += 1
    
    # break from while-loop if 
    # more than 50 items tallied
    if 50 < num_loop:
        break
else:
    print(total)
```

<!-- #endregion -->
