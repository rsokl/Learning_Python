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
   :description: Topic: Working with paths and files, Difficulty: Medium, Category: Section
   :keywords: open file, read file, pathlib, join directory, context manager, close file, rb, binary file, utf-8, encoding, pickle, numpy, load, archive, npy, npz, pkl, glob, read lines, write, save
<!-- #endraw -->

# Working with Files
This section will discuss the best practices for writing Python code that involves reading from and writing to files. We will learn about the built-in `pathlib.Path` object, which will help to ensure that the code that we write is portable across operating systems (OS) (e.g. Windows, MacOS, Linux). We will also be introduced to a *context manager*, `open`, which will permit us to read-from and write-to a file safely; by "safely" we mean that we will be assured that any file that we open will eventually be closed properly, so that it will not be corrupted even in the event that our code hits an error. Next, we will learn how to "glob" for files, meaning that we will learn to search for and list files whose names match specific patterns. Lastly, we will briefly encounter the `pickle` module which allows us to save (or "pickle") and load Python objects to and from your computer's file system.  

<!-- #region -->
## Working with Paths
Suppose you are writing a Jupyter notebook where you are analyzing data that is saved to your computer. You will naturally need to detail the location where your data is stored on your computer's file system so that you can load your data. Let's suppose that this notebook is in the directory `my_folder` and that there is a directory, `data`, within it, which contains some text files with your data. Thus your directory structure looks like this:

```
my_folder/
  |-notebook.ipynb
  |-data/
     |-data1.txt
     |-data2.txt
```
Now, if you are on a machine that is running Linux or MacOS, the path to `data1.txt` relative to the notebook is: `./data/data1.txt`. See that the character `/` is used as a separator used to denote subsequent directories in a path. On a Windows machine, the separator is `\`, thus the path to your data would be written as `.\data\data1.txt`. We want to write our code so that it can be utilized, without modification, across operating systems. This where Python's fantastic `pathlib` module comes in handy.

### pathlib.Path

The standard library's [pathlib module](https://docs.python.org/3/library/pathlib.html) provides a number of classes that make it easy to work with file system paths across operating systems. We will limit our discussion to the `pathlib.Path` class, which will take care of all of our most pressing needs. This class allows us to write all of our path-related code in a single way, and it will convert the path to the operating system-appropriate format for us underneath the hood.

Let's begin by creating a `Path` object that points to the directory containing the present notebook:

```python
# creating a path-object pointing to the present directory
>>> from pathlib import Path
>>> root = Path(".") # '.' means: the present directory that this code exists in
```

Because I am running this code from a Windows machine, this will form a `WindowsPath` object automatically:

```python
>>> root
WindowsPath('.')
```

If I were running on a Linux or MacOS machine, it would have formed a `PosixPath` object instead. Fortunately, we need not worry about these details as these classes handle them for us! The `Path` class has many useful methods for us to leverage. First, see that it conveniently overrides the `/` operator (by implementing a [special method](http://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html)) so that we can create a path to a subsequent directory. Let's see this in action:

```python
# creating a path to the file 'data1.txt' in the subdirectory 'data'
>>> path_to_data1 = root / "data" / "data1.txt"
>>> path_to_data1
WindowsPath('data/data1.txt')
```
See that the `/` operator, when used in conjunction with a `Path` instance, created a new path with the appropriate path-separator for the present OS. This is extremely convenient! 

Let's proceed to explore some other useful methods that `Path` provides us with. These methods enable us to inspect directories and files, create new directories, list all of the files in a directory, open files to for reading/writing, and much more. A complete listing of these methods can be found [here](https://docs.python.org/3/library/pathlib.html#methods-and-properties) and [here](https://docs.python.org/3/library/pathlib.html#methods), collectively; it is highly recommended that you take time to look through them.


```python
>>> root = Path(".")
>>> path_to_data1 = root / "data" / "data1.txt"

