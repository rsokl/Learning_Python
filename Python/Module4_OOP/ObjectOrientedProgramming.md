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

# Object Oriented Programming
Up until now, we've written functions that encapsulate code for easy re-use. We can pass data to our functions, which may operate on them and return results. However, we have been limited in the types of data we can work with. This section introduces the concept of object-oriented programming (often referred to as OOP).

An *object* bundles together data and functions. For example, a Python [List](https://docs.python.org/3/tutorial/datastructures.html) is an object. It contains data (its elements) and functions (such as `sort`, `append` and `count`).

<!-- #region -->
## Defining Objects
When we define our own objects, we will write a *class* containing data and functions. Let's start with a simple example:

```python
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height
```

We've defined a `Rectangle` object, which has two pieces of data that it keeps track of: `width` and `height`. It also has a function `get_area` that we can invoke, in much the same way we would create a list and call its `append` function. We can create a `Rectangle` in much the same way we might create a list:

```python
>>> rect = Rectangle(2, 3)
```

The `__init__` function is a special function that is executed when we create an object. Its purpose is to perform any *initialization* (hence its name) that ought to occur when the object is being created. In our case, we initialize the width and height of our `Rectangle`. Note that a parameter of our `__init__` method is `self`, which refers to the object we are creating.

We can call functions that our `Rectangle` has associated with it:

```python
>>> rect.get_area()
6
```
<!-- #endregion -->

<!-- #region -->
## Inheritance
Working with objects provides powerful abstractions and an incredible amount of code re-use. For example, let's implement a `Square` class. One way to write `Square` would be the following:

```python
class Square:
    def __init__(self, side=1):
        self.side = side
        
    def get_area(self):
        return self.side ** 2
```

However, we can take advantage of the code we've already written for `Rectangle`. We know that a square is a rectangle. Inheritance exactly follows this *is a* relationship. We can thus write our `Square` class to *inherit from* our `Rectangle` class:

```python
class Square(Rectangle):
    def __init__(self, side=1):
        super().__init__(side, side)
```

Here we're saying that a `Square` *is a* `Rectangle`. This means that `Square` *inherits* all of the data and functions inside `Rectangle`. Let's make sure:

```python
>>> my_square = Square(2)
>>> my_square.get_area()
4

>>> my_square.width
2
```

The `super()` call refers to `Square`'s *super* class, or *parent* class, which is `Rectangle`. We're calling the `__init__` method of `Rectangle`, and passing it `side` for both `width` and `height`.

In this way, we're able to re-use all the code that we already wrote for `Rectangle` so that we don't have to re-implement our `get_area` function. We can also show that our square is a rectangle, but our rectangle is not a square:

```python
>>> isinstance(my_square, Square)
True

>>> isinstance(my_square, Rectangle)
True

>>> isinstance(rect, Square)
False

>>> isinstance(rect, Rectangle)
True
```
<!-- #endregion -->

<!-- #region -->
## Operator Overloading

Recall a few operators in Python: `+`, `-`, `*`, `/`, and so on. As you know, these operators behave differently depending on context:

```python
>>> 2 + 3
5

>>> 'a' + 'b'
'ab'
```

This is because the string and integer classes have *overloaded* these operators. Observe what happens when we try to use the subtraction operator on a string:

```python
>>> 'a' - 'b'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

What's really going on here is the subtraction operator is a *function* that takes two parameters. The string class does not implement the subtraction function, so the operand type `str` is unrecognized. You can think of what's going on under the hood as this:

```
a - b => subtract(a, b)
```

Implementing an operator inside your own class is called *overloading* that operator. Here we will define a `Rational` class that keeps track of rational numbers. We'll overload several common operators so we can perform common functions on our `Rational`s.

```python
def gcd(a, b):
    ''' Greatest Common denom (GCD)
    
    Parameters
    ----------
    a : Integral
    
    b : Integral
    
    Returns
    -------
    int
        The greatest common denom of `a` and `b`.
    '''
    if a == 0:
        return b
    if b == 0:
        return a
    if a == 1:
        return 1
    if b == 1:
        return 1

    if a > 0 and b > 0:
        return gcd(b, a % b) if a >= b else gcd(a, b % a)
    if a < 0 and b < 0:
        return gcd(-a, -b)
    if a < b:
        return gcd(-a, b)
    return gcd(a, -b)

class Rational:
    ''' A rational number (a/b, where a and b are integers) '''
    def __init__(self, num=0, denom=1):
        assert denom != 0, "Cannot have zero in the denom"

        if denom < 0:
            num = -num
            denom = -denom

        factor = gcd(num, denom)
        
        self.num = num // factor
        self.denom = denom // factor
<!-- #endregion -->

<!-- #region -->
    def __add__(self, other):
        ''' Overload the `+` operator for `self` on the left '''
        num = self.num * other.denom + self.denom * other.num
        denom = self.denom * other.denom
        return Rational(num, denom)
        
    def __radd__(self, other):
        ''' Overload the `+` operator for `self` on the right '''
        return self.__add__(other)

    def __sub__(self, other):
        ''' Overload the `-` operator '''
        num = self.num * other.denom - self.denom * other.num
        denom = self.denom * other.denom
        return Rational(num, denom)
        
    def __rsub__(self, other):
        ''' Overload the `-` operator when `self` is on the right'''
        return Rational(-self.num, self.denom) + other

    def __lt__(self, other):
        ''' Overload the `<` operator '''
        return self.num * other.denom < self.denom * other.num

    def __eq__(self, other):
        ''' Overload the `==` operator '''
        return self.num == other.num and self.denom == other.denom

    def __str__(self):
        ''' Overload the `str()` operator; useful for printing '''
        return '{} / {}'.format(self.num, self.denom)

    def __repr__(self):
        ''' Overload the repr, which is used in the console:
        >>> rat = Rational(1, 2)
        >>> rat
        Rational(1, 2)
        '''
        return 'Rational({}, {})'.format(self.num, self.denom)
```

We can now create `Rational`s and operate on them:

```python
>>> a = Rational(1, 2)
>>> b = Rational(3, 4)
>>> print(a + b)
5 / 4

>>> print(a - b)
-1 / 4
```

We'll take some time now to walk through some of the details behind what we implemented. By now, the `__init__` function should look pretty familiar to you. A `Rational` object can take 0 parameters (which gives you the `Rational` $\frac{0}{1}$), 1 parameter (which gives you $\frac{a}{1}$), or 2 parameters (which gives you $\frac{a}{b}$). We've overloaded several common operators:

##### __add__
By overloading the `__add__` function, we allow the `+` operator to be used with `Rational`s. For example, we can add two `Rational`s together:

```python
>>> Rational(7, 2) + Rational(1, 7)
Rational(51, 14)
```

#### __radd__
This may look a little strage at first; especially when you see that this function just calls `__add__`. Under the hood, our `__add__` function call really looks like this:

```python
>>> r1 = Rational(1, 3)
>>> r2 = Rational(2, 5)
>>> r1.__add__(r2)  # same as r1 + r2
Rational(11, 15)
```

That call is made because `r1` appears before the `+` operator. In some cases, the operand on the left might not have a `+` operator defined that is compatible with the type of operand on the right:

```python
>>> r1 = Rational(1, 3)
>>> int(2).__add__(r1)
NotImplemented
```

Now, an `int` doesn't know anything about our `Rational` class. Python is unable to resolve the `+` operator in that scenario. However, it will then look to see whether our `Rational` class has the `__radd__` function implemented, which means "add on the right" and is called when our object is on the right of the `+`. Now, our `Rational` class doesn't have an `__radd__` function that works with an `int` so unfortunately this won't work either. However, we can still observe that this is what's happening by examining the error message:

```python
>>> 2 + Rational(1, 3)
AttributeError: 'int' object has no attribute 'denom'
```

The call fails on the line

```python
num = self.num * other.denom + self.denom * other.num
```

in our `Rational` class. Python unsuccessfully tries to resolve the `int` class's `__add__` operator, then attempts to use our `Rational`'s `__radd__`.

Since addition is commutative, we can simply call the `__add__` function from `__radd__` and things work like we expect them to. Notice that our `__rsub__` implementation is different from our `__sub__` implementation, since subtraction is not commutative. We can observe that these give different results, as they should:

```python
>>> Rational(1) - Rational(1, 3)
Rational(2, 3)

>>> Rational(1).__sub__(Rational(1, 3))
Rational(2, 3)

>>> Rational(1).__rsub__(Rational(1, 3))
Rational(-2, 3)

>>> Rational(1, 3) - Rational(1)
Raitonal(-2, 3)
```

For an exhaustive list of available operators, see [the documentation](https://docs.python.org/3/library/operator.html)
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Operator Overloading**
    
Using the `__add__` and `__sub__` implementations as a base, implement the operators:

- `*` (`__mul__`)
- `/` (`__truediv__`)
- `**` (`__pow__`)
- `<=` (`__le__`)
- `!=` (`__ne__`)
- `>` (`__gt__`)
- `>=` (`__ge__`)

for the `Rational` class.

</div>

<!-- #region -->
#### Reading Comprehension Solution

```python
class Rational:
    ''' A rational number (a/b, where a and b are integers) '''
    def __init__(self, num=0, denom=1):
        assert denom != 0, "Cannot have zero in the denom"

        if denom < 0:
            num = -num
            denom = -demoninator

        factor = gcd(num, denom)
        
        self.num = num // factor
        self.denom = denom // factor
<!-- #endregion -->

    def __add__(self, other):
        ''' Overload the `+` operator 
        
        Note that this works with non-Rationals if `self` is on the left, as in:
            >>> Rational(1, 3) + 1
            Rational(4, 3)
        but does not with `self` on the right:
            >>> 1 + Rational(1, 3)
            # error!
        '''
        num = self.num * other.denom + self.denom * other.num
        denom = self.denom * other.denom
        return Rational(num, denom)
        
    def __radd__(self, other):
        ''' Overload the `+` operator
        
        This works with non-Rationals for `self` on the right:
            >>> 1 + Rational(1, 2)
            Rational(3, 2)
        '''
        return self.__add__(other)

    def __sub__(self, other):
        ''' Overload the `-` operator '''
        num = self.num * other.denom - self.denom * other.num
        denom = self.denom * other.denom
        return Rational(num, denom)
        
    def __rsub__(self, other):
        ''' Overload the `-` operator when `self` is on the right'''
        return Rational(-self.num, self.denom) + other

    def __mul__(self, other):
        ''' Overload the `*` operator '''
        num = self.num * other.num
        denom = self.denom * other.denom
        return Rational(num, denom)
        
    def __rmul__(self, other):
        ''' Overload the `*` operator for `self` on the right '''
        return self.__mul__(other)

    def __truediv__(self, other):
        ''' Overload the `/` operator '''
        num = self.num * other.denom
        denom = self.denom * other.num
        return Rational(num, denom)
        
    def __rtruediv__(self, other):
        ''' Overload the `/` overator for `self` on the right '''
        return Rational(self.denom, self.num) * other
        
    def __pow__(self, power):
        ''' Overload the `**` operator '''
        num = self.num ** power
        denom = self.denom ** power
        return Rationa(num, denom)

    def __lt__(self, other):
        ''' Overload the `<` operator '''
        return self.num * other.denom < self.denom * other.num

    def __le__(self, other):
        ''' Overload the `<=` operator '''
        return self.num * other.denom <= self.denom * other.num

    def __eq__(self, other):
        ''' Overload the `==` operator '''
        return self.num == other.num and self.denom == other.denom

    def __ne__(self, other):
        ''' Overload the `!=` operator '''
        return not self == other

    def __gt__(self, other):
        ''' Overload the `>` operator '''
        return self.num * other.denom > self.denom * other.num

    def __ge__(self, other):
        ''' Overload the `>=` operator '''
        return self.num * other.denom >= self.denom * other.num
        
    def __str__(self):
        ''' Overload the `str()` operator; useful for printing '''
        return '{} / {}'.format(self.num, self.denom)

    def __repr__(self):
        ''' Overload the repr, which is used in the console:
        >>> rat = Rational(1, 2)
        >>> rat
        Rational(1, 2)
        '''
        return 'Rational({}, {})'.format(self.num, self.denom)
```

```python

```
