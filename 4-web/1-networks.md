# Networks

To understand the web, let's first get a sense of some of the constraints that shaped the web:

1. Computers (often called "nodes") can enter and exit the network any time, without warning.
2. In general, nodes on the network cannot be trusted, and may be lying.
3. Messages sent back and forth might be lost or corrupted in transit, unpredictably.
4. Nodes in the network can be anything; there are no guarantees about the nature or functionality about any comptuer in the network.

Given these constraints, we ultimately see the emergence of several networking principles, which continue to shape the web to this day:

## Standard Protocols

The [Internet Protocol Suite](https://en.wikipedia.org/wiki/Internet_protocol_suite) is a set of protocols used to organize communication on the internet.

This suite is organized into four "layers" of abstraction:

- The Link Layer
- The Internet Layer
- The Transport Layer
- The Application Layer

The **link layer** concerns itself with moving data between computers on a local network. This is the layer which controls the actual transmission of data cross physical medium, like wires or wifi.

The **internet layer** introduces the idea of long-range address (IP addresses, etc), and provides functionality for sending data across multiple networks (hence the term "internet"). This layer provides functionality for identifying the location of source and destination, and for routing data across networks to the correct destination. IP, the addressing protocol, is implemented in this layer.

The **transport layer** concerns itself with getting data from source to destination, reliably and without error. This layer monitors errors, data loss, and manages congestion on the network to ensure that data can move across the network as easily as possible. TCP, the protocol underlying HTTP, etc, is implemented in this layer.

The **application layer** provides the familiar protocols of HTTP (web pages), SMTP (email), FTP (file transfer). These protocols are built on and abstract away the underlying protocols, meaning that knowledge of the inner workings of the other layers is not necessary to use HTTP, etc.

## Authentication

Given that nodes on the network by default cannot be trusted, **authentication** has become a major component of work on the web. Almost all internet users have the experience of logging into sites with a password -- password-based authentication is one of the simplest and most popular modes of authentication.

There are additional types of authentication:

- Logging in via a Google, Facebook, or GitHub account uses a protocol known as ["OAuth"](https://en.wikipedia.org/wiki/OAuth) and removes the need for an additional password.
- RSA cryptography makes it possible to establish authenticity automatically by coordinating a "handshake" using established security keys.
- Two-factor authentication involves a second device (commonly a mobile phone) to verify identity beyond a password.

## Markup Languages

Because there are no guarantees about the nature of the nodes on the network, data sent across the network should be as flexible as possible. In general, [plain text ](https://en.wikipedia.org/wiki/Plain_text) is the most flexible data format, and so data on the web is generally sent as plain text. In order to generate the rich media often found on the web, the node interprets the text and takes the appropriate action.

This is the concept underlying HTML and CSS, the two markup languages powering the majority of the web. More on this in the next section.
