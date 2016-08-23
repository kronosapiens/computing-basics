# Computer Architecture

If one wants to use computers effectively, it is helpful to have some insight into their inner workings.

In this chapter, we will discuss the architecture of a computer, and point out some of the key ideas underlying the various components.

# Hardware

## Building Blocks

Ultimately, computers are nothing but billions of coordinated electric impulses. The reasons why computers are valuable is that these electric impulses are being **coordinated** in order to perform meaningful knowledge work. This work is accomplished by means of something known as **Boolean Algebra**. Boolean algebra,  is a very simple yet powerful tool for making decisions. Here are some examples:

```
true AND true = true
true AND false = false

true OR true = true
true OR false = true

NOT true = false
```

[Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra) was invented in 1847 by mathematician George Boole. In modern usage, "Boolean" significes the idea of a true/false binary.

Consider the following equivalences:

```
1 = on = true
0 = off = false
```

Electricity moves through computers along very precise pathways, which we can think of as wires. Electricity is either flowing through the wire (on), or not (off).

Imagine now a computer chip with two input wires and one output wire. This chip is called "AND". We put a positive charge to both pins -- what do we think the output should be? The answer: positive charge. What would the output be if we put a positive charge only to the first pin? The answer: no charge. By interpreting electric impulses (on/off) as though they represented true/false, it is possible to build physical chips which perform Boolean logic. These simple chips are known as "logic gates" and are the basic building block of computer hardware.

These gates are commonly represented using something known as a "truth table". Here is the truth table for AND:

| a | b | out |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

As it happens, it is possible to combine simple logic gates to create new, "compound" chips which can perform more advanced behavior. An important example of a slightly more advanced chip is the "Multiplexor". The multiplexor chip has two input pins, `a` and `b`, one output pin, and one "switch" pin (for a total of four pins). When the switch pin is set to off, the input to `a` becomes the output of the chip. If `a` is on, the output will be on, and vice versa. If the switch pin is set to on, the input to `b` becomes the output of the chip. The multiplexor chip is the first occurance of a "decision" based on the inputs, and is built out of simpler logic gates.

Here is the truth table for MULTIPLEX:

| a | b | sw | out |
|---|---|----|-----|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 |

From here, it is not such a leap to develop chips capable of performing addition and even more complicated operations. More complicated chips, however, require more input and output wires. Keeping track of these wires, however, requires a new language.

## Binary

To work with these electric impulses, computer programmers developed a language of ones and zeros, known as binary. 0 corresponds to off/false, and 1 corresponds to on/true.

Given that binary has two possible values (1 and 0), we can interpret binary strings as numbers in base 2. Consider the following table (with binary being base 2):

| base 2 | base 10 |
|--------|---------|
| 000 | 0 |
| 001 | 1 |
| 010 | 2 |
| 011 | 3 |
| 100 | 4 |
| 101 | 5 |
| 110 | 6 |
| 111 | 7 |

Here, binary numbers are given in "words" of three "bits" each. Here are the same numbers, represented in 8-bit (byte) form:

| base 2 | base 10 |
|--------|---------|
| 00000000 | 0 |
| 00000001 | 1 |
| 00000010 | 2 |
| 00000011 | 3 |
| 00000100 | 4 |
| 00000101 | 5 |
| 00000110 | 6 |
| 00000111 | 7 |

Same information, different representation. More bits require more memory to store, but can represent a wider range of possible values. Any given computer has a maximum word width which it can handle. A 64-bit computer, for example, is one in which the system word size is 64 bits wide. The following table provides helfpul intuition about powers of two:

| bits | possible combinations |
|--------|---------|
| 0 | 2^0 = 1 |
| 1 | 2^1 = 2 |
| 2 | 2^2 = 4 |
| 4 | 2^4 = 16 |
| 8 | 2^8 = 256 |
| 16 | 2^16 = 65,536 |
| 32 | 2^32 = 4,294,967,296 |
| 64 | 2^64 = 18,446,744,073,709,551,616 |

## Hardware Architecture

Binary can be used to represent numbers, but that is far from all it can do. Binary is a code, and as such can be used to represent almost anything: commands, locations, or data. A running computer is engaged in a never-ending cycle of **fetching and executing instructions**. This flow of instruction and execution is ultimately how computers do what they do, which is perform calculations and move data around in memory.

The following are the major components of a computer's hardware:

### CPU

The CPU, or Central Processing Unit, is the computational core of a computer. This chip is designed to:

1. Receive as input data and instructions.
2. Perform actions on the data based on the instructions.
3. Send the result elsewhere for further work.

A single CPU "core" can in general execute one instruction at a time. "Multi Core" computers have multiple CPU chips, allowing them to execute multiple instructions in parallel.

### Memory

Much of the rest of a computer consists of various places to store data -- memory. This memory comes in many forms, and plays many roles:

- RAM (Random Access Memory) is a type of memory that can be accessed quickly and in any order. RAM is generally used to store the results of calculations while the computer is running various programs.
- Hard drives are a type of memory that is slower to access and must be read in sequential blocks, but is also significantly cheaper. These drives are generally used for main storagae of data.

These are the main classes, but there are many more. For example, there is a piece of memory dedicated to holding a running program: after all, instructions themselves need to be read from memory somewhere.

## Kernel

The **[kernel](https://en.wikipedia.org/wiki/Kernel_(operating_system))** is a very important piece of software in a computer. It's generally the lowest-level piece of software, and the one that directly controls the hardware on the computer (physically reading from memory, sending instructions to the CPU, and so on)

All other processes on your computer ultimately make requests to the kernel for resources (memory, CPU time, etc), and the kernel is responsible for scheduling and coordinating all of these tasks and keeping the computer from crashing.

Kernels are hugely important, but it is unlikely you will work with them directly any time in the near future.

![kernel](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Kernel_Layout.svg/304px-Kernel_Layout.svg.png)

## Operating System

The **[operating system](https://en.wikipedia.org/wiki/Operating_system)** or OS consists of the kernel and a large number of other utilities, with the goal of providing a friendly interface to the user. Popular operating systems include Unix and variants, Apple OSX, and Microsoft Windows.

Operating systems must be run on computer hardware; not all hardware can run all operating systems. In general, OSX runs only on Apple computers, while Windows and Unix can be run on a wider variety of computers. Newer operating systems require newer hardware, and so on.

## Software

On top of the OS rests all the other software you care about: software you download from the internet, software you buy in the store, software you write yourself.

This software can do basically anything you want, provided it is written to run on the operating system you're using.

# Takeaways

The main takeaways from this section are:

1. Hardware -> Kernel + Operating System -> User Software

2. As a programmer, you will be writing software and will be interacting with the operating system. The kernel and hardware will generally not be important for you, but you should know they exist and the role they play.


