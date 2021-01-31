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
   :description: Topic: Introducing object oriented programming in python, Difficulty: Easy, Category: Section
   :keywords: class, type, creation, definition, intro, overview, basics, meaning
<!-- #endraw -->

<!-- #region -->
# Introduction to Object Oriented Programming

Our first foray into the essentials of Python introduced us to the [basic object types: numbers, strings, and lists](http://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html). Likewise, our discussion of NumPy was centered around the [N-dimensional array](http://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/IntroducingTheNDarray.html). These types of objects are distinguished in large part by the different functions that are bound to them. Functions bound to objects are known as **methods**. For example, where a string possesses methods designed to manipulate its sequence of characters, a NumPy array possesses methods for operating on the numerical data bound to that array.

```python
# Different types of objects can possess different methods 

>>> string = "hello world"
>>> string.capitalize() # use the string-method `capitalize`
'Hello world'

>>> import numpy as np
>>> array = np.array([[0, 1, 2],
...                   [3, 4, 5]])
>>> array.sum()  # use the array-method `sum`
15
```
<!-- #endregion -->

<!-- #region -->
More generally, an object can possess data, known as **attributes**, which summarize information about that object. For example, the array-attributes `ndim` and `shape` provide information about the indexing-layout of that array's numerical data.

```python
# accessing an object's attributes
>>> array.ndim
2
>>> array.shape
(2, 3)
```
<!-- #endregion -->

<!-- #region -->
In this module, we will learn to define our own, customized object types with distinct collections of attributes and methods. In this way, we will be using Python as an "objected oriented" programming language; this will greatly expand our capabilities as Python users, and deepen our understanding of the language itself.

As a sneak peek example, let's create our own class of objects known as `Rectangle`:

```python
class Rectangle:
    """ A Python object that describes the properties of a rectangle """
    def __init__(self, width, height, center=(0.0, 0.0)):
        """ Sets the attributes of a particular instance of `Rectangle`.

            Parameters
            ----------
            width : float
                The x-extent of this rectangle instance.

            height : float
                The y-extent of this rectangle instance.

            center : Tuple[float, float], optional (default=(0, 0))
                The (x, y) position of this rectangle's center"""
        self.width = width    
        self.height = height  
        self.center = center
    
    def __repr__(self):
        """ Returns a string to be used as a printable representation 
            of a given rectangle."""
        return "Rectangle(width={w}, height={h}, center={c})".format(h=self.height,
                                                                     w=self.width,
                                                                     c=self.center)

    def compute_area(self):
        """ Returns the area of this rectangle 

            Returns
            -------
            float"""
        return self.width * self.height

    def compute_corners(self):
        """ Computes the (x, y) corner-locations of this rectangle, starting with the
            'top-right' corner, and proceeding clockwise. 

            Returns
            -------
            List[Tuple[float, float], Tuple[float, float], Tuple[float, float], Tuple[float, float]]"""
        cx, cy = self.center
        dx = self.width / 2.0
        dy = self.height / 2.0
        return [(cx + x, cy + y) for x,y in ((dx, dy), (dx, -dy), (-dx, -dy), (-dx, dy))]
```

An instance of this `Rectangle` class is an individual rectangle whose *attributes* include its width, height, and center-location. Additionally, we can use the rectangle's *methods* (its attributes that are functions) to compute its area and the locations of its corners. 
<!-- #endregion -->

<!-- #region -->
```python
# create a rectangle of width 4, height 10, centered at (0, 0)
# here __init__ is executed and the width/height/center attributes are set
>>> rect1 = Rectangle(4, 10)  

# the __repr__ method defines how a rectangle instance will be displayed here
# in the console
>>> rect1  
Rectangle(width=4, height=10, center=(0, 0))

# compute the area for this particular rectangle
>>> rect1.compute_area()      
40

# compute the corner-locations of this rectangle
>>> rect1.compute_corners()   
[(2.0, 5.0), (2.0, -5.0), (-2.0, -5.0), (-2.0, 5.0)]
```
<!-- #endregion -->

Just like any other Python object that we have encountered, we can put our `Rectangle`s in lists, store them as values in dictionaries, pass them to functions, reference them with multiple variables, and so on.

Popular STEM, data analysis, and machine learning Python libraries rely heavily on the ability to define custom classes of Python objects. For example, [pandas](https://pandas.pydata.org/) defines a spreadsheet-like `DataFrame` class; [PyTorch](https://pytorch.org/), [MXNet](https://mxnet.incubator.apache.org/), and [TensorFlow](https://www.tensorflow.org/) each define tensor classes that are capable of [automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation), which is critically important for training neural networks. Understanding Python's class system will greatly improve your ability to leverage libraries like these (Shameless plug: refer to [MyGrad](https://mygrad.readthedocs.io) if you are interested in seeing a simple pure-Python/NumPy implementation of an auto-differentiation library). 

Moving forward, we will discuss the essential *class definition*, which will permit us to  define our own class (a.k.a. type) of object. Next, we will learn about creating distinct *instances* of a given object type and about defining methods. This will lead to our first encounter with *special methods*, which enable us to affect how our object type behaves with Python's various operators. For example, we can define how the `+` operator interacts with our objects. Lastly, we will briefly discuss the concept of class inheritance. 

<div class="alert alert-info">

**Takeaway:**

The goal of this module is to understand how to define and utilize our own class of Python objects. This will greatly mature our understanding of Python as an object-oriented language, and will expand our ability to fully leverage all of Python's features.  

</div>

## Class vs Type: An Important Note on Terminology
Before proceeding any further, it is worthwhile to draw our attention to the fact that the terms "type" and "class" are practically synonymous in Python. Thus far, we have only encountered the term "type" to distinguish objects from one another, e.g. `1` belongs to the type `int` and `"cat"` belongs to the type `str`. However, we will soon study *class* definitions for making new types objects, and soon introduce functions like `issubclass` into our lexicon. That being said, know that *class* and *type* mean the same thing! There are historical reasons for the coexistence of these two terms, but [since Python 2.2](https://www.python.org/download/releases/2.2/descrintro/) concepts of type and class have been unified.

In practice, people tend to reserve the word "type" to refer to built-in types (e.g. `int` and `str`) and "class" to refer to user-defined types. Again, in the modern versions of Python, these terms carry no practical distinction.


<div class="alert alert-info">

**Takeaway:**

The terms "type" and "class" are synonymous; they both refer to the encapsulating definition of a specific type/class of Python object, with all of its attributes. Although they are not treated synonymously within the Python language - we will write class definitions, not type definitions, and we will use `type` to inspect an object and not `class` - these distinctions are merely relics of versions of Python long passed.

</div>


## Links to Official Documentation

- [Python Tutorial: A First Look at Classes](https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes)
