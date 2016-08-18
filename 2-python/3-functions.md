# Expressions

An expression is the simplest description of some kind of action you're performing on your data.

Examples:

```
2 + 2
answer = 42
```

When your program starts running, the Python interpreter will "evaluate" these expressions and will return whatever the result is. An expression is a very general class of object in programming.

# Variables

"Variables" are used to hold references to data. Using variables makes it easier to organize programs, since it helps you keep track of what the **purpose** is for various data, as well as to make it easier to access the same piece of data repeatedly.

# Control Flow

Control flow is the way we have computers make decisions. The classic case is the "if statement":

```
if age < 21:
    print 'No alcohol!'
else:
    print 'Enjoy responsibly.'
```

Control flow involves at minimum two things: some expression which evaluates to either `True` or `False`, and an expression to evaluate if the answer should be "true". This would be a conditional with a single "branch". You can see how one could include additional expressions (such as "if-else" or an "if-elseif" conditionals) to create arbitrarily complicated control flows.

# Functions

"Functions" allow us to resuse bits and pieces of behavior, in a very convenient package.

Here is the canonical example, squaring a number.

```
def square(x):
    return x * x
```

Here, we have taken the squaring operation and captured it inside a function. Now, whenever we need to square a number, we simply call `square(x)` and have our answer. Without this function, we would have to write `x * x` every time we wanted a square. In this simple case, it might seem like writing `x * x` every time might not be such a bad thing. But functions can get complicated, and capturing them as functions is an absolutely crucial skill in programming. Consider another example:

```
def max(num_list):
    max_so_far = -inf
    for num in num_list:
        if num > max_so_far:
            max_so_far = num
    return max_so_far
```

Here, finding the max of a list of numbers requires performing a handful of operations. Having access to the `max` functions speeds things up enormously.

Another benefit of functions is that they can be used to define **interfaces** between parts of your program. When other parts of your code only know about a single function, then it becomes much easier to catch and fix bugs, as well as make large-scale changes and modifications to your code. Using functions to define interfaces is also a crucial programming skill.