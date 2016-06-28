# Programs and Processes

In the previous section, we discussed computer hardware architecture and described the means by which computers do work. This brings us to the natural next question: how do computer programmers develop, organize, and initiate this work? They do so via **programs**, executed as **processes**.

A computer program is, in the simplest form, a set of instructions for the computer to carry out. The computer will carry out these instructions, one after the other, until the instructions terminate or the computer is stopped by some external means. Some programs are designed to never terminate -- they continue to "loop" until the they are manually stopped. Your computer's operating system (OS) is an example of a such a program -- one designed to run as long as your computer stays on.

A program is stored in your computer's memory as a sequence of bits. When a program is executed, these bits are read by the CPU, and the actions they represent are performed.

When a program begins running, it is known as a **process**. A single program can be run as multiple processes -- consider how the Chrome browser can have multiple open tabs. There is a program, the "Chrome tab", which is saved somewhere on your computer (likely inside the Chrome .app or .exe file). Every time you open a new tab, this program is launched. A Chrome browser with five open tabs still counts as a single program, extended over five processes.

Processes can launch (or "spawn") other processes. Consider what happens when you double-click on a folder on your desktop: your OS process launches a Finder/Explorer process, which lets you browse files on your computer.

## Types of Programming Languages

As a programmer, a large part of your job will involve writing programs. For you, these programs will almost always be represented as "[plain text](https://en.wikipedia.org/wiki/Plain_text)", the term for text without any fonts or formatting. Plain text is opposed to "rich text", which is often displayed with specialized fonts, sizing, coloring, and other styling. The [markdown language](https://en.wikipedia.org/wiki/Markdown) (in which this curriculum is written) is a good example of a plain text language which can be rendered as rich text by specialized readers (such as the GitHub file viewer!)

This plain text will ultimately be converted into instructions to be read by the computer (known as "[machine code](https://en.wikipedia.org/wiki/Machine_code)"). This process will generally take one of two paths:

For **compiled** languages, like C and Java, the programs you write will be fed into another program, known as a "[compiler](https://en.wikipedia.org/wiki/Compiler)", which will parse the text and translate it into a new file, written in machine code. This new file, known as a "binary" or "executable" can be run directly by the OS as a new process. You may hear talk of "C compilers" and "Java compilers"; the study of compilers is itself a major field.

For **interpreted** languages, like Python and JavaScript, the programs you write will be read by another program, known as the "[interpreter](https://en.wikipedia.org/wiki/Interpreted_language)". The interpreter will execute the instructions described in your program, without translating those instructions directly into machine code. The "interpreter" process is the only process the computer ever sees -- it is a powerful program which will change its behavior based on the code you write. When we say a program is written "in Python", we mean to say it is text which can be executed by the Python interpreter.

The division between compiled and interpreted languages represents a major division among programming languages. Compiled programs have the advantage of generally being much faster, as the work of translating the plain text into machine code needs to be done only once. The downside is that compilation can be slow, making the work of developing and testing such programs tedious. Interpreted languages enjoy greater flexibility, as changes in the program can be run immediately. The downside is that such programs are generally slower to run than their compiled counterparts, as the program must be continuously interpreted every time it is run.