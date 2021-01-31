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
   :description: Topic: The different kinds of class methods, Difficulty: Medium, Category: Section
   :keywords: instance, class method, static method, property, abstract method, class funtion
<!-- #endraw -->

<!-- #region -->
# Methods

Recall that a method is an attribute of a class that is a function. For example, "append" is a method that is defined for the `list` class and "capitalize" is a method of the `str` (string) class. 

```python
# create an instance of the `list` class/type
# and invoke the instance method `append`
>>> a = [1, 2, 3]
>>> a.append(-1)
>>> a
[1, 2, 3, -1]

# create an instance of the `str` class/type
# and invoke the instance method `capitalize`
>>> b = "moo"
>>> b.capitalize()
'Moo'
```

Here we will encounter three varieties of methods:

- instance methods
- class methods
- static methods

whose differences are relatively minor but are important to understand. The functions "append" and "capitalize" are both examples of instance methods, specifically, as they are designed to be invoked by a particular list instance and string instance, respectively.

We have already worked with the instance method `__init__`, which is special in that it is reserved by Python to be executed whenever class-initialization is invoked. Similarly, the special instance method `__add__` informs how an object interacts with the `+` operator. For example, `float.__add__` specifies that `+` will sum the values of `float` instances, whereas `list.__add__` specifies that `+` will concatenate `list` instances together. We will conclude our discussion of methods by surveying a number of these special methods - they will greatly bolster our ability to define convenient, user-friendly classes.
<!-- #endregion -->

<!-- #region -->
## Instance Methods
An *instance method* is defined whenever a function definition is specified within the body of a class. This may seem trivial but there is still a significant nuance that must be cleared up, which is that '`self`' is the defacto first-argument for any instance method. This is something that we encountered when working with `__init__`. Let's proceed naively so that we will hit a very common error, which will bring this matter to light. We begin by creating a class with an instance method that simply accepts one argument and then returns that argument unchanged:

```python
class Dummy:
    def func(x): 
        """ An instance method that returns `x` unchanged. 
            This is a bad version of this instance method!"""
        return x
```   

We can call this method from the class object `Dummy` itself, and it will behave as-expected:
```python
>>> Dummy.func(2)
2
```
but something strange happens when we try to call `func` from an instance of `Dummy`:
```python
# calling `func` from an instance of `Dummy` produces
# an unexpected error
>>> inst = Dummy()
>>> inst.func(2)
TypeError: func() takes 1 positional argument but 2 were given
```
At first glance, this error message doesn't seem to make any sense. It is indeed true that `func` only accepts one argument - we specified that it should accept the argument `x` in its function definition. How is it that `inst.func(2)` specifies *two* arguments? It seems like we are solely passing `2` to our method. Herein lies an extremely important detail:
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-warning">

**Important!**

When you call an instance method (e.g. `func`) from an instance object (e.g. `inst`), Python automatically passes that instance object as the first argument, in addition to any other arguments that were passed in by the user.

</div>

So according to this, `inst` is being passed as the argument `x` and we are attempting to pass `2` as a second argument to the method; this explains the error message complaining about passing `func` two arguments. By this logic we should be able to call `a.func()` and see that `inst` is being passed as the argument `x` - recall that `func` is defined to simply return `x` unchanged. Let's confirm this:

```python
# verifying that `inst` is being passed as the first argument 
# of the instance-method `func`

# note the memory address of the Dummy-instance `inst`
>>> inst
<__main__.Dummy at 0x284f0008da0>

# `inst.func()` automatically receives `inst` as the 
# input argument, which is then returned unchanged
>>> inst.func()
<__main__.Dummy at 0x284f0008da0>

# `inst` is indeed being passed to, and
# returned by, `func`
>>> out = inst.func()
>>> inst is out
True
```

*Note that this "under the hood" behavior only occurs when the method is being called from an instance*; this is why we didn't face this issue when invoking `func` from `Dummy` - `Dummy` is a class object, not an instance. Thus, `inst.func()` is equivalent to `Dummy.func(inst)`:

```python
>>> out = Dummy.func(inst)
>>> out is inst
True
```

In its current form, there is no way for us to pass an argument to `func` when we are calling it from an instance of `Dummy`. To solve this issue, we will refactor our definition of `func` to anticipate the passing of the instance object as the first argument.
<!-- #endregion -->

<!-- #region -->
### The `self` Argument
We will want to define our instance methods in a way that anticipates that Python will automatically pass an instance object as the first argument. Thus if we want our method to accept $N$ external argument, we should define its signature to have $N+1$ arguments, with the understanding that Python will pass the instance object as the first argument. The accepted convention is to call this first argument `self`. There is no significance to this name beyond it being the widely-adopted convention among Python users; "self" is meant to indicate that the instance object is passing itself as the first argument of the method. Consider the following example:

```python
# demonstrate the use of `self` in instance arguments
class Number:
    def __init__(self, value):
        self.value = value
    
    def add(self, new_value):
        return self.value + new_value
```

```python
# calls __init__, setting self.value = 4.0
>>> x = Number(4.0)

# `x` gets passed to `self`
>>> x.add(2.0)
6.0

# Calling the instance method from the class object.
# We must explicitly pass an object to `self`
>>> Number.add(x, 2.0)
6.0
```

