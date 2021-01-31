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
   :description: Topic: Installing Python with Anaconda, Difficulty: Easy, Category: Tutorial
   :keywords: python, anaconda, instructions, environments, beginner, data science, introduction
<!-- #endraw -->

## Installing Python

Without further ado, we now provide instructions for installing Python and other useful Python libraries on your machine via the Anaconda platform. Installing the Anaconda platform will install the following:

 - Python; specifically the CPython interpreter that we discussed in the previous section.
 - A number of useful Python packages, like matplotlib, NumPy, and SciPy.
 - Jupyter, which provides an interactive "notebook" environment for prototyping code.
 - conda: a package manager that will allow you to install and update Python and additional Python packages, while handling all compatibility issues for you.
 
Note that installing Python via Anaconda will **not** break any other installations of Python that already exist on your computer. See [What did this just do to my computer?](#What-did-this-just-do-to-my-computer?) for more details.

Some of the packages provided by Anaconda, like NumPy, have been [optimized](https://docs.anaconda.com/mkl-optimizations/) and will run significantly faster than if you installed them manually.

<div class="alert alert-info">

**Takeaway**: 

"Anaconda" is a collection of the CPython interpreter and a number of very popular Python libraries for doing data science-related work. It also provides a package manager for downloading/updating Python packages, and an environment manager for maintaining independent installations of Python side-by-side.  
</div>

### Installing Anaconda

1. Navigate to [this page](https://www.anaconda.com/download/), and click the "Download" button for **Python 3**.
2. After the download is complete, begin the installation process. There will be an installation option: `Add Anaconda to the system PATH environment variable`; we advise you to **enable** this installation option (advanced users: see below for caveats).
3. Complete the 30 minute ["Getting Started"](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) tutorial to familiarize yourself with `conda`. This is very important!

You will need to know how to open a terminal (cmd.exe for Windows users) on your computer, and how to navigate between directories in the terminal. If you do not know how to do this, read a 'how-to' for whatever operating system you are using.


### What did this just do to my computer?

This created a directory called `Anaconda3` (or some variant of this) on your computer, which contains all of the files associated with the CPython interpreter, all of the modules in Python's standard library, the aforementioned 3rd party packages that come as part of the Anaconda distribution (e.g. NumPy, SciPy, Jupyter, iPython), and the `conda` package manager. It also contains the executable files for all of these applications. The default install location for Anaconda is:

- (Linux): `/home/<your_username>/Anaconda3`
- (Windows): `C:\Users\<your_username>\Anaconda3`
- (Mac): `/Users/<your_username>/Anaconda3`

If you followed the install instructions as specified above, then the Anaconda-installer also *placed this directory in your system's "path"*. Let's briefly discuss what this means. Your system's path is simply a list of directories. Whenever you execute any command in your computer's terminal, the computer will quickly search through the directories that are specified in the path for an executable with that name; *it will execute the first such executable that it finds*. Thus, by placing the `Anaconda3` directory at the beginning of your path, the Anaconda-installer has ensured that your computer will prioritize Anaconda's python executable over any other installations of Python on your computer, because it will find that executable first. 

For Linux and Mac users, it is very likely that your system already has a version of Python installed. *It is critical that you do not attempt to uninstall, remove, or change this native version of Python*. Those operating systems use their native versions of Python to perform some of their services. Those services are written such that they will directly invoke the Python executable that came with the operating system - they will not accidentally run the version of Python that came with Anaconda. At the end of the day you can simply install Anaconda without worrying about any of these details. 

**An important note for people who code in languages other than Python:**  Anaconda has its own `lib` and `bin` directories that it uses to store library files and binary files as needed. While this makes it very easy for users to install sophisticated Python packages that leverage C-libraries without having to manually build those libraries, it also means that your system will prioritize Anaconda's files before your system-level files. This can be a big problem if you work in languages other than Python.

The simple solution to this is to *not* have the Anaconda-installer include Anaconda in your path. Instead, you can create an alias that will allow you manually prepend Anaconda to your path. E.g., in Linux you can add the following alias to your `~/.bashrc` file:

```shell
alias anaconda="export PATH=/home/<your_username>/anaconda3/bin:$PATH"
```

With this alias in place, you can simply invoke the command `anaconda` in your terminal to place Anaconda at the beginning of your path for that terminal session. 

### A Brief Introduction to Conda Environments

`conda` is not only a package manager, but also a powerful environment manager. Let's take a moment to motivate a common use case for environment management before we dive into what it actually is:

>It is expected and encouraged that you work through Python Like You Mean It using the latest version of Python (Python 3.X). That being said, it is not uncommon to encounter courses and projects that require you to use Python 2.7, which is a dead version of the language. Is there a simple and sane way to switch back and forth between working in Python 3 and Python 2.7 environments? Yes! Utilizing conda environments is a perfect way to solve this problem.

Assuming that your initial installation of Anaconda contained Python 3, then your *root* (i.e. default) conda environment is that Python 3 environment. You can now create a conda environment that instead includes Python 2.7 and all of the 3rd party packages that come with Anaconda. Execute the following command in your terminal:

```shell
conda create -n py27 python=2.7 anaconda
```

Once the installation process is complete, you will be able to activate this environment, which we have named `py27`, by executing the command: 
```shell
conda activate py27
``` 

Activating an environment simply updates your system's path, swapping the directory `Anaconda3` with `Anaconda3/envs/py27` in this instance. Thus your system will now find the Python 2.7 executable and its associated libraries in its path. Note that this path change only occurs effect in *that particular terminal session*. Any other terminal session will default to the root conda environment. 

Having activated your `py27` environment, you can start a vanilla Python console, an iPython console, a Jupyter notebook, run a Python script, etc. These will now all use Python 2.7. You can also use `conda` (and `pip`) to install Python 2.7-compatible packages in this environment. As long as your path points to `Anaconda3/envs/py27` and not `Anaconda3`, it is as if this is the only version of Python that lives on your computer.

Deactivating this environment will return you to the root Python 3 environment. That is, it will switch your path back to including `Anaconda3` instead of `Anaconda3/envs/py27`. Simply invoke the command:

```shell
conda deactivate
```

And like that, conda environments give you all of the powers of a necromancer, allowing you to nimbly cross back and forth between the land of the living (Python 3) and the dead (Python 2.7).

Conda environments have more uses than simply switching back and forth between Python 3 and 2. Many people like to make a new conda environment for every major project that they work on, so that they can freely install any dependencies that are needed for that particular project, without worrying about conflicts with their other work. You should be keen on making regular use of conda environments.

It is highly recommended that you take time to read through [this tutorial on managing conda environments](https://conda.io/docs/user-guide/tasks/manage-environments.html).
