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
   :description: Topic: Palindrome Exercise, Difficulty: Easy, Category: Practice Problem
   :keywords: string, palindrome, practice problem
<!-- #endraw -->

<!-- #region -->
# Is Palindrome
> A palindrome is a string that reads the same from left to right and from right to left. Strings like `racecar` and `Live on time, emit no evil` are palindromes. Notice that only valid alphanumeric characters are accounted for and that palindromes are not case-sensitive. Given a string, return whether or not it is a palindrome. 

```python
# example behavior
>>> is_palindrome("Step on no pets!")
True
>>> is_palindrome("'Tis not a palindrome")
False
>>> is_palindrome("Hi, I am Mai Ih")
True
```

## Tips 
[str.isalnum](https://docs.python.org/3/library/stdtypes.html#str.isalnum) returns whether or not a string has purely alphanumeric characters (it works for single-character strings too).
```python
>>> "I love Python".isalnum()
False
>>> "IlovePython".isalnum()
True
```

Consider using this along with `str.lower` to filter out ignored characters and to normalize all of the character casing in the string before assessing whether or not it is a palindrome. 
<!-- #endregion -->

<!-- #region -->
## Solution
The simplest solution to this problem is the following, where we make use of the `str.join` function as well as slicing with a negative step:

```python
def is_palindrome(input_str):
    """ Given a string, determine if it is a palindrome.
        Whitespaces, character-casing, and non-alphanumeric  
        characters are all ignored.
        
        Parameters
        ----------
        s: str
            Input string
        
        Returns
        -------
        bool
    """
    filtered_str = "".join(c.lower() for c in input_str if c.isalnum())
    return filtered_str == filtered_str[::-1]
```

See that `(c.lower() for c in input_str if c.isalnum())` has the form of a [filtering generator comprehension](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html#Creating-your-own-generator:-generator-comprehensions). Thus, 

```python
"".join(c.lower() for c in input_str if c.isalnum())
```
is equivalent to the long-form code:

```python
filtered_str = ""
for char in input_str:
    if char.isalnum():
        filtered_str += char.lower()
```
The generator comprehension expression is not only more concise and readable, but its use of `str.join` also makes it a more efficient means for constructing a new list. Each call to `filtered_str += c.lower()` in the long-form code creates a new string in memory, whereas `str.join` forms a single string as it consumes the input iterable.

Next, [recall that](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/SequenceTypes.html#Slicing) `seq[::-1]` slices a sequence with a step of -1, which produces the sequence in *reverse order*. Thus `filtered_str == filtered_str[::-1]` allows us to compare the first character in `filtered_str` with the last and so on. This is equivalent to:

```python
is_equal = True
for i in range(len(filtered_str)//2): # recall:  5//2 -> 2, 6//2 -> 3
    if filtered_str[i] != filtered_str[-(i+1)]:
        is_equal = False
        break
```

The only downside to using slicing to perform this comparison is that it requires that a copy of `filtered_str` be created, whereas using the explicit for-loop does not. 

We must note that the performance differences pointed out here should only concern us if `is_palindrome` is potentially a performance bottleneck for our code. Although we want the reader to develop an intuition for writing efficient Python code, we discourage mangling code for the sake of premature optimization.
<!-- #endregion -->
