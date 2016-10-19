# Debugging

Bugs are unintended behaviors in a program. A crash is a major type of bug, but not all bugs cause crashes. Some are more subtle -- imagine trying to add up all the numbers in a list, but actually adding up all but the last one.

Code has bugs. There isn't much you'll be able to do to prevent this. While good coding practices and testing can help reduce the number of bugs you'll deal with, they'll still pop up.

Dealing with bugs can be frustrating, if not downright scary, at first. Over time, you'll get better at understanding what went wrong, and figuring out how to fix it.

## Read the error message

Very often, a crash will result in some sort of error message printing to the screen. Let's see an example in Python:

```
>>> ls = ['a', 'b', 'c']
>>> ls[3]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

We see two parts to the error message. The first part, known as the **traceback**, shows which line in the code caused the error, as well as the context for that line being called. In this case, since we were typing into a Python shell, the traceback is uninteresting (it's just saying input came from the keyboard, `stdin`). The second part is the actual **error**, in this case an `IndexError`, Python-speak for trying to access a list element that isn't there.

Let's see another example. First, let's define a few functions in the file `bug.py`:

`bug.py`
```
def foo():
    return bar()

def bar():
    return baz()

def baz():
    return 1 / 0

foo()
```

```
$ python bug.py

Traceback (most recent call last):
  File "bug.py", line 10, in <module>
    foo()
  File "test.py", line 2, in foo
    return bar()
  File "test.py", line 5, in bar
    return baz()
  File "test.py", line 8, in baz
    return 1 / 0
ZeroDivisionError: integer division or modulo by zero
```

Here, the traceback tells us the sequence of calls that led to the error being triggered. If a particular line of code is called in many different ways, this traceback gives valuable information about how the bug might have been triggered.

Error messages can be intimidating at first, but they are generally designed to be helpful. They tell you what line caused the error, what was happening with the program, and what specifically went wrong. Always a good place to start.

## Google the error message

If you're reading the error message and have no idea what to do, it's time to turn to the awesome power of the internet. You are most likely not the first person to have this problem, and you should lean on the people who've come before you. Very often, copy/pasting the error message directly into Google returns good results.

[Here's an example.](https://www.google.com/search?q=ZeroDivisionError%3A+integer+division+or+modulo+by+zero&oq=ZeroDivisionError%3A+integer+division+or+modulo+by+zero&aqs=chrome..69i57j69i58.642j0j4&sourceid=chrome&ie=UTF-8)

The first results will often be from a site called **StackOverflow**, a major resource. StackOverflow, or SO, is the leading question and answer site for programmers. Programmers ask questions on the site, and other programmers answer. These answers are saved and searchable, so the next time someone runs into the same problem, the answer is already waiting.





