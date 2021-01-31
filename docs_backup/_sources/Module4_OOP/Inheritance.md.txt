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
   :description: Topic: Class inheritance, Difficulty: Easy, Category: Section
   :keywords: inherit, object oriented, overwrite, sub class, issubclass
<!-- #endraw -->

<!-- #region -->
# Inheritance
A final topic for us to discuss in this introduction to object oriented programming is the concept of inheritance. Working with inheritance provides powerful abstractions and elegant code re-use - it permits a class to inherit and build off of the attributes of another class.

Let's immediately consider an example of inheritance in action. Let's revisit the `Rectangle` class that we wrote in the introduction to this module.

```python
class Rectangle:
    """ A class of Python object that describes the properties of a rectangle"""
    def __init__(self, width, height, center=(0, 0)):
        self.width = width    
        self.height = height  
        self.center = center

    def __repr__(self):
        return "Rectangle(width={w}, height={h}, center={c})".format(h=self.height,
                                                                     w=self.width,
                                                                     c=self.center)

    def compute_area(self):
        return self.width * self.height
```

Now suppose that we also want to write a `Square` class, such that only a single side length need be specified to determine its size. Recognize that a square is a special type of rectangle - one whose width and height are equal. In light of this, we ought to leverage the code that we already wrote for `Rectangle`. We can do this by defining a `Square` class that is a *subclass* of `Rectangle`. This means that `Square` will *inherit* all of the attributes of `Rectangle`, including its methods. Let's proceed with writing this subclass:

```python
# Creating Square, a subclass of Rectangle
class Square(Rectangle):
    def __init__(self, side, center=(0, 0)):
        # equivalent to `Rectangle.__init__(self, side, side, center)`
        super().__init__(side, side, center)
```

Specifying `class Square(Rectangle)` signals that `Square` is a subclass of `Rectangle` and thus it will have inherited the attributes of `Rectangle`. Next, see that we overwrote the `__init__` method that `Square` inherited; instead of accepting a height and a width, `Square` should by specified by a single side length. Within this new `__init__` method, we pass in that single side length as both the width and height to `Rectangle.__init__`. `super` always refers to the "super class" or "parent class" of a given class, thus `super` is `Rectangle` here.

Having defined our subclass, we can leverage the other methods of `Rectangle` as-is. Let's see `Square` in action:

```python
# create a square of side-length 2
>>> my_square = Square(2)

# using the inherited `get_area` method
>>> my_square.get_area()
4

# a square is a rectangle with equal height/width
>>> my_square
Rectangle(width=2, height=2, center=(0.0, 0.0))

>>> my_square.width == my_square.height
True
```

<!-- #endregion -->

<!-- #region -->
The built-in `issubclass` function allows us to verify the relationship between `Square` and `Rectangle`.

```python
# `Square` and `Rectangle` are distinct classes
>>> Square is not Rectangle
True

# `Square` is a subclass of `Rectangle`
>>> issubclass(Square, Rectangle)
True

# `my_square is an both an instance of `Square` and `Rectangle`
>>> isinstance(my_square, Square)
True

>>> isinstance(my_square, Rectangle)
True
```
<!-- #endregion -->

## Summary of Inheritance

<!-- #region -->
In general, if you have a class `A`, then you can define a subclass of `A` via:

```python

class A:
    attr = 0
    
    def method(self):
        return 0
    
# `B` is a subclass of `A`
class B(A):
    # inherits `attr` and `method`
    b_attr = -2  # class attribute distinct to `B`
    
    def method(self):
        # overwrites inherited `method`
        return -1
```

`B` will have inherited all of the attributes and methods of `A`. Defining attributes and methods within the definition of `B` will overwrite those that already exist in `A`. `B` is also free to have its own distinct attributes and methods be defined, irrespective of `A`.

```python
>>> issubclass(B, A)
True

>>> A.attr
0

>>> A().method()
0

>>> B.attr
0

>>> B().method()
-1

>>> B.b_attr
-2
```
<!-- #endregion -->

We have only scratched the surface of the topic of class inheritance. That being said, this section does convey the essential functionality and utility of class inheritance. 


## Links to Official Documentation

- [Official Tutorial: Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
