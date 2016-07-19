# Files and Filesystems

Under the hood, all the data on your computer is stored on your computer's hard drive, and takes up some small amount of physical space on this drive. Directly reading and writing data to these hard drives is, fortunately, not something you will need to do. The operating system abstracts away these low-level operations, and presents the content of your computer's hard drive in the form of a **file system**.

Data in a file system is stored in discrete units known, unsurprisingly, as **files**. Images are files, as are essays, programs, music, movies, and so on. Everything you interact with in a computer is stored as some sort of file.

Files are organized in a hierarchy of **directories** or **folders**. Here is an example of a simple filesystem:

```
/
    Documents/
        Images/
            catpic.jpg
        Poetry/
            feelings.txt
    Applications/
        Chrome.app
```

In this example, `catpic.jpg`, `feelings.txt`, and `Chrome.app` are examples of files. `Documents`, `Images`, `Poetry`, `Applications`, and `/` are all directories. Note that directories can be nested, creating a file **hierarchy**.

## Paths

When writing software, you will very often need to refer to files. Files are referred to using something known as a **path**. A path describes a location in a filesystem. Going back to our simple filesystem, we can refer to the file `feelings.txt` as follows:

```
/Documents/Poetry/feelings.txt
```

If you ever need to reference this file in a program, you can use this path.