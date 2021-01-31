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
   :description: Topic: Controlling behavior with special methods, Difficulty: Medium, Category: Section
   :keywords: dunder method, special method, operator overload, repr, getitem, custom syntax, __init__
<!-- #endraw -->

<!-- #region -->
# Special Methods
In this section, we will learn about a variety of instance methods that are reserved by Python, which affect an object's high level behavior and its interactions with operators. These are known as special methods. `__init__` is an example of a special method; recall that it controls the process of creating instances of a class. Similarly, we will see that `__add__` controls the behavior of an object when it is operated on by the `+` symbol, for example. In general, the names of special methods take the form of `__<name>__`, where the two underscores preceed and succeed the name. Accordingly, special methods can also be referred to as "dunder" (double-underscore) methods. Learning to leverage special methods will enable us to design elegant and powerful classes of objects.

These methods give us complete control over the various high-level interfaces that we use to interact with objects. Let's make a simple class with nonsensical behavior to demonstrate our ability to shape how our class behaves:

```python
# Demonstrating (mis)use of special methods
class SillyClass:
    def __getitem__(self, key):
        """ Determines behavior of `self[key]` """
        return [True, False, True, False]
    
    def __pow__(self, other):
        """ Determines behavior of `self ** other` """
        return "Python Like You Mean It"
```

