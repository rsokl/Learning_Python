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
   :description: Topic: Brief review of object oriented programming, Difficulty: Easy, Category: Tutorial
   :keywords: class definition, simple, examples, overview, init, initialize, type, object
<!-- #endraw -->

<!-- #region -->
## A Brief Summary of Terms and Concepts

Let's do a quick rundown of some of the concepts and terms discussed thus far.  The following code is a *class definition*, which specifies the *attributes* of objects that belong to the class/type `Example`.

```python
class Example:
    a = (1, 2, 3)
    
    def __init__(self):
        self.b = "apple"
```

Once executed, this code produces the *class object* `Example`, which encapsulates the above definition and can be used to create objects that are instances of this class/type. `Example.a` and `Example.__init__` are both attributes of this class. `Example.__init__` is more specifically a special method, which is automatically invoked whenever an instance of this class is created. 

The following code creates an *instance* of `Example`, assigning that instance to the variable `ex`. This means that the object belongs to the type (a.k.a class) `Example`.

```python
>>> ex = Example()

>>> Example.a
(1, 2, 3)

>>> ex.a
(1, 2, 3)

>>> isinstance(ex, Example)
True

>>> type(ex)
__main__.Example
```

Upon this instantiation, the instance-level attribute `b` was defined via execution of the `__init__` method, wherein Python passed the instance object being created as the argument `self` to the method. Thus `b` is an *instance-level* attribute, which is not possessed by `Example` itself.

```python
>>> Example.b
AttributeError: type object 'Example' has no attribute 'b'

>>> ex.b
'apple'
```

<!-- #endregion -->
