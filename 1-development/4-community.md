# Community

People often ask, "What programming language should I learn?". To answer the question, we will ask a counter-question: "What do you want to do?".

Languages are defined largely by two things: the language itself, and the community built around that language.

Regarding the languages themselves: the differences between them are significant, but not as large as you might think. In general, you can do most things in most languages. A individual programming language represents a set of *choices* about what sorts of things people writing in that language are going to want to do. Something that's easy in language A could be hard in language B, while something easy in language B could be hard in language A.

In general, people programming for data science and data analysis use languages like Python and R: "high-level", interpreted languages that read more or less like english and can be written and run quickly. These languages, as well as similar languages like Ruby, have a great deal in common.

The interesting differences start to emerge when we talk about the **community** built up around these languages.

When writing software, you will find (and may be surprised to find) that only a small fraction (let's say, 1%) of the code you **run** will be code that you actually **wrote**. The rest of your program will involve code written by others.

As an example, let's say I want to save a copy of the Google homepage to my computer. I'd open up the command line and do something like this:

```
>>> import requests
>>> page = requests.get('https://google.com')
```

Here, [requests](http://docs.python-requests.org/en/master/) is the name of a popular third-party library used to make HTTP (web) requests in Python, written primarily by Kenneth Reitz.

Kenneth Reitz saw a problem: making HTTP requests involved a lot of annoying and complex code. Programmers who needed to do this would spend a lot of time struggling to get their requests to work. They were also generally doing the same thing again and again.

So Kenneth went ahead and wrote some code to make HTTP requests very easily, and released the code as an **open-source library** that anyone else could download and use. Now, instead of figuring it out themselves, Python programmers just use Requests. This saves everyone **a lot** of time.

A huge amount of programming involves leveraging the work of others, and so the choice of language matters in that it determine what open-source libraries you'll be able to rely on in your programming.

The **Ruby** language, for example, is very popular among web developers. As a result, there are a ton of [great open-source libraries](https://rubygems.org/) available for doing web things in Ruby.

The **R** language, as another example, is mega popular among statisticians and data analysis. As a result, there are a ton of [great open-source libraries](https://cran.r-project.org/) available for doing statistics and data analysis in R.

The **Python** language, as yet another example, is very popular among both data analysts **and** web developers. As a result, there are a ton of [great open-source libraries](https://pypi.python.org/pypi) for doing data processing and web work in Python. But these libraries are different from the ones in Ruby and R.

They key takeaways from this section are:

1. A lot of programming involves finding ways of re-using the work of others.

2. Your choice of langauge will determine what libraries you can draw on to do the things you want to do.