```python
>>> silly = SillyClass()

>>> silly[None]
[True, False, True, False]

>>> silly ** 2
'Python Like You Mean It'
```
This section is not meant to be a comprehensive treatment of special methods, which would require us to reach beyond our desired level of sophistication. The [official Python documentation](https://docs.python.org/3/reference/datamodel.html#special-method-names) provides a rigorous but somewhat inaccessible treatment of special methods. [Dive into Python 3](http://www.diveintopython3.net/special-method-names.html) has an excellent appendix on special methods. It is strongly recommended that readers consult this resource.
<!-- #endregion -->

<!-- #region -->
## String-Representations of Objects
The following methods determines how an object should be represented as a string in various contexts. For example, this text consistently utilizes the fact that passing an object to the Python console will prompt the console to print out a representation of that object as a string. That is,

```python
>>> x = list(("a", 1, True))
>>> x
['a', 1, True]
```

Under the hood, the special method `x.__repr__` is being called to obtain this string representation whenever an object is displayed in a console/notebook like this. The method returns the string `"['a', 1, True]"`, which is then printed out to the console. This is an extremely useful for creating classes whose objects can be inspected conveniently in a Python console or in a Jupyter notebook. Similarly `__str__` returns the string that will be produced when `str` is called on the object.

|Method| Signature | Explanation |
|---|---|---|
|Returns string for a printable representation of object|`__repr__(self)`|`repr(x)` invokes `x.__repr__()`, this is also invoked when an object is returned by a console|
|Returns string representation of an object|`__str__(self)`|`str(x)` invokes `x.__str__()`|
<!-- #endregion -->

A well-implemented `__repr__` method can greatly improve the convenience of working with a class. For example, let's add this method to our `ShoppingList` class that we wrote in the preceding section; the `__repr__` will create a string with our shopping items on a bulleted list with purchased items crossed out:

<!-- #region -->
```python
def strike(text):
    """ Renders string with strike-through characters through it.
        
        `strike('hello world')` -> '̶h̶e̶l̶l̶o̶ ̶w̶o̶r̶l̶d'
        
        Notes
        -----
        \u0336 is a special strike-through unicode character; it
        is not unique to Python."""
    return ''.join('\u0336{}'.format(c) for c in text)

class ShoppingList:
    def __init__(self, items):
        self._needed = set(items)
        self._purchased = set()

    def __repr__(self):
        """ Returns formatted shopping list as a string with 
            purchased items being crossed out.
            
            Returns
            -------
            str"""
        if self._needed or self._purchased:
            remaining_items = [str(i) for i in self._needed]
            purchased_items = [strike(str(i)) for i in self._purchased]
            # You wont find the • character on your keyboard. I simply 
            # googled "unicode bullet point" and copied/pasted it here. 
            return "• " + "\n• ".join(remaining_items + purchased_items)
        
    def add_new_items(self, items):  
        self._needed.update(items) 

    def mark_purchased_items(self, items):
        self._purchased.update(set(items) & self._needed)
        self._needed.difference_update(self._purchased)
```

```python
# demonstrating `ShoppingList.__repr__`
>>> l = ShoppingList(["grapes", "beets", "apples", "milk", "melon", "coffee"])
>>> l.mark_purchased_items(["grapes", "beets", "milk"])
>>> l
• melon
• apples
• coffee
• ̶g̶r̶a̶p̶e̶s
• ̶m̶i̶l̶k
• ̶b̶e̶e̶t̶s
```

See that this simple method makes it much easier for us to inspect the state of our shopping list when we are working in a console/notebook environment.
<!-- #endregion -->

## Interfacing with Mathematical Operators
The following special methods control how an object interacts with `+`, `*`, `**`, and other mathematical operators. A full listing of all the special methods used to emulate numeric types can be found [here](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)

|Method| Signature | Explanation |
|---|---|---|
|Add|`__add__(self, other)`|`x + y` invokes `x.__add__(y)`|
|Subtract|`__sub__(self, other)`|`x - y` invokes `x.__sub__(y)`|
|Multiply|`__mul__(self, other)`|`x * y` invokes `x.__mul__(y)`|
|Divide|`__truediv__(self, other)`|`x / y` invokes `x.__truediv__(y)`|
|Power|`__pow__(self, other)`|`x ** y` invokes `x.__pow__(y)`|

You may be wondering why division has the peculiar name `__truediv__`, whereas the other operators have more sensible names. This is an artifact of the transition from Python 2 to Python 3; [the default integer-division was replaced by float-division](http://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Number-Types), and thus `__div__` was replaced by `__truediv__` for the sake of 2-3 compatibility.     

<!-- #region -->
Let's give `ShoppingList` an `__add__` method so that we can merge shopping lists using the `+` operator. Rather than redefine the entire `ShoppingList` class, we can simply define this as a function and use `setattr` to set it as a method to our existing class.

```python
def __add__(self, other):
    """ Add the unpurchased and purchased items from another shopping
        list to the present one.
        
        Parameters
        ----------
        other : ShoppingList
            The shopping list whose items we will add to the present one.
        Returns
        -------
        ShoppingList
            The present shopping list, with items added to it."""
    new_list = ShoppingList([])
    # populate new_list with items from `self` and `other`
    for l in [self, other]:
        new_list.add_new_items(l._needed)

        # add purchased items to list, then mark as purchased
        new_list.add_new_items(l._purchased) 
        new_list.mark_purchased_items(l._purchased) 
    return new_list
```

```python
# set `__add__` as a method of `ShoppingList`
>>> setattr(ShoppingList, "__add__", __add__)
```

Now let's create a few shopping lists and combine them:
```python
>>> food = ShoppingList(["milk", "flour", "salt", "eggs"])
>>> food.mark_purchased_items(["flour", "salt"])

>>> office_supplies = ShoppingList(["staples", "pens", "pencils"])
>>> office_supplies.mark_purchased_items(["pencils"])

>>> clothes = ShoppingList(["t-shirts", "socks"])

# combine all three shopping lists
>>> food + office_supplies + clothes
• t-shirts
• eggs
• pens
• milk
• staples
• socks
• ̶f̶l̶o̶u̶r
• ̶s̶a̶l̶t
• ̶p̶e̶n̶c̶i̶l̶s
```
Overloading the `+` operator provides us with a sleek interface for merging multiple shopping lists in a sleek, readable way. `food + office_supplies + clothes` is equivalent to calling `(food.__add__(office_supplies)).__add__(clothes)`. It is obvious that the former expression is far superior.
<!-- #endregion -->

## Creating a Container-Like Class
The following special methods allow us to give our class a container interface, like that of a dictionary, set, or list. An exhaustive listing and discussion of these methods can be found [here](https://docs.python.org/3/reference/datamodel.html#emulating-container-types)

|Method| Signature | Explanation |
|---|---|---|
|Length|`__len__(self)`|`len(x)` invokes `x.__len__()`|
|Get Item|`__getitem__(self, key)`|`x[key]` invokes `x.__getitem__(key)`|
|Set Item|`__setitem__(self, key, item)`|`x[key] = item` invokes `x.__setitem__(key, item)`|
|Contains|`__contains__(self, item)`|`item in x` invokes `x.__contains__(item)`|
|Iterator|`__iter__(self)`|`iter(x)` invokes `x.__iter__()`|
|Next|`__next__(self)`|`next(x)` invokes `x.__next__()`|

<!-- #region -->
To get a feel for these methods, let's create class that implements most aspects of a list's interface. We will store a list as an attribute of our class to keep track of the contents, but will implement special methods that "echo" the interface of the list.

```python
class MyList:
    def __init__(self, *args):
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            # handles `MyList([1, 2, 3])
            self._data = list(args[0])
        else:
            # handles `MyList(1, 2, 3)`
            self._data = list(args)

    def __getitem__(self, index):
        out = self._data[index]
        # slicing should return a `MyList` instance
        # otherwise, the individual element should be returned as-is
        return MyList(out) if isinstance(index, slice) else out
    
    def __setitem__(self, key, value):
        self._data[key] = value

    def __len__(self): 
        return len(self._data)

    def __repr__(self): 
        """ Use the character | as the delimiter for our list"""
        # `self._data.__repr__()` returns '[ ... ]',
        # thus we can slice to get the contents of the string
        # and exclude the square-brackets, and add our own
        # delimiters in their place
        return "|" + self._data.__repr__()[1:-1] + "|"

    def __contains__(self, item): 
        return item in self._data

    def append(self, item):
        self._data.append(item)
```
<!-- #endregion -->

<!-- #region -->
Let's appreciate the rich behavior that we get out of this simple class:

```python
# MyList can accept any iterable as its
# first (and only) input argument
>>> x = MyList("hello")
>>> x
|'h', 'e', 'l', 'l', 'o'|

# MyList accepts an arbitrary number of arguments
>>> x = MyList(1, 2, 3, 4, 5)
>>> x
|1, 2, 3, 4, 5|

>>> len(x)
5

# getting an item
>>> x[0]
1

# slicing returns a MyList instance
>>> x[2:4]
|3, 4|

# setting an item
>>> x[0] = -1
>>> x
|-1, 2, 3, 4, 5|

# checking membership
>>> 10 in x
False

>>> MyList()
||
```
<!-- #endregion -->

## Links to Official Documentation

- [Special Methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [Emulating Numeric Types](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)
- [Emulating Container Types](https://docs.python.org/3/reference/datamodel.html#emulating-container-types)
