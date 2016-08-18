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

Imagine that you are a president in charge of a government. You have thousands of government employees, hundreds of officials, and dozens of major branches. You need to somehow coordinate the activity of the whole government.

One approach would be having everyone in the government talk to everyone else. This approach would be inefficient, and highly error prone. Changes in policy would take a very long time to get spread throughout the government, and employees would often be acting on bad information. Resources would generally not be where they were needed, and changing plans would be hard.

A better approach would be to designate certain groups of employees for specific problems, having one agency be in charge of transportation, another in charge of education, yet another in charge of foreign policy. Each of these agencies would be run by a relatively small team of officials. These officials would communicate with you, and each other, and relay new plans to their employees. Such a model would be much easier to maintain, adding or removing agencies as needed. New information would lead to new strategies, which could be carried out by coordinating with the officials, who could then carry out orders with their agencies.

Experience shows that the second model has found favor with real-world organizations; parallel attitudes hold when creating software.

The key idea is that software is too complicated to hold in your head all at once, and so the best way to make programming manageable is to keep different parts of your program **very separate**. When you separate our parts of your program into different pieces (let's call them **modules**), then you can work on one without having to think about how the other ones work. Instead of having to hold the whole project in your head to be able to make changes, you only have to think of a single piece.


# Interfaces

Closely linked to the idea of modules is the idea of **interfaces**, or the way that modules communicate with each other. The gold star in software is the **simple, stable interface**, hiding complex behavior behind a simple set of commands.

Let's consider the transporation department. They develop a technology for finding the most efficient route between two points, and they make this technology available to everyone. The interface is simple: enter a starting address, and an ending address, and the tool does the rest. The actual algorithm for finding the route is complex, and researchers are constantly working to make it better. As long as the interface remains the same, however, no users of the tool have to know about the changes happening under the hood. Furthermore, the makers of the tool don't have to know about how the tool is being used. The *simple, stable interface* makes this possible.