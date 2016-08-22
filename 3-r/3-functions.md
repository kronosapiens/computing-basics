Expressions, variables, and functions in R work very similarly to those in Python, just with a different syntax.

Here is an example which combines these concepts and demonstrates R's syntax:

```
myMax <- function(num1, num2) {
    if (num1 > num2) {
        max <- num1
    } else {
        max <- num2
    }
    return(max)
}
```

One notable difference between R and Python is that Python's syntax is "white space dependent", meaning that the indentation is actually important for the code to be correct. This is why Python code doesn't require curly braces, a common feature of other languages. R, on the other hand, requires curly braces to denote different parts of the code. This can be cumbersome to write, but means that R code is not white space dependent -- you can indent it however you like, and it will still work:

```
myMax <- function(num1, num2) {
    if (num1 > num2) {max <- num1}
    else {max <- num2}
    return(max)
}
```