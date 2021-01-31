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
   :description: Topic: Measuring classification accuracy, Difficulty: Easy, Category: Practice Problem
   :keywords: numpy, vectorization, practice, machine learning, classifier
<!-- #endraw -->

<!-- #region -->
# Measuring the Accuracy of a Classification Model
Suppose that we are working on a project in which we have some model that can process an image and classify its content. For example, my `cat_dog_goose_other` function tries to classify whether a picture is of a cat (class 0), a dog (class 1), a goose (class 2), or something else (class 3). We want to measure the *accuracy* of our classifier. That is, we want to feed it a series of images whose contents are known and tally the number of times the model's prediction matches the true content of an image. The accuracy is the fraction of images that the model classifies correctly.

For each image we feed the `cat_dog_goose_other` model, it will produce four **scores** - one score for each class. The model was designed such that the class with the highest score corresponds to its prediction. There are no  constraints on the values the scores can take. For example, if the model processes one image it will return a shape-$(1, 4)$ score-array:

```python
>>> scores = cat_dog_goose_other(image)
# processing one image produces a 1x4 array of classification scores
>>> scores
array([[-10, 33, 580, 100]])
```
Here, our model has predicted that this is a picture of a goose, since the score associate with class 2 (`scores[2]`) is the largest value. In general, if we pass `cat_dog_goose_other` an array of $N$ images, it will return a shape-$(N, 4)$ array of classification scores - each of the $N$ images has $4$ scores associated with it.

Because we are measuring our model's accuracy, we have curated a set of images whose contents are known. That is, we have a true **label** for each image, which is encoded as a class-ID. For example, a picture of a cat would have the label `0` associated with it, a picture of a dog would have the label `1` and so on. Thus, a stack of $N$ images would have associated with it a shape-$(N,)$ array of integer labels, each label is within $[0, 4)$.

Suppose we have passed our model five images, and it produced the following scores:
```python
# Classification scores produced by `cat_dog_goose_other` 
# on five images. A shape-(5, 4) array.
>>> import numpy as np
>>> scores = np.array([[ 30,   1,  10,  80],  # prediction: other
...                    [-10,  20,   0,  -5],  # prediction: dog
...                    [ 27,  50,   9,  30],  # prediction: dog
...                    [ -1,   0,  84,   3],  # prediction: goose
...                    [  5,   2,  10,   0]]) # prediction: goose
``` 

And suppose that the true labels for these five images are:
```python
# truth: cat, dog, dog, goose, other 
>>> labels = np.array([0, 1, 1, 2, 3])
```

Our model  classified three out of five images correctly; thus, our accuracy function should return 0.6:
```python
>>> classification_accuracy(scores, labels)
0.6
```

To generalize this problem, assume that your classifier is dealing with $K$ classes (instead of $4$). Complete the following function. 

