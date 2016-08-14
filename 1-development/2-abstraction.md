# Abstraction

As it turns out, writing quality software is very hard. When a project is small, it is generally possible for a talented programmer to keep track of the various moving parts in their head. As the project gets larger, however, the number of moving parts increases dramatically, and it becomes impossible to keep track of the project in its entirety.

To handle this, programmers rely on a concept known as "abstraction" to limit the amount of complexity they have to deal with at any given time. The word "abstract", in its use as a verb, means to consider something separately or removed from something else. In this sense, it means to separate the **use** of something from its **implementation**.

Let's consider the case of addition:

```
1 + 2
```

This is one of the simplest possible examples of code, consisting of three things: two integers, and an operator to apply to those integers. Underneath this simple appearance, however, hides a surprising amount of complexity. The integers `1` and `2` are themselves represented using strings of bits and the `+` operation itself requires manipulating those bits. When programming, it is almost never necessary to think about this underlying implementation, so we "abstract" it away underneath a simple **interface**. Rather than think about moving bits every time we want to add two integers, we create the `+` abstraction, and use it whenever we need to add. By doing this, we limit the amount of complexity we have to keep track of at any given time.

Closely associated with the concept of abstraction is the concept of an **interface**. The idea here is that complex behavior is hidden behind a simple interface; in order to use this complex behavior, one only needs to learn the simple interface.

Let's consider a slightly more interesting example, that of a hypothetical `cash_register`.

```
cash_register.add_item('banana')
cash_register.add_item('apple')
cash_register.add_item('milk')
cash_register.add_item('eggs')
cash_register.add_item('eggs')

cash_register.remove_item('eggs')

cash_register.apply_discount(.2)
cash_register.total_with_tax()
```

In this example, we have a "cash register" which can add and remove items, apply discounts, and calculate the total. Under the hood, each of these behaviors is implemented with some (potentially complex) code. Ultimately, we don't care how these things are implemented, since we only care that these behaviors work the way we expect. We have "abstracted away" the underlying implementation of the cash register, and interact with the underlying code only via the given interface (the methods `add_item`, `remove_item`, `apply_discount`, `total_with_tax`, etc).


# Modularity