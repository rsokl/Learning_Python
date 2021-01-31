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
   :description: Topic: Class instances versus objects, Difficulty: Medium, Category: Section
   :keywords: instance, class creation, init, self, isinstance
<!-- #endraw -->

<!-- #region -->
# Instances of a Class

Thus far we have learned about the syntax for defining a new class of object, specifying its name, attributes, and methods (which are attributes that are functions). Once we leave the scope of the class definition, a class object is formed - the resulting *class object* is the singular object that encapsulates our class definition. We seldom will want to pass around or manipulate this class object once it is created. Rather, we will want to use it to create individual *instances* of that class. To be more concrete, `list` is a class object (remember that "class" and "type" are synonymous) - it is the same sort of object that is produced when a `class` definition is executed. As you saw in [Module 2](http://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Lists), we can use this class object to create individual *instances* of the list class, each one containing its own sequence of items.

```python
# using the class object `list` to create list-instances
>>> list()  # create a `list`-instance that is empty
[]

>>> list((1, 2, 3))  # create a `list`-instance containing 1, 2, and 3
[1, 2, 3]

# `a` and `b` are distinct instances of the list class/type
# even though they contain the same sequence of integers
>>> a = list((1, 2, 3))
>>> b = list((1, 2, 3))
>>> a is b
False

>>> isinstance(a, list)
True

>>> isinstance(b, list)
True

# Calling the append method on `a` only affects that particular 
# list-instance.
>>> a.append(-1)
>>> a
[1, 2, 3, -1]

>>> b
[1, 2, 3]
```

Each of these instances share the common attributes `append`, `count`, `reverse`, and so on, as specified in the definition of Python's list class, which is encapsulated by the `list` class object. That being said, the specific content of any given list is an attribute of that particular list instance; that is, the content of a particular list is an *instance attribute* rather than a class attribute. Thus far, we do not have the ability to create instance-level attributes. Let's change that.

Suppose that we want to make our own `Person` class. Each person should have her/his own name, thus the name should be an instance-level attribute. We will learn to define a special initialization method that allows us to define and set instance-level attributes. In the context of `Person`, this will allow us to give each person their own name:

```python
>>> class Person:
...    def __init__(self, name):
...        self.name = name

>>> emmy = Person("Emmy")
>>> niels = Person("Niels")

>>> emmy.name
'Emmy'

>>> niels.name
'Niels'

>>> isinstance(emmy, Person)
True
```

<!-- #endregion -->

We will learn about the `__init__` method and that peculiar `self` argument momentarily. First, we will learn about creating an instance object from a class object.

<!-- #region -->
## Object Identity and Creating an Instance

Here we will learn the basic mechanism for creating an instance of a class. Consider the following trivial class definition:

```python
class Dummy:
    x = 1
```

We can use the "call" syntax on `Dummy`, `Dummy()`, to create individual instances of this class:

```python
# create an object that is an instance of our Dummy class
>>> d1 = Dummy()

>>> isinstance(d1, Dummy)
True
```

Recall that the `is` operator checks to see if two items reference the exact same object in your computer's memory. Also recall that the built-in `isinstance` function checks to see if an object is an instance of a class/type. These will help us understand the relationship between class objects, their instances, and references to objects.

```python
# `Dummy` is the class object that encapsulates
# our class definition
>>> Dummy
__main__.Dummy

# `d1` is an object that is an instance of our Dummy class.
# this instance resides at some memory address (0x2ae8f68f2e8)
>>> d1
<__main__.Dummy at 0x2ae8f68f2e8>

# d1 is not Dummy; it is an instance of Dummy
>>> d1 is Dummy 
False

>>> isinstance(d1, Dummy)
True
```
See that `Dummy` is to `d1` as `list` is to `[1, 4, "a"]`  

Let's create another instance of `Dummy`. It is important to understand that this new instance is *distinct* from the one that we already created.

```python
# `d2` is a new instance of our Dummy class.
# It resides at a distinct memory address (0x2ae8f666f60)
>>> d2 = Dummy()
>>> d2
<__main__.Dummy at 0x2ae8f666f60>

>>> d2 is d1  # `d2` and `d1` are distinct instances of `Dummy`
False

>>> isinstance(d2, Dummy)
True
```

Python's [rules for referencing objects with variables](http://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Variables_and_Assignment.html) still apply here: assigning an object to a variable, be it a class object or an instance, does not create a distinct copy of that object. The variable merely references that object, serving only as an alias for it.

```python
# `A` references `Dummy`
>>> A = Dummy

>>> A is Dummy
True

# creates an instance of `Dummy`, using `A`
>>> dummy_instance = A()  
>>> dummy_instance 
<__main__.Dummy at 0x2ae8f65fcf8>

>>> isinstance(dummy_instance, A)  # equivalent to `isinstance(dummy_instance, Dummy)`
True

# `var` references the Dummy-instance `dummy_instance`
>>> var = dummy_instance

>>> var is dummy_instance
True

# setting a new value to `var.x` is equivalent to 
# setting that value to `dummy_instance.x`
>>> var.x = 22
>>> dummy_instance.x
22

```
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Class Initialization**

Using the `Dummy` class defined above, create a list consisting of 10 *distinct* instances of this type. Write code to explicitly verify that each entry is distinct from the other, and that each entry is an instance of the `Dummy` class.

Then, create a tuple that contains a *single* instance of `Dummy` stored ten times. Write code to explicitly verify that the entries all reference the exact same object, and that each entry is an instance of the `Dummy` class.

</div>

<!-- #region -->
<div class="alert alert-info">

**Reading Comprehension: Terminology**

Given:
```python
>>> class Cat:
...     pass

>>> x = Cat
>>> y = Cat()
>>> x1 = x
>>> x2 = x()
>>> y1 = y
```

What relationship do `x` and `Cat` share?

What relationship do `y` and `Cat` share?

What relationship do `x` and `y` share?

What relationship do `x2` and `y` share?

What relationship do `y` and `y1` share?
<!-- #endregion -->

Next, identify each of the following objects as a class object or an instance (and if instance, an instance of what)

 - `"hello world"`
 - `True`
 - `int`
 - `{"a" : 22}`
 - `tuple`

</div>


Now that we know the basics of how to create an instance of a class, understand the relationship between class objects and instances, and understand the distinction between instances that are independent from one another, we can move on to learning about creating instance-level attributes for our class.

<!-- #region -->
## Defining Instance-Level Attributes: the `__init__` Method

As demonstrated in the `Person` class that we defined earlier in this section, and the `Rectangle` class that we defined in this module's introduction section, there is a special method, `__init__`, that allows us to define instance-level attributes for our class. This is a critically-important method, which we will leverage often. Note that the name of this is: "underscore-underscore-init-underscore-underscore", which can be pronounced as "dunder-init" (where "dunder" stands for double-underscore).  

Consider the slightly-modified definition of `Person`, which also includes the class-attribute `x`:

```python
class Person:
    x = 1  # this sets a class-level attribute, common to all instances of `Person`
    
    def __init__(self, name):
        """ This method is executed every time we create a new `Person` instance. 
            `self` is the object instance being created."""
        self.name = name   # set the attribute `name` to the Person-instance `self`
        
        # __init__ cannot not return any value other than `None`. Its sole purpose is to affect
        # `self`, the instance of `Person` that is being created.
```

Invoking `Person()` actually calls `__init__()` "under the hood", and any argument that we feed to `Person()` gets passed to `__init__`. Looking at our definition of `__init__` it looks like we must pass two values to this method: `self` and `name`. This first argument, `self`, actually represents the object instance of `Person` that is being created. Python will pass the appropriate object for `self` to `__init__` automatically, thus we need only worry about passing a value for `name`. 

Let's make an instance of our `Person` class, passing the string `"Kamasi"` as the name:

```python
# Creates the instance `self`,  passes it 
# and `"Kamasi"` to `Person.__init__`, and then
# returns the instance-object that was created
>>> p = Person("Kamasi")  

>>> p.name  # access the instance-attribute `name`
'Kamasi'
>>> p.x     # access the class-attribute `x`
1
```

Here is what is going on "under the hood" when we create this instance of `Person` (**this is very important**):

- Invoking `Person("Kamasi")` first creates an instance of `Person` as if there was no `__init__` method specified. The resulting object does not yet have a `name` attribute. It only has the class-level attribute `x`.
- Next, that instance of `Person` is passed to `__init__` as the argument `self`, and `"Kamasi"`, which we provided explicitly, is passed as the argument `name`. 
- With these arguments, `Person.__init__(self, "Kamasi")` executes its body of instructions. Specifically, `self.name = name` sets the attribute `name` on `self`, using the value `"Kamasi"`. 
- Having finished executing the `__init__` method, `Person("Kamasi")` resolves by returning the instance-object that was created.

We now have the ability to define and set attributes on an instance-level! Understanding this process is critical to mastering object oriented programming in Python. Let's create several `Person`-instances, all stored in a list:

```python
# creating several instances of `Person`
>>> list_of_people = [Person(n) for n in ("Fermi", "Noether", "Euler")]

>>> for person in list_of_people:
...    print(person.name)
...    print(person.x)
Fermi
1
Noether
1
Euler
1
```

Updating the class-level attribute `x` of `Person` affects all instances of `Person`:
```python
# setting a new value to the class-attribute `x`
>>> Person.x = 22 

# this affects all instances of `Person`
>>> for person in list_of_people:
...    print(person.name)
...    print(person.x)
Fermi
22
Noether
22
Euler
22
```
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info">

**Reading Comprehension: Instance Attributes**

Define a class, `Tmp`, that has three instance attributes: `x`, `y`, and `z`. `x` and `y` should be numbers that are set according to values passed to the instance creation, and `z` should be the product of these two values. 

For example:
```python
>>> tmp = Tmp(2.1, 3.0)
>>> tmp.x
2.1

>>> tmp.y
3.0

>>> tmp.z
6.3
```

</div>
<!-- #endregion -->

You should now have a grasp of how the special `__init__` method can be used to define and set instance-level attributes for your classes. Furthermore, the basic process by which invoking class instantiation produces an instance object which then automatically gets passed to `__init__` as the `self` argument, should be salient. In the following section, we will encounter three varieties of methods: instance methods, class methods, and static methods. Additionally, we will encounter even more so-called "special methods", similar to `__init__`, which can be used to more broadly specify how your class behaves and interacts with Python's operators. 


## Reading Comprehension Solutions

<!-- #region -->
**Solution: Class Initialization**

Using the `Dummy` class defined above, create a list consisting of 10 *distinct* instances of this type

```python
# will call `Dummy()` once for each iteration
>>> list_of_dummies = [Dummy() for i in range(10)] 

# note the distinct memory addresses
>>> list_of_dummies
[<__main__.Dummy at 0x1d50de89940>,
 <__main__.Dummy at 0x1d50de896d8>,
 <__main__.Dummy at 0x1d50de897b8>,
 <__main__.Dummy at 0x1d50de89a20>,
 <__main__.Dummy at 0x1d50de89ac8>,
 <__main__.Dummy at 0x1d50de89a58>,
 <__main__.Dummy at 0x1d50de899e8>,
 <__main__.Dummy at 0x1d50de89a90>,
 <__main__.Dummy at 0x1d50de89b00>,
 <__main__.Dummy at 0x1d50de89b38>]
```

Write code to explicitly verify that each entry is distinct from the other, and that each entry is an instance of the `Dummy` class.

```python
>>> from itertools import combinations
# `combinations(list_of_dummies, 2)` loops over all pairs of entries
# in `list_of_dummies`
>>> all(a is not b for a,b in combinations(list_of_dummies, 2))
True

>>> all(isinstance(a, Dummy) for a in list_of_dummies)
True
```

Create a tuple contains a *single* instance of `Dummy` ten times. Note here that we initialize `Dummy` once, and that the tuple-comprehension merely populates the tuple with that same instance ten times.  
```python
>>> dummy = Dummy()  # a single instance of `Dummy`
>>> tuple_of_dummy = tuple(dummy for i in range(10))

# note that the memory addresses are identical
>>> tuple_of_dummy
(<__main__.Dummy at 0x1d50de887b8>,
 <__main__.Dummy at 0x1d50de887b8>,
 <__main__.Dummy at 0x1d50de887b8>,
 <__main__.Dummy at 0x1d50de887b8>,
 <__main__.Dummy at 0x1d50de887b8>,
 <__main__.Dummy at 0x1d50de887b8>,
 <__main__.Dummy at 0x1d50de887b8>,
 <__main__.Dummy at 0x1d50de887b8>,
 <__main__.Dummy at 0x1d50de887b8>,
 <__main__.Dummy at 0x1d50de887b8>)
```

Write code to explicitly verify that the entries all reference the exact same object, and that each entry is an instance of the `Dummy` class.

```python
>>> all(dummy is i for i in tuple_of_dummy)
True

>>> all(isinstance(a, Dummy) for a in tuple_of_dummy)
True
```
<!-- #endregion -->

<!-- #region -->
**Reading Comprehension: Terminology**

Given:
```python
>>> class Cat:
...     pass

>>> x = Cat
>>> y = Cat()
>>> x1 = x
>>> x2 = x()
>>> y1 = y
```

What relationship do `x` and `Cat` share?: `x` and `Cat` reference the same class object.

What relationship do `y` and `Cat` share?: `y` is an instance of the `Cat` class.

What relationship do `x` and `y` share?: `x` references `Cat`, and `y` is an instance of `Cat`. Thus `y` is an instance of `x`.

What relationship do `x2` and `y` share?: They are independent instances of `Cat`

What relationship do `y` and `y1` share?: They reference the same instance of `Cat`.
<!-- #endregion -->

Identify each of the following objects as a class object or an instance (and if so, an instance of what)

 - `"hello world"`: An instance of the `str` type (a.k.a class)
 - `True`: an instance of the `bool` type
 - `int`: a class object describing integers
 - `{"a" : 22}`: an instance of the `dict` type 
 - `tuple`: a class object describing tuples

<!-- #region -->
**Reading Comprehension: Instance Attributes**

Define a class, `Tmp`, that has three instance attributes: `x`, `y`, and `z`. `x` and `y` should be numbers that are set according to values passed to the instance creation, and `z` should be the product of these two values.

```python
class Tmp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = x * y
```

```python
>>> test = Tmp(8, 5)
>>> test.x
8
>>> test.y
5
>>> test.z
40
```
<!-- #endregion -->
