# Modules

As you may recall from the earlier section on community, one of the key non-programming skills of programming is knowing when and how to leverage code written by others.

This code is organized into units known as **"packages"** or **"libraries"**, and can consist of one or more **"modules"**. These terms have come up earlier in this curriculum.

In Python, these libraries come in three flavors: as part of the Python Standard Library, as a third-party library downloadable from the internet, or as code you've written yourself.

Every installation of Python comes with the **[Python Standard Library](https://docs.python.org/2/library/)**, a set of key modules that are often useful for programming in Python. Everything in the standard library is already installed on your computer, making it very easy to use. Further, every Python installation includes these libraries, so code which relies on them is virtually guaranteed to run on anyone's computer.

Beyond the standard library is a massive collection of third-party libraries, organized using the **[Python Package Index]**(https://pypi.python.org/pypi), or PyPI. To install and manage these third-party libraries, we use a tool known as a "package manager", which for Python is a tool called [`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager)).

Finally, you can write and re-use your own modules; a very common practice.

## Import Syntax

First, let's discuss the syntax for importing modules:

Importing the entire module:

```
import <module>
<module>.<function>
```

Importing a function from the module:

```
from <module> import <function>
<function>
```

Importing all functions in the module:

```
from <module> import *
<function>
```

## Standard Library

The Python Standard Library contains many utilities. Here are a few of the modules available in the library:

- `math` -- more advanced math functions.
- `datetime` -- tools for working with dates and times.
- `os` -- tools for working with the operating system.
- `json` -- tools for working with JSON, a common data format.

Let's see a few examples:

### Getting a square root:

```
>>> import math
>>> math.sqrt(4)
2.0
```

### Measuring time passing:

```
>>> from datetime import datetime
>>> start = datetime.now()
>>> end = datetime.now()
>>> end - start
datetime.timedelta(0, 4, 399648)
```

At this point, you may be wondering: "if these modules are included with Python, why do we need to import them at all? Why can't they always be available?". It's a good question, and the answer is that importing modules takes time, and importing the entire standard library would be wasteful if the functionality isn't necessary. The Python core developers have tried to strike a balanced between speed and functionality; having the standard library available as needed was their attempt to strike this balance.

## Third-Party Libraries

Using third-party libraries requires installing them from an external source (generally the internet).

Doing this requires a tool called `pip`. Here are [installation instructions](https://pip.pypa.io/en/stable/installing/). Note that `pip` is used from the command line, **not** the Python interpreter.

Let's see some examples. Recall that `$` denotes the shell, and `>>>` denotes the Python interpreter:

### Installing `Requests`

```
$ pip install requests
Collecting requests
  Downloading requests-2.11.1-py2.py3-none-any.whl (514kB)
    100% |████████████████████████████████| 522kB 787kB/s
Installing collected packages: requests
Successfully installed requests-2.11.1

$ python
Python 2.7.9 (default, May  1 2015, 19:04:44)
>>> import requests
>>> requests.get('https://google.com')
<Response [200]>
```

### Installing `IPython`

There is a powerful alternative Python interpreter known as [IPython](https://ipython.org/), short for Interactive Python. The IPython interpreter has many valuable features that the vanilla Python interpeter does not. Here is an example of using `pip` to install `IPython`. Here you will see an example of one package, `IPython`, requiring other packages (known as "dependencies") in order to run. `pip` is smart enough to figure out what these are and install them as well.

```
$ pip install ipython
Collecting ipython
  Downloading ipython-5.1.0-py2-none-any.whl (747kB)
    100% |████████████████████████████████| 747kB 183kB/s

# Downloading other things...

Installing collected packages: wcwidth, prompt-toolkit, traitlets, backports.shutil-get-terminal-size, setuptools, pathlib2, ipython

Successfully installed backports.shutil-get-terminal-size-1.0.0 ipython-5.1.0 pathlib2-2.1.0 prompt-toolkit-1.0.6 setuptools-26.0.0 traitlets-4.2.2 wcwidth-0.1.7

$ ipython
Python 2.7.9 (default, May  1 2015, 19:04:44)

In [1]: 2 + 2
Out[1]: 4

In [2]: _ + 2
Out[2]: 6

In [3]: Out[2] * 2
Out[3]: 12
```

## Personal Modules

Modules in the standard library, as well as those installed with `pip`, all ultimately live as files on your computer. It stands to reason that modules you write yourself, also being files on your computer, should be importable as well. And they are!

As an example, let's imagine the following files in the current working directory:

```
prog1.py
prog2.py
utilities.py
```

You're writing two programs, `prog1.py` and `prog2.py`. There is code that you want to re-use between both programs, which you put in the file `utilities.py`. You can import this code using the same syntax you use to import any module:

```
import utilities
utilities.foo()
```

OR

```
from utilities import foo
foo()
```

There are some details about import paths which will become relevant if you are trying to import code across larger distances, which are discussed more [here](http://kronosapiens.github.io/blog/2014/07/28/understanding-package-imports-in-python.html).