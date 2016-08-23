# Shells

For many people, interactions with a computer takes place via a graphical user interface, otherwise known as a “GUI”. Icons on your desktop, double-clicks, drag-and-drop – all of these are GUI operations. The GUI is a program, like any other, which puts things on the screen and interprets keystrokes and trackpad activity. The GUI talks to the kernel and turns your clicks and keystrokes into actions.

A GUI is a very sophisticated program, and GUI-based computers have been around only for the last twenty or so years. Before graphical interfaces were popular (or even possible), computing took place via a much simpler text-based interface. That interface was known as the command line, or the **shell**.

Why shell? Because the shell was a program that wrapped around (get it?) the kernel and provided a convenient way to run commands.

Why would someone use a shell over a more user-friendly GUI? Principally, for control. The primary drawback of a GUI is that it can only do what it was programmed to do. It is very hard to program a GUI, and the interfaces popular on modern computers are not designed to be modified. A shell, on the other hand, is a simple program that can be modified to do almost anything. If a GUI is intuitive but inflexible, a command line is less intuitive (at first), but extremely powerful and flexible. For programmers, data scientists, and others for whom work involves the organization and manipulation of information, this power and flexibility is crucial. This is why people use the command line.

## Working with the shell

A shell is just a program. There are many kinds of shell. On Mac OSX, the default is the **bash** shell. On Windows, there is **PowerShell**. On OSX, you can open a bash shell by opening the “Terminal” application. On Windows, there is a PowerShell application.

Firing up the shell will bring you to a boring-looking screen which looks something like this:

```
Hi! Welcome to the shell!

$ _
```

Not much to look at. You type some things and hit enter. Something happens. Rinse and repeat until your computer crashes or you’re a billionare. Things get more interesting when you realize that every command you type into the shell looks like the following:

```
$ <program> <arguments>
```

There is always one program, and an arbitrary number of arguments. This is how every command works. Your computer comes with several dozen built-in programs, which do very simple but useful things. We will review them shortly. First, however, we must discuss the concept of a **working directory**.

The working directory is your shell’s current “location” inside the filesystem. You can “navigate” the filesystem by running commands which cause the shell to move up or down directory hierarchies. This is analagous to double-clicking on a folder on your desktop.

In OSX and Windows, there are the Finder and Explorer programs for browsing through folders. These programs are GUIs accomplishing the same goal.

Recall from the previous section any file can be fully described by its **absolute path**. When interacting with files (a common activity), you could in theory specify the full path of every file. This can be be extremely tedious, especially when working with deeply-nested files, and especially given that, for any particular task, the files you need are generally close together (for example, if you are writing a program to organize a music collection).

When using the shell, after navigating to a directory, every file argument is evaluated as though the current working directory were prepended to the file's name. Let’s see an example, taking place in the context of the following filesystem:

```
/
    dir1/
        file1.py
```

Here’s an example. In this example, the current **working directory** appears before the `$` symbol, and the command we are running appears after.

```
/$ python dir1/file1.py
Hello world

/$ cd dir1
/dir1$ python file1.py
Hello world

/$ cat file1.py
print 'Hello world'

/dir1$ cd ..

/$ python file1.py
usr/bin/python: can't open file 'file1.py': [Errno 2] No such file or directory
```

Here, we saw three programs run on three arguments.

1. First, we ran the `python` program on argument `dir/file1.py`, a python file. When run, this files prints the text `Hello world` to the screen.
2. Then, we ran the `cd` (change directory) program on argument dir1, also a file (in Unix, everything is a file, even a directory.) Note how the command prompt changes to reflect the fact that we moved through the filesystem.
3. We ran the python program on argument file1.py, the same python file.
4. We ran the `cat` program on the same file. This program simply prints out the contents of the file (the actual python code).
5. We ran the cd program on `..`, representing the current parent directory (`..` is used to traverse **up** the file hierarchy).
6. We ran the python program on argument file1.py, but received an error, because there is no such file in our current location.

Hopefully this example will illustrate the nature of using a shell to navigate and executing commands in a filesystem.

## Command Reference

For Linux-style command line interfaces

Note that in this program reference, filenames and directories can be given as either absolute or relative paths.

Here are the ten utilities you will use most often:

`ls` – list files in current directory

`cd <directory>` – change current directory to `<directory>`

`touch <filename>` – makes a new file

`rm <filename>` – delete a file

`mkdir <directory>` – create a new directory

`rmdir <directory>` – delete a directory

`mv <filename1> <filename2>` – move `<filename1>` to `<filename2>`

`cp <filename1> <filename2>` – copy `<filename1>` to `<filename2>`

`man <program>` – show additional information about the program

Here are a number of other useful utilities:

`pwd` – print working directory

`python <filename>.py` – run a Python file

`cat <filename>` – print the contents of the (entire) file to the screen

`head <filename>` – print the first few lines of a file to the screen

`tail <filename>` – print the last few lines of a file to the screen

`echo <string>` – print `<string>` to the screen (as in, a "string" of letters)

`ps` – print information about currently-running processes (instances of programs)

Note that programs often accept additional optional arguments. Consider:

`tail -n 20 <filename>` – print the last 20 lines of a file to the screen

`ls -lah` – list files in current directory in a super easy-to-read format

`ps -aux` – print a lot of information about currently-running processes

`kill <integer>` – kill the process with process id `<integer>`

## Stdin, Stdout, Processes, Piping

By default, every program takes input from one place, “Standard Input” (`stdin`), and sends output to one place, “Standard Output” (`stdout`). In general, `stdin` is the keyboard, and `stdout` is the screen. A surprisingly large amount of programming boils down to routing the output of one program into the input of another (either via some common data store like a file or database, or directly via something called a **pipe**).

When you execute a command in the shell, the program “takes control” of the terminal while it is running. When it finishes, it returns control of the shell to you. While the programming is running, it may request input from `stdin` (such as asking for a password). It may also send output to `stdout` (for example, updating you on the program’s progress).

A process is an instance of a running program. To think of it another way, a program is just a bunch of zeroes and ones inside of memory. A process is that program being executed in a million steps on the computer’s CPU. The same program can be run as many processes. They fundamental rule about computers is that processes aren’t allowed to mess with each other’s memory. The kernel makes sure of this (remember the kernel?).

It is possible to “background” a process, which simply means that you don’t let that process take control of your shell. This lets you type in more commands while the process is running. At times this behavior may be desirable. On Unix-like systems (Linux, OSX), you can background a process using the ampersand, like this:

```
/$ <program> <arg1> <arg2> &
```

Also, processes can (and often do) create (“spawn”) other processes. The Chrome process spawns Tab processes, and so on. Processes can control other processes. Processes can change their working directory, or spawn subprocesses in other directories. There are basically no limits, except that processes can only interact via a specific interface.

Finally, piping is a technique for routing the output of one program into the input of another:

```
/$ <program1> <args> | <program2>
```

Here, the flow of information would go as follows:

`stdin` -> program1 -> program2 -> `stdout`

This is useful as it allows you to combine simple programs to create more complicated programs, which some people think is a good idea. For more on this, and on Unix in general, [check out this classic video](https://www.youtube.com/watch?v=tc4ROCJYbm0).

# More Practice

If you would like more practice working with the shell, Codecademy has a free curriculum: https://www.codecademy.com/learn/learn-the-command-line