# Checking to see if a file or directory exists:
>>> path_to_data1.exists()
True

>>> (root / "bogus_path").exists()
False

# Getting the "absolute" path to a file or directory:
>>> path_to_data1.absolute()
WindowsPath('C:/Users/TerranceWasabi/Desktop/PLYMI/Module5_OddsAndEnds/data/data1.txt')

# Access the name of the file that the path is pointing to
>>> path_to_data1.name
'data1.txt'

# Create a new directory, named 'new_folder' within the root directory
>>> new_dir = root / "new_folder"
>>> new_dir.mkdir()

# Use 'glob' to return a generator over all files
# that match a specified pattern. E.g. get path to every
# .txt file in a directory
>>> list((root / "data").glob("*.txt"))
[WindowsPath('data/data1.txt'), WindowsPath('data/data2.txt')]

# convert a path-object to a string formatted for the present OS
>>> str(path_to_data1)
'data\\data1.txt'
```

<!-- #endregion -->

<div class="alert alert-info">

**Takeaway**: 

You should strive to utilize `pathlib.Path` whenever you are working with file system paths in your code. To reiterate - this will ensure that your code is portable across operating systems, it will help make your path handling easy to read, plus this class's methods provides a massive amount of functionality for you to leverage at your convenience.

</div>


<div class="alert alert-warning">

**Note**: 

`pathlib` was introduced in Python 3.4. Although many 3rd party libraries have updated their file-I/O utilities to accept both strings and `pathlib.Path` objects (e.g. `numpy.save` can be passed a `Path` instance to tell it where to save a numpy-array), some libraries are late to the party and will only accept strings as paths. On such occasions you can simple convert your `Path` instance to a string by calling `str` on it, and then pass the resulting string-path to the file-I/O function. This is also a friendly reminder to accomodate `pathlib.Path` objects whenever you find yourself writing your own file-I/O functions!

</div>

<!-- #region -->
## Opening Files
It is recommended that you refer to the [official Python tutorial](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) for a simple rundown of file reading and writing

Whenever you instruct your code to open a file for reading or writing, you must take care that the file ultimately is closed so that its data is not vulnerable to being modified. Python provides the `open` context manager, which is designed to ensure that a file will be closed even in the event that our code raises an error.

The following code opens the file "file1.txt" for writing:

```python
# demonstrating the use of the `open` context manager

# we will write to the file named "file1.txt", located 
# in the present directory
path_to_file = Path("file1.txt")
with open(path_to_file, mode="w") as f:
    # The indented space enters the "context" of the open file.
    # Leaving the indented space exist the context of the opened file, forcing
    # the file to be closed. This is ensured even if our code causes an error
    # within this indented block
    f.write('this is a line.\nThis is a second line.\nThis is the third line.')

# The file is closed here.
```

The syntax `with <context_manager>() as <context_variable>:` signifies the creation of a context with the object `<context_variable>` . In this case `open` is the context manager, and the variable we named `f` is the file-object that is opened within that context, which is delimited by the subsequent indented space. You can also call `open` directly from a `Path` instance:

```python
with path_to_file.open(mode="w") as f:
    f.write('this is a line.\nThis is a second line.\nThis is the third line.')
