## The List

The "list" (often called an "array") is the simplest data type. It represents an **ordered collection** of other (usually similar) objects. Lists have length and contents. You can insert things into lists, as well as access things inside the list.

Lists are great when you have a handful of homogeneous or ordered items that you want to keep together, like names of band members:

```
['john', 'paul', 'george', 'ringo']
```

Lists have the following (unsurprising) properties:

1. Length
2. Contents

Here is an example of a list in action:

```
>>> mylist = [1,2,3]

>>> len(mylist)
3

>>> mylist[0]
1

>>> mylist[2]
3

>>> mylist[0:2]
[1,2]

>>> mylist[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

>>> mylist.append('cat')

>>> mylist
[1, 2, 3, 'cat']

>>> mylist[3]
'cat'

>>> len(mylist)
4
```

A few things going on here:

First thing to note: a list is "zero-indexed", meaning that the first element in the list is accessed with `0`, the second element with `1`, etc. Zero-indexing is very common in computer science; it may seem strange at first but will soon become second nature.

Next, note how you can pass two values separated by a colon to select a subset of the list. The first element of the subset will be the element indexed by the first value; the last element of the subset will be the element **before** the element indexed by the last value.

Next, see what happens when trying to access an element of the list that isn't there -- Python will "throw an exception", in this case an `IndexError`.

Last, note that you can add elements to a list using the `append` method. There are other ways of constructing and extending lists; these are just the basics.

## The Dictionary

With lists, you access objects by their **location**. This is great when order matters, but there are lots of situations where order doesn't matter. In those situations, you usually want to access an objects by some sort of **key**.

Enter the "dictionary" (often called a "hash", for reasons that are very legitimate if not immediately apparent).

The dictionary has the property that every item is associated with a key. You use the key to set the value, you use the key to get the value. Dictionaries are great when you want to organize heterogenous data, like student records:

```
{
    'name': 'Isaac Harper'
    'uni': 'ish2321'
    'age': 27
    'city': 'Brooklyn'
}
```

Dicts have the following properties:

1. Keys
2. Values
3. Length

Here is an example of a dict in action:

```
>>> mydict = {'name': 'Daniel Kronovet'}

>>> mydict
{'name': 'Daniel Kronovet'}

>>> mydict['email'] = 'dbk2123@gmail.com'

>>> mydict
{'name': 'Daniel Kronovet', 'email': 'dbk2123@gmail.com'}

>>> mydict['ssn']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'ssn'

>>> mydict['email']
'dbk2123@gmail.com'

>>> mydict['email'] = 'kronovet@gmail.com'

>>> mydict['email']
'kronovet@gmail.com'

>>> len(mydict)
2

>>> mydict.keys()
['name', 'email']

>>> mydict.values()
['Daniel Kronovet', 'dbk2123@gmail.com']
```

A few things going on here:

First, note that you assign and access values by passing a key. A key can be anything -- a string, an integer, or even another object. Keys are commonly strings, as strings have more semantic power than integers.

Observe that the value for a given key can be updated as often as necessary. Note also that attempting to access a value that does not exist (i.e. there is not value for that key) will result in a `KeyError`.