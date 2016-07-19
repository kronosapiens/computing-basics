# Git

In many fields, but most of all in software, version matters. Software products are in constant states of change. Software projects almost always require the collaboration of multiple people. Managing all of this activity can be challenging. Enter Git.

Git is a tool for recording change over time, making it easier for people working on software to make sure they both have the correct and up-to-date version of their code, but also to be able to go back and see where and why changes were made. Known as source control, this bookkeeping is now fundamental in modern software development.

The core unit of Git is the **repository**. A repository can be thought of as unit being remembered. Work on repositories are saved in chunks known as **commits**. A commit can be thought of as a unit of memory. Developing software is then a process of committing changes to a repository representing the software project.

Some benefits of using Git:

1. Easy to restore files if they have been lost or damaged
2. Easy to get changes to files or folders without having to re-download the entire file or folder

There are more, but these two are so useful that rather than enumerate them it may be best to pause and reflect on these instead. Git, like many things, is a program.

GitHub, on the other hand, is a website which makes it easy to collaborate with others via the internet. GitHub uses Git as a foundation, and builds on it. This distinction is subtle but worth knowing.

Using Git involves understanding a handful of commands. Here are most of them:

`git clone <url to repo>` – clone a repository from GitHub to your computer

`git add .` – prepare all modified files for the next commit

`git commit -am "<commit message>"` – make a commit, with the message `<commit message>`

`git push` – “push” new changes **to** GitHub

`git pull` – “pull” new changes **from** GitHub

# Activity: Learn Git

Throughout the rest of this curriculum, you will be asked to modify and run code samples included in this repository. Before you can do that, you will need to get the code samples on your computer. To do that, you'll first learn Git.

1. Work through [this tutorial](https://try.github.io/levels/1/challenges/1).
2. Make a GitHub Account. Everyone who writes programs for anything has one. It’s like having an email address. If you don’t have one people will think you’re weird and won’t hire you.
3. **Clone this curriculum to your computer.**