```
<!-- #endregion -->

<!-- #region -->
The complete documentation for `open` can be found [here](https://docs.python.org/3/library/functions.html#open).

### Specifying the Open-Mode
Specifying `mode='w'` indicates that we will be writing to the file anew - if the file already has any content, that content will be *erased* before being written to. The following are the available "modes" for opening a file:

|Mode| Explanation |
|---|---|
|`r`| Open the file for reading text|
|`w`| Open the file, **clearing its contents**, for writing text anew |
|`a`| Open the file to write text to end of any existing content, thus "appending" to the file |
|`x`| Open the file for writing text, failing if the file already exists |
|`+`| Open the file for both reading and writing text |

By default, these modes will read and write text utilizing the unicode (utf-8) decoding/encoding specification. That is, when you read data from your file system with `mode='r'` Python will automatically *decode* that binary data that was stored on your machine according to utf-8, which converts the binary data to written text stored as a string. Similarly, writing a string to a file in modes 'w', 'a', 'x', or '+' will presume that the string should be encoded into a binary representation (which is necessary for it to be stored as a file) according to the utf-8 encoding scheme.

You can instead force Python to read and write strictly in terms of binary data by adding a `'b'` to these modes: `'rb'`, `'wb'`, `'ab'`, `'xb'`, `'+b'`. It is important to be aware of this binary mode. For example, if you are saving a NumPy-array, you should open a file in the 'wb' or 'xb' modes so that it expects binary data to be written to it; obviously we are not saving text when we are saving a NumPy array of numbers.

```python
# saving a NumPy-array to the file 'array.npy'
>>> import numpy as np
>>> x = np.array([1, 2, 3])

# file must be open for binary-write mode
# since we are not saving text
>>> with open("array.npy", mode="wb") as f:
...     np.save(f, x)

```

### Working with the File Object
When we invoke `open` to open a file, the context manager produces an opened file object. The methods of this file object allow us to write-to and read-from the opened file (assuming that we have utilized the appropriate mode when opening it).

```python
# demonstrating the `read` method of the file object
>>> with open(path_to_file, mode="r") as var:
...     # reads the entire content of the file as a string
...     content = var.read() 

>>> content
'this is a line.\nThis is a second line.\nThis is the third line.'
>>> print(content)
this is a line.
This is a second line.
This is the third line.
```

The following summarizes some of the methods available to this file object:

- `read()`: Read the entire content of the file as a string or as bytes (depending on the open-mode)
- `readline()`: Read the next line of text from the file, including the trailing `'\n'` character
- `readlines()`: Read in the lines of text from the file, storing each line as an string in a list.
- `write(x)`: Write `x` (a string) to the file.
- `writelines(x)`: Given an iterable of strings, treat each string as a line of text to be written to the file (the inverse of `readlines`)

Also, it is important to note that the file object can be *iterated over*, and that each iteration will return an individual line of text from the file. This is the best way to read through an entire file line-by-line.
<!-- #endregion -->

<!-- #region -->
## Example: Writing and Reading a Text File

Given the following string:

```python
# recall: triple-quotes can be used to write multi-line strings
>>> some_text = """A bagel rolled down the hill.
I mean *all* the way down the hill.
A lady watched it roll.
Way to help me out."""

>>> some_text
'A bagel rolled down the hill.\nI mean *all* the way down the hill.\nA lady watched it roll.\nWay to help me out.'
```

Write that string to a file, "a_poem.txt", in the present directory:

```python
# use mode-x to ensure that we don't overwrite the file
# if it already exists
with open("a_poem.txt", mode="x") as my_open_file:
    my_open_file.write(some_text)
```

Now let's read in each line of the file and append them to the list `out`, but *only if that line starts with the letter 'A'* (just to make things a little bit more involved):

```python
with open("a_poem.txt", mode="r") as my_open_file:
    # recall: iterating over the file-object yields each line of the file
    # one line at a time
    out = [line for line in my_open_file if line.startswith("A")]
```

```python
# verify that the output is what we expect
>>> out
['A bagel rolled down the hill.\n', 'A lady watched it roll.\n']
```
<!-- #endregion -->

## Globbing for Files

There are many cases in which we may want to construct a list of files to iterate over. For example, if we have several data files, it would be useful to create a file list which we can iterate through and process in sequence. One way to do this would be to manually construct such a list of files:

```python
my_files = ['data/file1.txt', 'data/file2.txt', 'data/file3.txt', 'data/file4.txt']
```

However, this is extraordinarily tedious and prone to error, either by mis-typing a file name or forgetting a file. A much more powerful way to construct such a list of files is by file globbing. A `glob` is a set of file names matching some pattern. To glob files, we use special wildcard characters that will match all the files with a certain part of a file name. In our case, `*` will be the wildcard character we use the most - it matches any character. This is much better motivated with an example. Below, we see some globs and the types of patterns they will match:

```
# matches anything that starts with `file` and ends with `.txt` like 
# file1.txt, filefilefile.txt, file.txt, file12345.txt, ...
file*.txt 