**Tip:** You will find it useful to leverage [numpy's argmax function](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax)`f

```python
def classification_accuracy(classification_scores, true_labels):
    """
    Returns the fractional classification accuracy for a batch of N predictions.

    Parameters
    ----------
    classification_scores : numpy.ndarray, shape=(N, K)
        The scores for K classes, for a batch of N pieces of data 
        (e.g. images).
    true_labels : numpy.ndarray, shape=(N,)
        The true label for each datum in the batch: each label is an
        integer in the domain [0, K).

    Returns
    -------
    float
        (num_correct) / N
    """
    # YOUR CODE HERE
    pass

```
<!-- #endregion -->

<!-- #region -->
### Unvectorized Solution
A simple approach to this problem is to first loop over the rows of our classification scores. We know that each such row stores the scores for each class for a particular data point, and that the *index* of the highest score in that row gives us the predicted label for that data point (e.g. image in our hypothetical use-case). We can then directly compare these predicted labels with the true labels to compute the accuracy.

We can use the function `numpy.argmax` to get the index of the highest score, and thus the predicted class-ID, for each data point. Recall that NumPy arrays use [row-major traversal ordering](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/ArrayTraversal.html#How-to-Traverse-an-Array:-Row-major-%28C%29-vs-Column-major-%28F%29-Traversal-Ordering), so performing a for-loop over `classification_scores` will yield one row of the array at a time.

```python
pred_labels = []  # Will store the N predicted class-IDs
for row in classification_scores:
    # store the index associated with the highest score for each datum
    pred_labels.append(np.argmax(row))  
```

Next, we need to count the fraction of predicted class-IDs that match the true labels classification matches the true classification.

```python
num_correct = 0
for i in range(len(pred_labels)):
    if pred_labels[i] == true_labels[i]:
        num_correct += 1
```

Or we can make use of [a generator comprehension](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html#Creating-your-own-generator:-generator-comprehensions) and [itertools](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Itertools.html) to be much more succinct:

```python
# recall: int(True) -> 1, int(False) -> 0
num_correct = sum(p == t for p, t in zip(pred_labels, true_labels)) 
```

We can formally write this out into the following function:

```python
def unvectorized_accuracy(classification_scores, true_labels):
    """
    Returns the fractional classification accuracy for a batch of N predictions.

    Parameters
    ----------
    classification_scores : numpy.ndarray, shape=(N, K)
        The scores for K classes, for a batch of N pieces of data 
        (e.g. images).
    true_labels : numpy.ndarray, shape=(N,)
        The true label for each datum in the batch: each label is an
        integer in the domain [0, K).

    Returns
    -------
    float
        (num_correct) / N
    """
    pred_labels = []  # Will store the N predicted class-IDs
    for row in classification_scores:
        pred_labels.append(np.argmax(row))
    
    num_correct = 0
    for i in range(len(pred_labels)):
        if pred_labels[i] == true_labels[i]:
            num_correct += 1
    return num_correct / len(true_labels)
```
Testing against our example from above:
```python
>>> unvectorized_accuracy(scores, labels)
0.6
```
Horray! We have a working accuracy function! However, this function can be greatly simplified and optimized by [vectorizing](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html) it.
<!-- #endregion -->

<!-- #region -->
### Vectorized Solution
`numpy.argmax` is one of NumPy's [vectorized sequential functions](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html#Sequential-Functions). As such, it accepts [axis as a keyword argument](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html#Specifying-the-axis-Keyword-Argument-in-Sequential-NumPy-Functions). This means that, instead of calling `np.argmax` on each row of `classification_scores` in a for-loop, we can simply instruct `np.argmax` to operate *across the columns of each row of the array* by specifying `axis=1`.

```python
# returns the column-index of the max value 
# within each row of `classification_scores`
pred_labels = np.argmax(classification_scores, axis=1)
```
This simple expression eliminates our first for-loop entirely.

Next, we can use NumPy's *vectorized logical operations*, specifically `==`, to get a boolean-valued array that stores `True` wherever the predicted labels match the true labels and `False` everywhere else. Recall that `True` behaves like `1` and `False` like `0`. Thus, we can call `np.mean` on our resulting boolean-valued array to compute the number of correct predictions divided by the total number of predictions. We can thus vectorize our second for-loop with:

```python
# computes the fraction of correctly predicted labels
frac_correct = np.mean(pred_labels == true_labels)
```

All together, making keen use of vectorization allows us to write our classification accuracy function *in a single line of code*. 

```python
def classification_accuracy(classification_scores, true_labels):
    """
    Returns the fractional classification accuracy for a batch of N predictions.

    Parameters
    ----------
    classification_scores : numpy.ndarray, shape=(N, K)
        The scores for K classes, for a batch of N pieces of data 
        (e.g. images).
    true_labels : numpy.ndarray, shape=(N,)
        The true label for each datum in the batch: each label is an
        integer in the domain [0, K).

    Returns
    -------
    float
        (num_correct) / N
    """
    return np.mean(np.argmax(classification_scores, axis=1) == true_labels)
```

Not only is this cleaner to look at, but it was also simpler and less error-prone to write. Moreover, it is much faster than our unvectorized solution - given $N=10,000$ data points and $K=100$ classes, our vectorized solution is roughly $40\times$ faster 

(The following "time-it" code blocks must be run in independent cells in a Jupyter notebook or IPython console - `%%timeit` must be the topmost command in the cell)

```python
>>> N = 10000
>>> K = 100
>>> scores = np.random.rand(N, K)
>>> labels = np.random.randint(low=0, high=K, size=N)
```
```python
>>> %%timeit
... unvectorized_accuracy(scores, labels)
39.5 ms ± 1.2 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

```python
>>> %%timeit
... classification_accuracy(scores, labels)
1.6 ms ± 7.04 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```
<!-- #endregion -->
