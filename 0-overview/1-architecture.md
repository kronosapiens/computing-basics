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

Binary can be used to represent numbers, but that is far from all it can do. Binary is a code, and as such can be used to represent almost anything: commands, locations, any data. A running computer is engaged in a never-ending cycle of **fetching and executing instructions**. This flow of instruction and execution is ultimately how computers do what they do, which is perform calculations and move data around in memory.