# matches all .txt files in the 'data' directory
data/*.txt

# matches any file name
*

# matches all png image files
*.png

# matches anything that contains 'test' as part of its file name
*test*

# matches all .py files that contain 'number'
*number*.py
```

The `pathlib` module provides convenient functionality for globbing files. Once we have a `Path` object, we can simply call `glob()` on it and pass in a glob string. This will return a [generator](http://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html#Introducing-Generators) that will yield each of the globbed files.

<!-- #region -->

``` python
# glob all of the text files in the present directory
# that start with 'test' and end with '.txt'
>>> root_dir = Path('.')
>>> files = root_dir.glob('test*.txt')  # this produces a generator
<generator object Path.glob at 0x00000146CE118620>

# get a sorted list of the globbed paths
>>> sorted(files)
[PosixPath('test_0.txt'),
 PosixPath('test_1.txt'),
 PosixPath('test_apple.txt')]

# iterating over the generator directly 
>>> for file in root_dir.glob('test*.txt'):
>>>     with open(file, 'r') as f:
...         # do some processing
...         pass
```

<!-- #endregion -->

For more details on globbing, see [the documentation](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob).

<div class="alert alert-info">

**Reading Comprehension: Basic glob patterns**

Write a glob pattern for each of the following prompts

- Glob all .txt files in the directory `./files` 
- Glob all files that contain 'quirk' as part of their file name 
- Glob all file that begins with 'data'
- Glob all file that starts with the letter 'q', contains a 'w', and ends with a '.npy' extension

</div>


The `*` wildcard is not the only pattern available to us. Sometimes it can be useful to match certain subsets of characters. For example, we may only want to match file names that start with a number. With the `*` wildcard alone, that's not possible. Luckily for us, these common use-cases are also taken care of.

To match a subset of characters, we can use square brackets: `[abc]*` will match anything that starts with 'a', 'b', or 'c' and nothing else. We can also use a '-' inside our brackets to glob groups of characters. For example:

```
# matches any file that starts with a number
[0-9]*.txt

# matches any file that has a vowel in its name
*[aeiou]*

# matches any file that starts with a lowercase letter
[a-z]*
```

<div class="alert alert-info">

**Reading Comprehension: More glob patterns**

Write a glob pattern for each of the following prompts

- Any file with an odd number in its name
- All txt files that have the letters 'q' or 'z' in them

</div>

<!-- #region -->
## Saving & Loading Python Objects: pickle
Suppose that you have just populated a dictionary that is serving as a grade book for a course that you are teaching:
```python
>>> grades = {"Albert": 92, "David": 85, "Emmy": 98, "Marie": 79}  
```
How do you save this dictionary so that you can revisit these grades at a later time? Python's standard library includes the [pickle](https://docs.python.org/3/library/pickle.html) module, which provides functions for saving and loading Python objects to disk. Let's "pickle" this dictionary, saving it to the file "grades.pkl" in our present directory:

```python
import pickle

# pickling a dictionary
with open("grades.pkl", mode="wb") as opened_file:
    pickle.dump(grades, opened_file)
```
`pickle.dump` creates a serialized representation of our dictionary, which is then written to our opened file via the file object that we supplied. Note that we open the file in write-binary mode as we are writing binary data and not text data that first needs to be encoded to binary data. Also note that we use the ".pkl" suffix to indicate that the file is binary data that was written using Python's pickle protocol. Using this suffix is not necessary but is good practice.

`pickle.load` will unpickle our Python object from disk, permitting us to resume work with our grade book.

```python
# unpickling a dictionary
with open("grades.pkl", mode="rb") as opened_file:
    my_loaded_grades = pickle.load(opened_file)
```

```python
>>> my_loaded_grades
{'Albert': 92, 'David': 85, 'Emmy': 98, 'Marie': 79}
```

`pickle.dump` and `pickle.load` cover the vast majority of our object-pickling needs. A wide range of Python objects can be saved in this way, including functions that we define and instances of custom classes. Please refer to [the official documentation](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled) for a discussion of the Python objects that can and cannot be pickled. 
<!-- #endregion -->

<!-- #region -->
## Saving and Loading NumPy Arrays
NumPy provides its own functions for saving and loading arrays. Although these arrays can be pickled, it is strongly advised to leverage NumPy's file-IO functions. NumPy's standard binary file type used to store array data is known as an '.npy' file. The NumPy binary archive format, which stores multiple arrays in one file, is known as the '.npz' format.

Let's save the array `x = np.array([1, 2, 3])` to the binary file (not a text file) "my_array.npz". `numpy.save` and `numpy.load` will save and load arrays, handling all of the file opening and closing for you. Thus there is no need to use a context manager when using these functions.

```python
>>> import numpy as np
>>> x = np.array([1, 2, 3])

# save a numpy array to disk
>>> np.save("my_array.npy", x)

# load the saved array from disk
>>> y = np.load("my_array.npy")

>>> y
array([1, 2, 3])
```

We can use `numpy.savez` to save multiple arrays to a single archive file "my_archive.npz". Here we will save three arrays to the archive. We can specify the names of these arrays, via the keyword arguments that we provide, so that we can distinguish them when loading the archive.

```python
# save three arrays to a numpy archive file
a0 = np.array([1, 2, 3])
a1 = np.array([4, 5, 6])
a2 = np.array([7, 8, 9])

# we provide the keywords arguments `soil`, `crust`, and `bedrock`,
# as the names of the respective arrays in the archive.
np.savez("my_archive.npz", soil=a0, crust=a1, bedrock=a2)
```

Loading arrays from an archive is slightly more involved than loading a single array; we will want to open our archive file using a context manager and then load the arrays as we see fit. `np.load` can be used as a context manager in lieu of `open`. The file-object that it produces is our archive of numpy arrays, and it provides a dictionary-like interface for accessing these arrays:

```python
# opening the archive and accessing each array by name
with np.load("my_archive.npz") as my_archive_file:
    out0 = my_archive_file["soil"]
    out1 = my_archive_file["crust"]
    out2 = my_archive_file["bedrock"]
```
```python
>>> out0
array([1, 2, 3])
>>> out1
array([4, 5, 6])
>>> out2
array([7, 8, 9])
```
<!-- #endregion -->

## Links to Official Documentation

- [The 'pathlib' module](https://docs.python.org/3/library/pathlib.html)
- [The 'open' function](https://docs.python.org/3/library/functions.html#open)
- [Official tutorial: reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Globbing files](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob)
- [The pickle module](https://docs.python.org/3/library/pickle.html)
  - [What can and cannot be pickled?](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled)


## Reading Comprehension Solutions

**Basic glob patterns: Solutions**

- Glob all .txt files in the directory `./files` (answer: `./files/*.txt`)
- Glob all files that contain 'quirk' as part of their file name (answer: `*quirk*`)
- Glob all file that begins with 'data' (answer: `data*`)
- Glob all file that starts with the letter 'q', contains a 'w', and ends with a '.npy' extension (answer: `q*w*.npy`)

**More glob patterns: Solutions**

Write a glob pattern for each of the following prompts

- Any file with an odd number in its name (answer: `*[13579]*`)
- All txt files that have the letters 'q' or 'z' in them (answer: `*[qz]*.txt`)

