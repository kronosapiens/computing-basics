## Data Types

What are the objects we manipulate when writing computer programs?

Sometimes, they are numbers. Other times, they are words. Occasionally, they are answers, like yes or no.

What about a set of numbers? Or an operation that you apply? Or a reference from one thing to another?

All of these are objects we manipulate.

Let's consider them in turn.

### Integers

The integers are the whole numbers. They are core values and [we can represent them very concisely](wiki article). We can add and subtract them very quickly. Both positive and negative numbers are easily represented.

Examples:

```
8
19
0
```

### Floats

Floats are numbers with nonzero values after the decimal. Because these numbers (the "reals") have in theory infinite precision, representing them on a computer requires approximating them to some number of places after the decimal (note the contrast with the integers, which can be represented perfectly).

The approximate nature of floats underlies one of the major challenges of scientific computing: performing accurate calculations at very high precision.

Examples:

```
8.483990
0.100939
14e-3
```

### Strings

For some reason, letters, words, and sentences are called "strings". It's probably because they are understood as "strings" of characters. Strings work pretty much as you'd expect, although note that they can take up much more memory than integers.

```
'cat'
'Hello World!'
'1984'
```

Note that an integer can be represented as a string, albeit taking up more space.

### Booleans

Booleans are in a very important sense the most important data type. A "boolean" is the name we give to the values of `true` and `false`. These are identical with `1` and `0`, as well as `yes` and `no`. If you recall the earlier chapter on architecture, and in particular logic gates, you'll recall that they use exactly this language.

```
True
False
1
0
```