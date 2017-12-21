from contextlib import redirect_stdout
from inspect import cleandoc
from textwrap import dedent
import numpy as np

def check_raises_error(func, *args, **kwargs):
    """ Raises AssertionError if `func` raises an error"""
    try:
        with redirect_stdout(None):
            func(*args, **kwargs)
    except Exception as e:
        raise AssertionError("TEST FAILED: Your code raised the following error:\n\t{}".format(e))

def check_returns_None(func, *args, **kwargs):
    """ raises AssertionError if `func` returns `None`"""
    with redirect_stdout(None):
        if func(*args, **kwargs) is None:
            msg = """TEST FAILED: Your function returned `None`. 
            Make sure that you have included a `return` statement in your function."""
            raise AssertionError(cleandoc(msg))

def raises_IndexError(func, *args, **kwargs):
    try:
        with redirect_stdout(None):
            func(*args, **kwargs)
        return False
    except IndexError:
        return True

def check_same_datatype(out, expected):
    if not isinstance(out, type(expected)):
        msg = """TEST FAILED:
                 Your function returned an object with the data type:
                 {out}
                 
                 Grader expected the data type:
                 {expected}"""
        raise AssertionError(cleandoc(msg.format(out=type(out), expected=type(expected))))

def is_close_verbose(out, expected):
    if out.shape != expected.shape or not np.allclose(out, expected):
        msg = "TEST FAILED:\n\nYour function returned:\n{out}\n\nGrader expected:\n{expected}"
        raise AssertionError(msg.format(out=repr(out), expected=repr(expected)))

def shares_memory_verbose(x1, x2):
    if not np.shares_memory(x1, x2):
        raise AssertionError("TEST FAILED: The array you returned did not come from the original array.")