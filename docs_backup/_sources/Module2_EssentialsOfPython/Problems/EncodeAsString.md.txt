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
   :description: Topic: String Encoding Exercise, Difficulty: Medium, Category: Practice Problem
   :keywords: function, string, casting, practice problem
<!-- #endraw -->

# Encode as String
Sometimes it is very important to handle different input object types differently in a function. This problem will exercise your understanding of types, control-flow, dictionaries, and more.

>We want to encode a sequence of Python objects as a single string. The following describes the encoding method that we want to use for each type of object. Each object's transcription in should be separated by `" | "`, and the result should be one large string. 

- If the object is an integer, convert it into a string by spelling out each digit in base-10 in this format:
`142` $\rightarrow$ `one-four-two`; `-12` $\rightarrow$ `neg-one-two`. 
- If the object is a float, just append its integer part (obtained by rounding down) the same way and the string `"and float"`:
`12.324` $\rightarrow$ `one-two and float`. 
- If the object is a string, keep it as is.
- If the object is of any other type, return `'<OTHER>'`.


``` Python
# example behavior
>>> s = concat_to_str([12,-14.23,"hello", True,
...                    "Aha", 10.1, None, 5])
>>> s
'one-two | neg-one-four and float | hello | <OTHER> | Aha | one-zero and float | <OTHER> | five'
```

**Tips**: check out the `isinstance` function introduced [here](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html) for handling different types. Also, consider creating a helper function for the conversion from integer to our special-format string, since we have to do it twice. It's always good to extrapolate repeated tasks into functions. You'll also need to hard-code the conversion from each digit to its English spell-out. 

<!-- #region -->
## Solution
Our solution is broken down into three simple functions. `int_to_str` is used to map signed integers to English words. `item_to_transcript` is capable of mapping an object of any type to its string representation, in accordance with the prescription made by the problem statement. Finally, `concat_to_str` orchestrates these two helper functions, looping over each object in our input list, mapping each object to its string representation, and joining these strings with `' | '`. 

```python
def int_to_str(n):
    """ 
    Takes an integer and formats it into a special string 
        e.g. 142 -> "one-four-two"
             -12 -> "neg-one-two"
    """
    mapping = {"0": "zero", "1": "one", "2": "two", "3": "three",
               "4": "four", "5": "five", "6": "six", "7": "seven",
               "8": "eight", "9": "nine", "-": "neg"}
    return "-".join(mapping[digit] for digit in str(n))
    
def item_to_transcript(item):
    """ Any -> str """
    if isinstance(item, bool): return '<OTHER>'
    if isinstance(item, int): return int_to_str(item)
    if isinstance(item, float): return int_to_str(int(item)) + " and float"
    if isinstance(item, str): return item
    return '<OTHER>'

def concat_to_str(l):
    """ 
    Maps a list of objects to their string 
    representations concatenated together.

    Parameters
    ----------
    l: List[Any]
        Input list of objects

    Returns
    -------
    str

    Examples
    --------
    >>> concat_to_str([1, None, 'hi', 2.0])
    one | <OTHER> | hi | two and float
    """
    return " | ".join(item_to_transcript(item) for item in l)
```

We use the `str.join` function along with a generator comprehensions in a couple places in our solution. Recall that 
```python
"<hi>".join(x for x in some_iterable_of_strings)
```
is equivalent to the long-form code:
```python
out = ""
for x in some_iterable_of_strings:
    out += "<hi>" + x
``` 

`int_to_str` plays a clever trick to convert each integer, digit-by-digit, into its string form - it calls `str` on the integer. This converts the integer into a string, which is a [sequence](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/SequenceTypes.html). This permits us to access each digit of the integer and even iterate over them:

```python
# casting an integer to a string makes its
# sign and digits accessible via indexing/iteration
>>> x = str(-123)
>>> x
'-123'
>>> x[0]
'-'
>>> x[-1]
'3'
```
Thus, in total `"-".join(mapping[digit] for digit in str(n))` is responsible for casting an integer to a string, iterating over each of its digits and mapping them to their corresponding word using the [dictionary](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_II_Dictionaries.html) that we defined in the function.

`item_to_transcript` it an especially slick function. First, let's make clear the fancy use of the inline syntax here. This function:
```python
def item_to_transcript(item):
    """ Any -> str """
    if isinstance(item, bool): return '<OTHER>'
    if isinstance(item, int): return int_to_str(item)
    if isinstance(item, float): return int_to_str(int(item)) + " and float"
    if isinstance(item, str): return item
    return '<OTHER>'
```
is entirely equivalent to this function:
```python
def item_to_transcript_alt(item):
    """ Any -> str """
    if isinstance(item, bool): 
        return '<OTHER>'
    elif isinstance(item, int): 
        return int_to_str(item)
    elif isinstance(item, float): 
        return int_to_str(int(item)) + " and float"
    elif isinstance(item, str): 
        return item
    else:
        return '<OTHER>'
```
The latter uses the familiar pattern of [if-elif-else](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/ConditionalStatements.html) statements and makes for a completely satisfactory version of the function. See, however, that each of the [multiple return statements](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Functions.html#Multiple-return-Statements) in `item_to_transcript` guarantees the same logic, in that if a condition is meant a value will be returned by the function and none of its subsequent code can be visited. That is, if `item` is an integer the second if-condition will evaluate to `True` and `int_to_str(item)` will be returned, immediately expelling the point of execution from the body of the function.

Ultimately, the preference of one function over the other is merely a matter of stylistic preference. You also have likely noted the peculiar in-line `if-return` expressions. These too are only stylistic choices; 
```python
if isinstance(item, int): return int_to_str(item)
```
is no different from
```python
if isinstance(item, int): 
    return int_to_str(item)
```
The use of in-line `if-return` expressions in `item_to_transcript` does a nice job emphasizing the dictionary-like mapping behavior of the function: the form of the code suits its functionality nicely. That being said, these should generally be used sparingly. Some may call this a "cute" trick. And it is. This code is cute. I write cute code.

Finally, you may have noticed what looks like a redundancy in our code: our first `if` statement returns `'<OTHER>'` if `item` is `True` or `False`, and our final line of code returns `'<OTHER>'` if none of the preceding conditions were met (i.e. `item` is not a `bool`, `int`, `float`, or `str` type object). Why then did we not just merge our first `if` clause with this ultimate catch-all? The reason is that `True` and `False` are not only instances of the boolean type, they are also integers! `True` behaves like the integer `1` and `False` like `0`:

```python
>>> isinstance(True, int) and isinstance(True, bool)
True

>>> 3*True + True - False
4
```

Thus, had we not taken care to check for booleans up front, `True` and `False` would have been mapped to `'one'` and `'zero'`, respectively, rather than `'<OTHER>'`. This is a relatively subtle edge case to catch.
<!-- #endregion -->