Note the utility of having `self` be automatically passed in as an argument to both `__init__` and `add`. An instance method is meant to have access to the instance object that is calling it - when you call `capitalize` from a string instance, it is obvious that you want to capitalize *that* specific string. It would be tedious and redundant if Python did not manage that automatically. 

Next, we will see that we can also define class-methods, which automatically have *class objects* get passed as their first arguments, and static methods, which do not have any objects passed to them under the hood.
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Invoking Instance Methods**

Rewrite `Dummy` so that its instance method `func` accepts two arguments: the instance object that Python automatically passes and the argument `x`, which we want `func` to return unchanged. Create an instance of `Dummy` and call `func` from this instance and pass it the string `"hi"`, what will be returned? What will happen if you try to call `Dummy.func("hi")`? Why? How can we modify this call from `Dummy` itself so that the method will work as desired? 

</div>

<!-- #region -->
## Class Methods
A class method is similar to an instance method, but it has a *class object* passed as its first argument. Recall that, when an instance method is called from an instance object, that instance object is automatically passed as the first argument to the method. By contrast, when a *class method* is called from a either a class object or an instance object, the class object is automatically passed as the first argument to the method. Instead of calling this first argument `self`, the convention is to name it `cls`.

To define a class method you must *decorate* the method definition with a special built-in decorator `classmethod`. We have not discussed decorators. Suffice it to know that this simply "tags" the method, so that Python knows to treat it like a class method instead of an instance method. The following demonstrates this decoration process:

```python
class Dummy:
    
    @classmethod
    def class_func(cls):
        """ A class method defined to simply 
            return `cls` unchanged"""
        return cls
```

```python
# `Dummy` gets passed as `cls` automatically.
#  We defined `class_func` to return `cls` unchanged
>>> Dummy.class_func()
__main__.Dummy

# `Dummy.class_func()` returns `Dummy`
>>> out = Dummy.class_func()
>>> out is Dummy
True

# `Dummy` gets passed as `cls` automatically
# even when `class_func` is called from an instance
>>> inst = Dummy()
>>> inst.class_func()
>>> inst.class_func()
__main__.Dummy
```
<!-- #endregion -->

<!-- #region -->
`dict.fromkeys` is an example of a class method that takes in an iterable, and returns a dictionary whose keys are the elements of that iterable, and whose values all default to `None`.

```python
>>> dict.fromkeys("abcd", 2.3)
{'a': 2.3, 'b': 2.3, 'c': 2.3, 'd': 2.3}
```

It is sensible that this is a class method rather than an instance method, as the method creates a brand new dictionary from scratch. It need only have access to the `dict` object (i.e. the `cls` argument) so that it can construct the dictionary. The following is what an implementation of `fromkeys` could look like, were we to define `dict` ourselves: 

```python
class dict:
    # assume all other dictionary methods are defined here
    @classmethod
    def fromkeys(cls, iterable, value=None):
        """ Creates a dictionary whose keys are the elements of `iterable`. All 
        keys map to `value`.
        
        Parameters
        ----------
        iterable: Iterable[Hashable]
            An iterable of valid dictionary keys (i.e. any object that is hashable).
        
        value : Optional[Any]
            The value that all of the keys will map to. Defaults to `None`.
        
        Returns
        -------
        dict """
        new_dict = cls()  # equivalent to `dict()`: creates a new dictionary instance
        for key in iterable:
            new_dict[key] = value
        return new_dict
```
<!-- #endregion -->

<!-- #region -->
## Static Methods
A static method is simply a method whose arguments must all be passed explicitly by the user. That is, Python doesn't pass anything to a static method automatically. The built-in decorator `staticmethod` is used to distinguish a method as being static rather than an instance method.

```python
class Dummy:

    @staticmethod
    def static_func():
        """ A static method defined to always returns 
            the string `'hi'`"""
        return 'hi'
```

```python
# A static method can be called from a class object
# or an instance object; nothing gets passed to it 
# automatically.
>>> Dummy.static_func()
'hi'

>>> inst = Dummy()
>>> inst.static_func()
'hi'
```
<!-- #endregion -->

## Reading Comprehension Solutions

<!-- #region -->
**Invoking Instance Methods: Solution**

Rewrite `Dummy` so that its instance method `func` accepts two arguments: the instance object that Python automatically passes and the argument `x`, which we want `func` to return unchanged.

> We will rewite func to accept an argument called 'self', which will accept the instance object that is passed "under the hood" , and 'x'. As you will see in the reading, the name argument 'self' is simply used by convention.  

```python
class Dummy:
    def func(self, x): 
        return x
```

Create an instance of `Dummy` and call `func` from this instance and pass it the string `"hi"`.

```python
>>> inst = Dummy()
>>> inst.func("hi")  # `inst` is passed to the argument `self`
'hi'
```

What will happen if you try to call `Dummy.func("hi")`? Why?

> This will raise an error, which complains that func expects two arguments, and that we have only passed it one. Indeed, we will have only passed it the object "hi" and nothing else. Dummy is a class object, not an instance object. Thus Python does not do anything special "under the hood" when we call Dummy.func. We must pass something to the self argument. Because this particular method doesn't do anything with self, we can just pass it None, or any other object, really.

```python
# Dummy.func("hi") would raise an error
>>> Dummy(None, "hi")
'hi'
```
<!-- #endregion -->
