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
   :description: Topic: Integrated Development Environments, Difficulty: Easy, Category: Tools
   :keywords: python, introduction, IDE, PyCharm, VSCode, Jupyter, recommendation, tools
<!-- #endraw -->

# Setting Up a Development Environment
## What You Will Learn

- An IDE is a sophisticated text editor that allows you edit, run, and debug code. 
- The Python shell is an interface for typing Python code and executing it directly in your computer's terminal.
- The IPython shell is a much nicer version of the Python shell - it provides syntax highlighting, autocompletion, and other features.
- The Jupyter Notebook is a powerful tool for prototyping and experimenting with code, as well as visualizing data and writing nicely-formatted text. We will be using this throughout the course.


## Integrated Development Environments
In Section 1 of this module, we learned that a Python script is simply a text file that contains Python code. Aside from using a `.py` suffix for the filename, there is nothing that differentiates this sort of file from any other text file. That being said, it is not a good idea to use a simple text editor to write Python code (and it is a big mistake use word-processing software, like Microsoft Word, to do so). Instead we want an "integrated development environment" (IDE) that will facilitate our code-writing. 

First and foremost, a good IDE will provide a text editor that will:

- check your code for syntax errors (a misspelled function name, a reference to an undefined variable, etc)
- colorize your code so that it is easy to distinguish, for instance, numbers from character strings.
- enable you to easily look up documentation and definitions for functions that you are using.
- autocomplete the names of variables and functions as you are typing them.

An IDE also often provides debugging tools so that you can test your code; it will also typically interface with version-control software, like Git, so that you can keep track of versions of your code as you modify it. We will not discuss these useful, but more advanced features here.

## Recommended IDEs
There are many excellent IDEs that can be configured to work well with Python. Two IDEs that we endorse are:
 
### PyCharm

[PyCharm](https://www.jetbrains.com/pycharm/download) is a powerful and highly-polished IDE dedicated to developing Python code.

**Pros**

- Works well out-of-the-box.
- Long-supported by professionals and thus is very reliable.
- Highly configurable.
- Fully-featured, with an excellent debugger, context-dependent "intellisense", type-inference, and more.
- The free "community version" is extremely robust and feature-rich.
- Generally provides an extremely high-quality and responsive experience for doing Python development.

**Cons**

 - Can be resource-heavy, especially for a laptop.
 - May be overwhelming to new users (but has good documentation and tutorials).
 - Jupyter notebook support requires the premium version of PyCharm, making it inaccessible to newcomers.
 
### Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) (with the [Python extension](https://code.visualstudio.com/docs/languages/python)) is a lightweight, highly customizable IDE that works with many different languages.

Note: if you decide to use VSCode to do Python development, it is highly recommended that you install Microsoft's [PyLance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
extension.
This adds many useful features to the IDE that will make writing Python code a more delightful experience. 

**Pros**

- Lightweight and elegant.
- Completely free.
- Works with many different languages, so you only need to familiarize yourself with one IDE if you are a polyglot programmer.
- Offers a huge number of extensions that can be downloaded to add functionality to the editor; these are created by a large community of open-source developers.
- [Has native support for Jupyter notebooks](https://code.visualstudio.com/docs/python/jupyter-support), meaning that you get VSCode's intellisense, debugger, and ability to inspect variables, all in a notebook.
- Provides incredibly robust [remote coding](https://code.visualstudio.com/docs/remote/remote-overview) and [collaborative coding](https://visualstudio.microsoft.com/services/live-share/) capabilities.

**Cons**

- Configuring VSCode for Python development can have a moderate learning curve for newcomers.
- Some features, like context-aware intellisense and type-inference, are simply more polished and powerful in PyCharm.


<div class="alert alert-info">

**Takeaway**:

Integrated Development Environments (IDEs) provide powerful tools for helping you write well-formatted and typo-free code. We recommend using PyCharm Community Edition or Visual Studio Code (with the Python extension installed) for your Python IDE. 
</div>
