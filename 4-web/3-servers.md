# Servers

As a web user, you are most often in the role of a consumer of content. This section will consider the role of the supplier of content: the web server.

Web servers provide the following key functionality:

1. Receiving "requests" from the internet, often thousands or millions per second.
2. Processing these requests: determining authenticity and finding the appropriate content.
3. Returning a "response" to the requesting node.

This loop is known as the ["Request-Response Cycle"](https://en.wikipedia.org/wiki/Request%E2%80%93response), and is core to everything on the web.

Over time, a number of open-source web servers have become standard choices for deploying websites. Two in particular, [Apache](https://en.wikipedia.org/wiki/Apache_HTTP_Server) and [Nginx](https://en.wikipedia.org/wiki/Nginx), are responsible for much of the traffic on the internet today. Microsoft's web server remains a popular choice, although it is closed-source.

These web servers are advanced pieces of software, designed to handle thousands of **simultaneous** connections. Ultimately, though, they are no different from other pieces of software -- you could write on yourself, although it would be a difficult challenge for a beginner.

Let's now discuss two types of websites:

# Static Sites

Most of the websites on the early internet were what are now known as "static" sites. This means that the HTML files being returned by the server were saved on the server somewhere, as a regular text file. Everyone who requested that page got the same result, and there was virtually no processing required on the server, other than fetching that HTML file.

# Dynamic Sites

Most of the websites currently on the internet fall into the category known as "dynamic". This means that, as part of the request, the web server does some special processing, just for you.

Consider the Facebook news feed. What you see when you visit Facebook differs greatly from what another person sees. Yet, they are entering the same URI into the address bar. How is this possible?

Dynamic sites have the ability to generate HTML on the fly, based on specifics about the user and the request. In this case, Facebook looks at the user id of the person making the request, and generates customized HTML based on that person's friends. It then returns this HTML to the browser, which renders the news feed.

Another example is that of Google. When you make a Google query, Google's search engines will take this query and find the latest and most relevant information, turn that into HTML, and send it back to you.

Creating customized responses to requests, quickly, at a massive scale, is a major challenge. This is why Facebook and Google are massive companies that employ thousands of engineers.