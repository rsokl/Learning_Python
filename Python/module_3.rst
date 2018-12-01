Module 3: The Essentials of NumPy
==================================
NumPy is the reason why Python stands among the ranks of R, Matlab, and Julia, as one of the most popular languages for doing STEM-related technical computing. It is a 3rd party library (i.e. it is not part of Python's standard library) that facilitates numerical computing in Python by providing users with a versatile N-dimensional array object for storing data, and powerful mathematical functions for operating on those arrays of numbers. NumPy implements its features in ways that are highly optimized, via a process known as vectorization, that enables a degree of computational efficiency that is otherwise unachievable by the Python language.

The impact that NumPy has had on the landscape of technical computing in Python is hard to overstate. Whether you are plotting data in matplotlib, analyzing tabular data via `pandas <https://pandas.pydata.org>`_ and `xarray <https://xarray.pydata.org/en/stable>`_, using `OpenCV <https://opencv.org>`_ for image and video processing, doing astrophysics research with the help of `astropy <www.astropy.org>`_, or trying out machine learning with `Scikit-Learn <https://scikit-learn.org/stable/index.html>`_ and `MyGrad <https://mygrad.readthedocs.io >`_, you are using Python libraries that bare the indelible mark of NumPy. At their core, each of these libraries depend on NumPy's N-dimensional array and its efficient vectorization capabilities. It also fundamentally impacts the designs of these libraries and the way that they interface with their users. Thus, one cannot leverage these tools effectively, and cannot do STEM work in Python in general, without having a solid foundation in NumPy.

Thus, this module presents to us the essentials of NumPy. We will first define what the term dimensionality means and will develop an intuition for what zero, one, two, and N-dimensional arrays are, and why they are invaluable for data science applications. Next, we will discuss the ambiguities of array traversal-order and NumPy's default use of row-major ordering. We will then arrive at the critical topic of vectorization, which prescribes the ways in which NumPy dispatches mathematical operations over arrays of numbers. This will also give us keen insight into how NumPy achieves its tremendous computational efficiency. Finally, we will dive into some of NumPy's more advanced features. These include its rules for broadcasting mathematical operations between arrays of different shapes, as well as its mechanisms for accessing and updating an array's contents via basic and advanced indexing. Armed with these techniques, we will be able to write concise and powerful numerical code using NumPy and Python's many other STEM libraries!



.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Module3_IntroducingNumpy/IntroducingTheNDarray.ipynb
   Module3_IntroducingNumpy/AccessingDataAlongMultipleDimensions.ipynb
   Module3_IntroducingNumpy/BasicArrayAttributes.ipynb
   Module3_IntroducingNumpy/FunctionsForCreatingNumpyArrays.ipynb
   Module3_IntroducingNumpy/ArrayTraversal.ipynb
   Module3_IntroducingNumpy/VectorizedOperations.ipynb
   Module3_IntroducingNumpy/Broadcasting.ipynb
   Module3_IntroducingNumpy/BasicIndexing.ipynb
   Module3_IntroducingNumpy/AdvancedIndexing.ipynb
