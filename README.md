# Python Like You Mean It
View this content as hosted on [Python Like You Mean It](https://www.pythonlikeyoumeanit.com/)

This repository contains the source material for the website [Python Like You Mean It](pythonlikeyoumeanit.com). The site is written primarily in [Jupytext-markdown](https://jupytext.readthedocs.io/en/latest/formats.html#jupytext-markdown) (which are eventually transformed into html using [nbsphinx](https://nbsphinx.readthedocs.io/en/0.3.4/)). A huge perk of this of this is that you simply need to be familiar with Jupyter notebooks and some [markdown syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) in order to contribute to this project!

## Asking Questions
Please feel free to post questions (or point out mistakes) about the reading by opening a [GitHub issue](https://github.com/rsokl/Learning_Python/issues). Someone from the PLYMI team will respond ASAP! Refer to [this reference](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code-and-syntax-highlighting) to see how to include python-codeblocks  in your post. This will make it much easier for us to discuss code with each other. 

## How To Contribute
Contributions to this project are very welcome!  I will be sure to credit any/all contributions (unless your want to remain anonymous). Some great ways to help out are to:
- proofread 
- add reading comprehension exercises to existing sections
- provide general feedback about the organization of the website, the consistency of the material, etc.
- create lengthier standalone problems to serve as holistic examples of how to apply the concepts presented in the reading 
- recommend new sections to be added to PLYMI
 
You can either open an issue to provide feedback or point out errors, or you can create a [pull request](https://help.github.com/articles/creating-a-pull-request/) if you want to submit new/modified materials. The other maintainers of PLYMI and I are happy to help you refine your issues and PRs, so please do not be discouraged if you are new to Git/GitHub.

I have posted a number of "To-Do" tasks in this project's [issues](https://github.com/rsokl/Learning_Python/issues) page, and I will be adding to these as this project progresses. Included are requests for proofreading and exercises. Please post within an issue if you are working on a to-do item, so multiple people don't end up working on the same task. General feedback on content is also hugely valuable, so feel free to open a new issue to provide your feedback on any of the material.

[Here is a nice Markdown "cheat sheet"](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for looking up how to make tables, code-blocks, etc., in Markdown.

### Making a Pull Request
If you want to submit a change to some of the content (e.g. correcting typos), do the following:
1. [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) this repository
2. Create a new branch, appropriately named for whatever task you are performing: `git checkout -b your_branch_name`
3. In your new branch, make the relevant changes and commit them.
4. Push your branch to your fork: `git push origin your_branch_name`
5. Create a [Pull Request](https://help.github.com/articles/creating-a-pull-request/) from your fork branch into the master branch of this repo.

# Building the Site
**Important Note: it is strongly preferred that pull requests *do not* contain changes to the HTML of this site. Rather, it is better if PRs simply contain changes to text files (.rst or .md). A site administrator (@rsokl, @davidmascharka) will be responsible for publishing the actual site-HTML**. Thus the following instructions are useful for you to view your changes as they will appear in the site, but you likely need not go through the process of committing the changes to the HTML. 

## Creating a Conda Environment From Scratch

First, create a miniconda environment. We'll call it `plymi` and will use Python 3.8

```shell
conda create -n plymi python=3.8
```

It is important that we activate the environment before proceeding

```shell
conda activate plymi
```

Next, we will install ipython, Jupyter, numpy, and matplotlib

```shell
conda install ipython jupyter notebook numpy matplotlib 
```

Next, we'll use the `conda-forge` package channel to install some critical packages for building the HTML

```shell
conda install -c conda-forge sphinx==3.4.3 nbsphinx==0.8.1 pandoc==2.1.3 jupytext=1.9.1 nbformat=5.0.8
```

Finally, we will use PyPi to install jupytext and our website's stylistic theme

```shell
pip install sphinx-rtd-theme==0.5.1
```

and install the `plymi` code base from this repo. Clone the present repository and run:

```shell
pip install .
```

Using this environment, you should now be able to run sphinx to build the html for this site from the source-code. To do this, run the following commands in your Python terminal:

```python
import plymi
plymi.convert_src_to_html("./Python") # point to the dir containing `conf.py`
```

This will convert all of the "restructured text" (.rst) files to html via `sphinx`. `jupytext` is responsible for converting the markdown (.md) files to jupyter notebooks (.ipynb) and then `nbsphinx` converts these notebooks to html.
These html files will be located in `Python/_build`. You can open the `index.html` page in your browser to view how the locally-built site looks on your computer. 

Note that, if you are introducing a new page to the site or are doing anything that would affect the site's navigation-bar, it is a good idea to delete the `_build` directory before building the html. This will make sure that sphinx fully generates the pages from scratch.

# Publishing HTML for this site
Once you have built the html and have verified that it looks good to you, navigate to the top level of the repository and run:

```python
import plymi
plymi.build_to_doc(".") # point to the top-level dir (contains both `docs/` and `docs_backup`)
```

This will back-up your current `docs` directory, and will move the html from `_builds` to `docs`. It will also ensure some essential "meta" files, `.nojekyll` and `CNAME` are present. The former is required for githubpages to build the site correctly, the latter ensures that the canonical name for the site is `pythonlikeyoumeanit.com`.




The only directories in this repository that contain html should be `docs` and `docs_backup`. **Do not commit the `_build` directory**  
