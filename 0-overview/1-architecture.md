# Computer Architecture

If one wants to use computers effectively, it is helpful to have some insight into their inner workings.

In this chapter, we will discuss the architecture of a computer, and point out some of the key ideas underlying the various components.

## Hardware

### Building Blocks

Ultimately, computers are nothing but billions of coordinated electric impulses. The reasons why computers are valuable is that these electric impulses are being **coordinated** in order to perform meaningful knowledge work. This work is accomplished by means of something known as **Boolean Logic**. Boolean logic is a very simple yet powerful tool for making decisions. Here are some examples:

```
true AND true = true
true AND false = false

true OR true = true
true OR false = true

NOT true = false

```

Boolean logic was invented in XXXX by mathematician George Boole. In modern usage, "Boolean" significes the idea of a true/false binary.

Consider the following equivalences:

```
1 = on = true
0 = off = false
```

Electricity moves through computers along very precise pathways, which we can think of as wires. Electricity is either flowing through the wire (on), or not (off).

Imagine now a computer chip with two input wires and one output wire. This chip is called "AND". We put a positive charge to both pins -- what do we think the output should be? The answer: positive charge. What would the output be if we put a positive charge only to the first pin? The answer: no charge. By interpreting electric impulses (on/off) as though they represented true/false, it is possible to build physical chips which perform Boolean logic. These simple chips are known as "logic gates" and are the basic building block of computer hardware.

As it happens, it is possible to combine simple logic gates to create new, "compound" chips which can perform more advanced behavior. An important example of a slightly more advanced chip is the "Multiplexor". The multiplexor chip has two input pins, A and B, one output pin, and one "switch" pin (for a total of four pins). When the switch pin is set to on, the input to A becomes the output of the chip. If A is on, the output will be on, and vice versa. If the switch pin is set to off, the input to B becomes the output of the chip. The multiplexor chip is the first occurance of a "decision" based on the inputs, and is built out of simpler logic gates.

From here, it is not such a leap to develop chips capable of performing addition and even more complicated operations. More complicated chips, however, require more input and output wires. Keeping track of these wires, however, requires a new language.

### Binary

To work with these electric impulses, computer programmers developed a language of ones and zeros, known as binary. 0 corresponds to off/false, and 1 corresponds to on/true.

Given that binary has two possible values (1 and 0), we can interpret binary strings as numbers in base 2. Consider the following table:

| binary | base 10 |
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

| binary | base 10 |
|--------|---------|
| 00000000 | 0 |
| 00000001 | 1 |
| 00000010 | 2 |
| 00000011 | 3 |
| 00000100 | 4 |
| 00000101 | 5 |
| 00000110 | 6 |
| 00000111 | 7 |

Same information, different representation. More bits require more memory to store, but can represent a wider range of possible values. Any given computer has a maximum word width which it can handle. A 64-bit computer, for example, is one in which the system word size is 64 bits wide. The following table provides very helfpul intuition about powers of two:

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

### Hardware Architecture

Binary can be used to represent numbers, but that is far from all it can do. Binary is a code, and as such can be used to represent almost anything: commands, locations, or data. A running computer is engaged in a never-ending cycle of **fetching and executing instructions**. This flow of instruction and execution is ultimately how computers do what they do, which is perform calculations and move data around in memory.

#### Tick Tock

To understand how a computer's hardware works, we'll begin with the idea of a "[system clock](https://en.wikipedia.org/wiki/System_time)". Every computer has one, and this clock serves two very important purposes: *keeping track of earth time* and *coordinating activity throughout the computer*. It is this second purpose that interests us.

To get a sense of how a computer understands time, we introduce the idea of a "cycle", consisting of a "tick" phase and a "tock" phase. Not all chips in the computer require a notion of time -- the boolean logic chips discussed above have no notion of time. At any point in time, the state of the inputs determine the state of the outputs. For other chips, including importantly memory chips, the notion of time becomes crucial. Further, complex chips consist of multiple smaller chips, often including some that are time-sensitive, making the complex chip time-sensitive.

For time-sensitive chips, their behavior is divided into two phases. In the "tick" phase, these chips read from their input pins. In the "tock" phase, these chips emit the correct outputs given the inputs. This is one cycle. In the next "tick" phase, they read their next inputs, and then emit the proper outputs, and so on and so forth. The system clock coordinates these cycles across the computer, allowing for very complex interactions.

#### Memory

These time-sensitive chips form the foundation of computer memory. Imagine a chip with three input pins: two labeled "in1" and "in2", and the last labeled "read". It has one output pin: "out". This output pin, however, is forked: one fork points outward, where it can in theory connect to anything. The other fork, however, connects to "in2", forming a loop. The "in1" and "read" chips are connected to the outside. The function of the chip is simple: during the "tick" phase, if "read" is set to 0, then the chip reads from the "in2" pin. Otherwise, it reads from the "in1" pin. During the "tock" phase, it sends the input through to the "out" pin.

Imagine if "in1" and "read" were set to 1 for a single cycle: the 1 would be read into the chip, which would output 1 in the "tock" phase, which would also be the value of "in2" in the **next** "tick" phase. If "read" were set to 0 from then on, the 1 would keep circulating through this loop, since nothing else would ever be accepted from "in1". This is a simple type of memory.

## Kernel

The **[kernel](https://en.wikipedia.org/wiki/Kernel_(operating_system))** is a very important piece of software in a computer. It's generally the lowest-level piece of software, and the one that directly controls the hardware on the computer.

All other processes on your computer ultimately make requests to the kernel for resources (memory, CPU time, etc), and the kernel is responsible for scheduling all of these tasks and keeping the computer from crashing.

Kernels are hugely important, but it is unlikely you will work with them directly any time in the near future.

![kernel](https://en.wikipedia.org/wiki/Kernel_(operating_system)#/media/File:Kernel_Layout.svg)

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


