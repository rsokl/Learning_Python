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
   :description: Topic: Applications of object-oriented programming, Difficulty: Medium, Category: Section
   :keywords: summary, tutorial, python shopping list, object oriented, method, attribute
<!-- #endraw -->

# Applications of Object Oriented Programming

We have spent a considerable amount of time learning about the syntax and definitions of classes, class objects, instances, and methods. Let's take a moment to gather our knowledge and create a useful class. This will help develop a sense for the ways in which object oriented programming can be useful for us. We will try to take care to make some recommendations when one should and shouldn't define their own classes. 


## Shopping List
Let's create a shopping list class, where an instance of this class stores a list of item-names (strings) to be purchased and a list of names that have already been purchased. We will write an `__init__` function that accepts one or more strings, which will be added to the shopping list. Then, we will create methods that will allow us to:

- add new items to the shopping list
- mark items on the list as "purchased"
- remove items, purchased or not, from the list
- list the name of the items to-be purchased (in alphabetical order)
- list the name of the items have been purchased (in alphabetical order)

We do not want redundant items to be included on our shopping list - if someone enters "apples" twice, we should only list it once. Thus we will make use of [sets](http://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_III_Sets_and_More.html#The-%E2%80%9CSet%E2%80%9D-Data-Structure), which store unique elements, to store the items on our list.

Lastly, we will want our methods to accept a variable that is either a single item name (a string) or multiple item names (a list/tuple/iterable of strings). To accommodate this, if we receive a sole string as an input, we will place it in a list before carrying on. This will ensure that we are always working with an iterable containing a string.


<!-- #region -->

```python
class ShoppingList:
    def __init__(self, items):
        """ Parameters
            ----------
            items : Union[str, Iterable[str]]
                Iterable of item-names to add to shopping list"""
        if isinstance(items, str):
            items = [items]
        self._needed = set(items)
        self._purchased = set()
    
    def add_new_items(self, items):
        """ Add more items to the shopping list 
            
            Parameters
            ----------
            items : Union[str, Iterable[str]]
                Iterable of item-names to add to shopping list"""
        if isinstance(items, str):
            items = [items]
        # set.update adds elements of an iterable to a set  
        self._needed.update(items) 
        
    def mark_purchased_items(self, items):
        """ Provide names of items to mark as 'purchased' 
            
            Parameters
            ----------
            items : Union[str, Iterable[str]]"""
        if isinstance(items, str):
            items = [items]
        # only mark items as purchased that are on our list to begin with
        self._purchased.update(set(items) & self._needed)
        # remove all purchased items from our unpurchased set
        self._needed.difference_update(self._purchased)
    
    def list_purchased_items(self):
        """ Return a sorted list of the items that have been purchased"""
        return sorted(self._purchased)

    def list_unpurchased_items(self):
        """ Return a sorted list of the items still on the list"""
        return sorted(self._needed)
```

<!-- #endregion -->
<!-- #region -->
Let's create a shopping list with a few items on it:

```python
# creating a shopping list
>>> my_list = ShoppingList(["apples", "apples", "grapes", "peaches", "milk", "bread"])
>>> my_list.list_unpurchased_items()
['apples', 'bread', 'grapes', 'milk', 'peaches']
>>> my_list.list_purchased_items()
[]
```

Notice that I mistakenly placed apples on my list twice. However our use of sets under the hood handles this gracefully, reducing all redundant entries automatically. Supposing that we are carrying on with our shopping and we purchase several items, let's mark them as such.

```python
# mark items as purchased on our list
>>> my_list.mark_purchased_items(["grapes", "pineapples"])
>>> my_list.list_purchased_items()
['grapes']
>>> my_list.list_unpurchased_items()
['apples', 'bread', 'milk', 'peaches']
```

See that "grapes" were appropriately removed from our unpurchased set and added to our purchased set. Additionally, our implementation gracefully ignores our request to mark pineapples as being purchased, as pineapples weren't even on our list to begin with.

In the next section we will augment our `ShoppingList` class with some special methods to make it easier to view the items, purchased and not, on our list.
<!-- #endregion -->

<div class="alert alert-warning">

**Caution: Using Class Definitions Responsibly**

Our `ShoppingList` class' main utility is that it coordinates two sets of items for us, making the logic of tracking unpurchased and purchased items intuitive and simple. If we did not care about keeping track of purchased items, then we ought not define a class at all. We should instead just store our items in a `list` and use its methods to add and remove items. 

When possible, it is preferable to use Python's built-in types in lieu of defining a new class. Doing so will help keep your code simple, portable, and compatible with other code.

</div>
