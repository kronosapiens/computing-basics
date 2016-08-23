## The Vector

The "vector" is R's version of the "array" (known in Python as a "list"). The functionality is almost identical.

Let's see an example of a vector in action:

```
> myvec <- c(1, 2, 3)

> length(myvec)
[1] 3

> myvec[1]
[1] 1

> myvec[3]
[1] 3

> myvec[1:2]
[1] 1 2

> myvec[4]
[1] NA

> myvec[4] <- 'cat'

> myvec
[1] "1"   "2"   "3"   "cat"

> myvec[4]
[1] "cat"

> length(myvec)
[1] 4
```

A few things going on here:

First thing to note: a list is "one-indexed", meaning that the first element in the list is accessed with `1`. Contrast this to the zero-indexing of the Python list.

Next, note how you can pass two values separated by a colon to select a subset of the list. The first element of the subset will be the element indexed by the first value; the last element of the subset will be the element indexed by the second value. Contrast with with Python, for which the subset **excludes** the element indexed by the second value.

Next, see what happens when trying to access an element of the list that isn't there -- R will return the null value NA, but will not throw an error.

Last, note that you can add elements to a list using the select and `<-` syntax.

## The Dataframe

For some reason, R does not include the "hash table" datatype (the dictionary in Python). The omission seems strange, since this data type is very useful (once described as "the most useful data structure known to man"). There's probably a good reason somewhere.

Fortunately, R gives us another datatype, built in, that's very useful: the dataframe. A dataframe is basically a table, much like an Excel spreadsheet. It has rows, and columns, and is the representation of choice for most data sets you will find in the wild. Note that dataframes exist in Python as well, but require a third-party library, [`pandas`](http://pandas.pydata.org/), to use.

Let's see an example of a dataframe in action:

```
> names <- c('Keiko', 'Sarah', 'Abe')

> ages <- c(24, 25, 23)

> heights <- c(100, 110, 105)

> students <- data.frame(names, ages, heights)

> students
  names ages heights
1 Keiko   24     100
2 Sarah   25     110
3   Abe   23     105

> students$ages
[1] 24 25 23

> mean(students$ages)
[1] 24

> max(students$heights)
[1] 110

> students[students$ages >= 24,]
  names ages heights
1 Keiko   24     100
2 Sarah   25     110
```

Notice how the dataframe lets us organize all of our data in a single object. Now we can ask questions of our data (mean, max and so on), as well as select subsets of our data based on criteria (24 or older, etc). This is barely scratching the surface; much of your work in data analysis will revolve around dataframes.
