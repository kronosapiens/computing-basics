# Browsers

There are many types of nodes on the web:

- Google bots crawl the web, indexing web pages for search.
- Internet of Things devices are sending data to remote servers.
- Printers are listening for print instructions.
- Humans are using web browsers to view content online.
- Etc.

One of the most common and familiar types of node is the personal computer, accessing the web via a piece of software known as a ["web browser"](https://en.wikipedia.org/wiki/Web_browser). Popular web browsers include Google Chrome, Microsoft Internet Explorer, Apple Safari, Opera, Mozilla Firefox, and more.

Ultimately, a web browser is a piece of software (if you wanted, you could write one yourself) designed to make it easy to view content on the web. A browser has the following three capabilities:

1. Take a human-readable URI ([Uniform Resource Identifier](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)) and locate and retrieve the desired content.
2. Receive the desired content, and render it as appropriate for the user.
3. Allow the user to follow links and retrieve new content as necessary.

# HTML & CSS

Ocassionally, browsers are used to download files. In this case, the behavior is straightforward: take the entire file and save it to the computer. What happens afterwards is not the browser's concern.

More often, browsers are used to download web pages. In this case, the browser has additional responsibilities: it must **display** the page for the user. This may seem simple, but realize that there are many browsers, and many computers, each with different abilities. How a page looks is ultimately a function of many things: computer power, supporting software, screen size, and so on. A user might have impaired vision, and so request that all text be displayed extra-large. In order to allow for this kind of flexibility, web pages are not sent as they ultimately appear, but rather as text with a special kind of formatting, or markdown.

This formatting comes in two flavors: HTML (Hypertext Markup Language) and CSS (Cascading Style Sheets). Each plays an important role in displaying web pages.

Let's consider an example of a simple page, a chapter of a book. This page consists of two things: the title of the chapter, and several paragraphs, consisting of the chapter's body. Here's what the raw HTML might look like:

```
<body>
    <h1>Book 1</h1>

    <p>
        Tell me, O muse, of that ingenious hero who travelled far and wide after
        he had sacked the famous town of Troy. Many cities did he visit, and
        many were the nations with whose manners and customs he was acquainted;
        moreover he suffered much by sea while trying to save his own life and
        bring his men safely home; but do what he might he could not save his men,
        for they perished through their own sheer folly in eating the cattle of
        the Sun-god Hyperion; so the god prevented them from ever reaching home.
        Tell me, too, about all these things, O daughter of Jove, from whatsoever
        source you may know them.
    </p>

    <p>
        So now all who escaped death in battle or by shipwreck had got safely
        home except Ulysses, and he, though he was longing to return to his wife
        and country, was detained by the goddess Calypso, who had got him into a
        large cave and wanted to marry him. But as years went by, there came a
        time when the gods settled that he should go back to Ithaca; even then,
        however, when he was among his own people, his troubles were not yet
        over; nevertheless all the gods had now begun to pity him except Neptune,
        who still persecuted him without ceasing and would not let him get home.
    </p>
</body>
```

Notice how in addition to the text, we have some letters in brackets. These are known as "html tags", and they are how we tell the browser what the page is supposed to look like. The `h1` tag is known as the "header 1" tag, and tells the browser that this is a major headline. The `p` tag is known as the "paragraph" tag, and tells the browser that the text is regular body text. Notice also that the tags come in pairs: the first is the "opening" tag, and the second, with the `/`, is the "closing" tag. Everything after the opening tag and before the closing tag is contained inside that tag. This is how HTML communicates the **structure** of the page.

In addition to structure, we need to tell the browser how to format based on structure. This is where CSS comes in. CSS lets us define the **styles** to apply to different parts of the page, i.e. make paragraph text blue, make h1 text size 40 font. Let's see an example:

```
h1 {
  font-size: 24pt;
  color: purple
}

p {
  font-size: 12pt;
  color: green
}
```

The browser will download both the HTML and CSS at the same time, and then decide how to show the page by looking at the CSS, the user's settings, the size of the screen, and the capabilities of the browser itself.

This separation, of structure from style and from both structure and style from presentation, has proven very effective in allowing a large variety of nodes to interact together via a common interface.

# JavaScript

In the last few years, more and more websites have begun using JavaScript to add additional features beyond what is possible with HTML and CSS. While HTML and CSS are markup languages, JavaScript is a full-blown programming language, and has given websites the ability to function more and more like regular pieces of software.

JavaScript programming has many parallels to the Python and R programming discussed in earlier chapters, with additional quirks brought on by the need to deploy this code on the internet.

# Markdown

HTML is what's known as a "markup language", which refers to the use of tags and other types of plain text "markup" to define things like structure and style. Markdown is a popular language for writing text documents, as it makes it easy to define things like headers and styles in plain text. As an example, this curriculum was written in Markdown. If you view the raw `.md`. files in this curriculum (instead of via Github, which renders markdown), you'll see that headers,  code snippets, and so on are defined via simple text markup.

Contrast this with "rich text" software like Microsoft Word, in which styling is saved in a special format (in this case, `.docx`), which can only be read by specialized programs.