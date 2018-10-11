Module 2: The Essentials of Python
==================================
This module is designed to introduce you to the essential elements of Python. We will begin by studying the basic types of objects that are built-in to Python, which will enable us to work with numbers, text, and containers that can store a collection of objects. Lists, tuples, and strings all store *sequences* of objects (characters, in the case of strings), as such Python provides a common interface for working with these types; your ability to manipulate sequences of data will be a cornerstone for nearly all STEM work that you do in Python.

Having introduced Python's basic types of objects and the means for working with sequences, we will formally discuss the process of assigning variables to these objects. It is not uncommon to assign multiple variables to the same object; Python's treatment of multiple "references" to a single object will be resolved here, and in doing so we will distinguish *mutable* objects from *immutable* objects.

Armed with our growing toolkit of Python objects, and our newfound understanding of how to reference them with variables, we proceed to learn how to control the flow of logic within our code. "if", "else", and "else-if" statements are defined so that we can have branches of code be executed only if user-specified conditions are met (e.g. if a student's grade is below 65, execute code to email that student a warning). "while-loops" and "for-loops" permit us to execute blocks of code repeatedly (e.g. for each student in this list, execute the code to compute that student's average score). These so-called control-flow tools will greatly improve our ability to write useful code.

Coming off our discussion of for-loops, we take the opportunity to discuss some niceties of the Python language that arise when working with objects that are iterable (e.g. can be iterated over in a for-loop). Niceties is actually an understatement; these tricks of the trade will greatly bolster our ability to write clean, concise, and efficient code. We will pay particular attention to generator comprehension statements, which will allow us to process long sequences of data without having to hold all of the data in memory. You will be glad to have these tricks and tools in your repertoire.

Returning to a more traditional paradigm of programming languages, we will learn how to define our own functions. This will allow us to encapsulate code for reuse and invoke the code on-demand by "calling" the function that contains that code. Functions enable us to write code that is modular and to construct powerful algorithms by relying on these functions.

Finally, we will return to our initial endeavor of learning about the various types of objects that are built-in to Python, adding dictionaries, sets, and other types of collections to our inventory. Now that we are much more familiar with the language as a whole, we can concern ourselves with more nuanced, but extremely important matters. This involves discussing the efficiency of the algorithms used under the hood by its different data structures. For example, it will become clear that checking if an object is contained in a set is *much* more efficient than checking for membership in a list. Using the right tool for a given task is of manifest importance.

Although far from comprehensive, this module will acquaint you with the many of the essential elements of Python, along with the niceties that make the language easy to use. The objective here is to equip the reader with the tools needed to write clear and efficient code, that is particularly effective for data science applications. It is paramount that writing code in Python does not feel like stacking a bunch black boxes together; for this reason, a considerable amount of detail is included here. I hope that a reasonable balance has been struck such that this text is still easy to read and that its key "takeaways" are readily distilled.
  
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Module2_EssentialsOfPython/Basic_Objects.ipynb
   Module2_EssentialsOfPython/SequenceTypes.ipynb
   Module2_EssentialsOfPython/Variables_and_Assignment.ipynb
   Module2_EssentialsOfPython/Introduction.ipynb
   Module2_EssentialsOfPython/ConditionalStatements.ipynb
   Module2_EssentialsOfPython/ForLoops.ipynb
   Module2_EssentialsOfPython/Iterables.ipynb
   Module2_EssentialsOfPython/Generators_and_Comprehensions.ipynb
   Module2_EssentialsOfPython/Itertools.ipynb
   Module2_EssentialsOfPython/Functions.ipynb
   Module2_EssentialsOfPython/Scope.ipynb
   Module2_EssentialsOfPython/DataStructures.ipynb
   Module2_EssentialsOfPython/DataStructures_II_Dictionaries.ipynb
   Module2_EssentialsOfPython/DataStructures_III_Sets_and_More.ipynb
