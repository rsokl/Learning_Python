**NOTE**: Some of the Jupyter notebooks in this repository contain elements that do not render properly when viewed via GitHub. For the "optimal reading experience", clone this repository and open the Jupyter notebooks locally.

**NOTE**: This content is not ready for public release. If you are reading this, then I have added you as a contributor to this project. Please do not distribute this work to others.

# Table of Contents
- [Essentials of Python, for Data Science Applications](#essentials-of-python-for-data-science-applications)
- [How To Contribute](#how-to-contribute)
- [Text Contents (Subject to Change)](#text-contents-subject-to-change)

# Essentials of Python, for Data Science Applications
The following is a collection of modules geared to introduce certain core elements of the Python programming language and the NumPy library in a concise manner. These elements are selected to include the tools and "tricks" that are most important for numerical and data science applications, while still conveying a solid understanding of the Python language itself. A specific audience that I have in mind are high school students who are interested in participating in the [Beaver Works Summer Institute](https://beaverworks.ll.mit.edu/CMS/bw/bwsi) (BWSI). That is, I want this text to be sufficient for talented/focused high school juniors to teach themselves Python over a couple of months, so that they can begin to tackle exciting, real-world problems using applied mathematics (signal processing, machine learning, and other techniques). It is important that these students have a good understanding of the tools that they are using - to merely equip them with a tool belt holding various "black boxes" would be a failure.

 There are a number of good books that cover these topics, and a massive number of blog posts in this vein as well, so why bother with this text? In short, some books cover the Python language so extensively that it is not feasible for a novice to discern what parts are "essential", and assigning selected sections for reading is too incoherent and inaccessible for students. Books and courses that focus on "Python for data science" are typically shallow in their treatment of the Python language itself. And lastly, there is the immense, ever-growing collection (dumpster fire) of "how-to" Python blog posts... look, just because you figured out how to write your first decorator doesn't mean you need to speed off to your local starbucks to write a blog post about it. 

 All in all, I like to teach, I like to write, and I like Python, so this is a fun project for me to take on. I am building off of my experience teaching the Cog*Works 2017 BWSI course (which was awesome!) to help inform this work.
 
# How To Contribute
Contributions to this project are very welcome!  Some great ways to help out are to:
- proofread (via [Pull Request](https://help.github.com/articles/creating-a-pull-request/))
- write reading comprehension exercises (create a new [issue](https://github.com/LLrsokl/BWSI_2018/issues))
- provide general feedback (create a new [issue](https://github.com/LLrsokl/BWSI_2018/issues))
- "dummy test" assignments (create a new [issue](https://github.com/LLrsokl/BWSI_2018/issues))
 
I have posted a number of "To-Do" tasks in this project's [issues](https://github.com/LLrsokl/BWSI_2018/issues) page, and I will be adding to these as this project progresses. Included are requests for proofreading and exercises. General feedback on content is also hugely valuable, so feel free to open a new issue to provide your feedback on any of the material.

[Here is a nice Markdown "cheat sheet"](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for looking up how to make tables, code-blocks, etc., in Markdown.

### Making a Pull Request
If you want to submit a change to some of the content (e.g. correcting typos), do the following:
1. Clone this repository
2. Create a new branch, appropriately named for whatever task you are performing
3. Check out your new branch and commit any changes you make to it
4. Push your branch: `git push origin <your_branch_name>` (you should have permission to do this, if you are added as a "contributor" to this project)
5. Create a [Pull Request](https://help.github.com/articles/creating-a-pull-request/)) from your branch into the master branch.

# Text Contents (Subject to Change)

Module 1: Getting Started with Python
- What is Python?
- Installing Python (via Anaconda)
- IDEs and Jupyter Notebooks
- Basics of Python

Module 2: Essentials of Python
- Boolean logic and conditional statements
- For-loops and iterators
- Generators and comprehension statements
- Itertools
- Functions
- Scope

Module 3: Introducing NumPy
- Introducing the NumPy "ND-array"
- Accessing data along multiple dimensions
- Basic array attributes
- Functions for creating NumPy arrays
- Reshaping arrays and array-traversal ordering
- Vectorized Operations

Module 4: Python's Data Structures (Incomplete)
- Lists
- Dictionaries
- Tuples
- Sets
- Python's collections module

Module 5: Advanced NumPy (Incomplete)
- Basic Indexing
- Broadcasting
- Advanced Indexing

Module 6: Object Oriented Programming (Incomplete)
- Introduction to object oriented programming
- Defining a class
- Referencing an object
- Creating an object instance
- Methods
- Special methods
- Class inheritance
