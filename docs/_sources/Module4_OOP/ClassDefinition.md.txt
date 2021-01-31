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
   :description: Topic: The rules for defining classes in python, Difficulty: Easy, Category: Section
   :keywords: class definition, scope, class object, attribute, method
<!-- #endraw -->


<!-- #region -->
# Defining a New Class of Object

This section will introduce the basic syntax for defining a new class (a.k.a. type) of  Python object. Recall that the phrase `def` is used to denote the definition of a function. Similarly, `class` is used to denote the beginning of a class definition. The body of the class definition, which is the indented region below a `class` statement, is used to define the class' various **attributes**.

The following defines a new class of object, named `MyGuy`, specifying four attributes `x`, `y`, `z`, and `f`

```python
# defining a new class/type of object
class MyGuy:
    x = 1 + 2
    y = [2, 4, 6]
    z = "hi"
    
    def f():
        return 3

# leaving the indented region ends the class definition
```

Once this definition for a new class of object is executed, you can proceed to reference that object in your code. Here, we will access the various attributes of `MyGuy`.

```python
>>> MyGuy.x
3

>>> MyGuy.y
[2, 4, 6]

>>> MyGuy.z
"hi"

>>> MyGuy.f
<function __main__.MyGuy.f>
```

See that all of the attributes can be accessed using the "dot" syntax: `object.attribute_name`. The attribute `f` is a function, thus we can call it and it will evaluate as expected:

```python
# calling the attribute f
>>> MyGuy.f()
3
```

An object attribute that is also a function is referred to as a **method**. Thus `f` is a method of `MyGuy`.

`MyGuy` is the singular class object that embodies our class definition. It is akin to `list`, `str`, and `int`. We will use `MyGuy` to create objects that are *instances* of our class, in the same way that `"cat"` is an instance of `str`. More on this soon. 
<!-- #endregion -->

<div class="alert alert-info">

**Takeaway:**

The `class` expression denotes the definition of a new class of object, which entails defining the attributes of that class. An attribute can "bind" to that class other Python objects (integers, strings, lists, etc), including functions. Attributes that are functions are called *methods*. The syntax `obj.attr` is the dot syntax for "getting" the attribute named `attr` from the object named `obj`.  

</div>

<!-- #region -->
## The General Form of a Class Definition
The general form for a class definition is simply a collection of attribute definitions, which either take the form of variable assignments or function definitions, resulting in the formation of a new class of object, with its attributes and methods:

```python
class ClassName:
    """ class docstring """
    <statement-1>
    .
    .
    .
    <statement-N>
```

where each `<statement-j>` defines an attribute (e.g. `z = "hi"` defines the attribute `z`, or a function definition creates a method) for that class of object. 

Similar to function definitions, class definitions can contain effectively arbitrary Python code, and the definition has its own [scope](http://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Scope.html); however, *any* variables assigned within the class definition will be available as attributes. 

```python
# Any variable assigned within a class definition becomes
# available as an attribute for that class of object, even
# a variable defined in a for-loop becomes an attribute of 
# that class.

class Dummy:
    cnt = 0
    
    for i in range(5, 11):
        # i = 5
        # i = 6
        # ...
        # i = 10
        cnt += i
    
    # last iteration of loop assigns i = 10
    # thus i is an attribute of Dummy with value 10
```

```python
>>> Dummy.cnt  # cnt = 0 + 5 + 6 + 7 + 8 + 9 + 10
45

>>> Dummy.i
10
```
<!-- #endregion -->

<div class="alert alert-warning">

**Naming Classes of Objects:**

The convention for naming a new class/type of object is to use "camel-casing". Thus if I wanted to call my class of objects "pizza shop", I would use the name `PizzaShop`. This is in contrast to variable names, function names, and *instances* of a class object (still to be introduced), where convention dictates the use of lower-case letters and underscores in place of spaces (snake-case).  

</div>


<div class="alert alert-info">

**Reading Comprehension: Create Your Own Class of Object**

Create a definition for the class of object named `Dog`. This class should have two attributes: "name" and "speak". The "name" attribute should bind a string to the object (the name of the dog). The "speak" attribute should be a *method*, that takes a string as an input argument and returns that string with `"*woof*"` added to either end of it (e.g. `"hello"` -> `"*woof* hello *woof*"`)

</div>

<!-- #region -->
## Working with Object Attributes
Attempting to access an undefined attribute from an object will raise an `AttributeError`:

```python
>>> MyGuy.apple
AttributeError: type object 'MyGuy' has no attribute 'apple'
```

We can use built-in function `hasattr` to inspect if an object possesses a particular attribute:

```python
# demonstrating `hasattr`
>>> hasattr(MyGuy, "apple")  # MyGuy.apple is not defined
False

>>> hasattr(MyGuy, "x")      # MyGuy.x is defined
True
```

In addition to using the dot-syntax for accessing attributes, the built-in function `getattr` can be used to the same effect:

```python
# demonstrating `getattr`
>>> MyGuy.x
3

>>> getattr(MyGuy, "x")
3
```

It may be surprising to discover that new attributes can be bound (or "set") to the object *after* that class of object has already been defined. This can be done using the builtin-function `setattr`:

```python
# use `setattr` to bind the attribute `apple` to `MyGuy` 
>>> hasattr(MyGuy, "apple")  # MyGuy.apple is not defined
False

>>> setattr(MyGuy, "apple", "red")
>>> MyGuy.apple
'red'
```

Attributes can be defined/set even less formally, using a simple assignment syntax:
```python
>>> hasattr(MyGuy, "grape")  # MyGuy.grape is not defined
False

# set the attribute `grape` to `MyGuy` 
>>> MyGuy.grape = "purple"  # define and set the attribute 'grape' 
>>> MyGuy.grape
'purple'

>>> MyGuy.x = -1  # set the attribute 'x' with a new value
>>> MyGuy.x
-1
```

It may seem like the class definition is reduced to a mere formality, since attributes can be set to an object at so casually. Although Python is known for permitting this loosey-goosey style of coding, know that it is generally bad form to create attributes for a class of object outside of its designated definition.  
<!-- #endregion -->

<div class="alert alert-info">

**Takeaway:**

`hasattr`, `getattr`, and `setattr` are built-in functions that allow us to, by the name of an attribute, check to see if it exists, access its value, and set its value, respectively. Python's objects are shockingly flexible in that their attributes can be created outside of the formal space of the class definition. That being said, we should be civilized and treat the class definition as a formal contract/specification whenever possible.

</div>


## Links to Official Documentation

- [Python Tutorial: Class Objects](https://docs.python.org/3/tutorial/classes.html#class-objects)


## Reading Comprehension Solutions

<!-- #region -->
**Set Creation: Solution**
    
Create a definition for the class of object named `Dog`. This class should have two attributes: "name" and "speak". The "name" attribute should bind a string to the object (the name of the dog). The "speak" attribute should be a *method*, that takes a string as an input argument and returns that string with `"*woof*"` added to either end of it (e.g. `"hello"` -> `"*woof* hello *woof*"`)

```python
class Dog:
    name = "Charlie"
    
    def speak(input_string):
        return "*woof* " + input_string + " *woof*"
```
<!-- #endregion -->
