"""
Indexing a 3D array
-------------------

Use the following code to initialize the 3-dimensional array `x`:

```python
>>> import numpy as np
>>> x = np.arange(27).reshape(3,3,3)
>>> x
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],

       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])
```

In the following questions, you will be asked to access specific 
items or sub-arrays within `x`, using indexing and slicing. You 
will be asked to provide your answer in the form of a function. 

For example, if you were asked to access the element `0` in the
array, your solution would simply be:
```python
def solution_example(x):
    return x[0, 0, 0]
```
"""

def _grade_3d_index(student_func, problem_no):
        import numpy as np
        from .grader_utils import raises_IndexError, shares_memory_verbose, is_close_verbose
        from .grader_utils import check_raises_error, check_returns_None, check_same_datatype
        from inspect import cleandoc
        from contextlib import redirect_stdout, redirect_stderr

        input_array = np.arange(27).reshape(3, 3, 3)
        key = [(0, slice(None), slice(None)),
            (slice(None), slice(None), 0),
            (0, slice(None, 2), slice(1, None)),
            (slice(None, None, -1), ),
            (slice(None, None, 2), 0, slice(None)),
            (1, 2, 2)]

        print("Grading problem # {}:...\n".format(problem_no))
        
        soln_index = key[problem_no - 1]
        soln = input_array[soln_index]
        
        check_raises_error(student_func, input_array)
        check_returns_None(student_func, input_array)
        
        out = student_func(input_array)
        check_same_datatype(out, soln)

        if any(isinstance(i, slice) for i in soln_index) or len(soln_index) < input_array.ndim:
            # check that returned subarray came from input array
            shares_memory_verbose(input_array, out)
        else:
            # check that returned item came from input array
            edited_array = np.copy(input_array)
            edited_array[soln_index] = -100
            tmp_out = student_func(edited_array)
            if  tmp_out != -100:
                msg = "TEST FAILED: The item you returned did not come from input array"
                raise AssertionError(msg)
        is_close_verbose(out, soln)
        return None


def grade_3d_index(student_func, problem_no):
    try:
        _grade_3d_index(student_func, problem_no)
    except AssertionError as e:
        print(e)
        return None
    print("All Tests Passed!")
    return None
