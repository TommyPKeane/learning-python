# Python 3.11 (OSI) Networking Examples and Tutorials

<!-- MarkdownTOC -->

- [GraphQL \(`strawberry-graphql`\)](#graphql-strawberry-graphql)
- [RESTful API \(`flask`\)](#restful-api-flask)
- [Fast Webserver \(`tornado`\)](#fast-webserver-tornado)
- [References](#references)

<!-- /MarkdownTOC -->

<a id="graphql-strawberry-graphql"></a>
## GraphQL (`strawberry-graphql`)

GraphQL is an object-oriented-like API standard that can be used for web development as an (arguably) enhanced approach to APIs over the common RESTful API approach.

With GraphQL you have client-server contracts through "Query" standardization ("Graph(-based) Query Language") with defined types/objects and definitions of query parameters (arguments) and response definitions.

One of the major differences between RESTful and GraphQL APIs is that with GraphQL you often use a common endpoint and you have configurable options through the Query format to decide what arguments and response values you want to be included in your query and the server's response.

This means that your Query has optional arguments and parameterized configuration (per the server's provided Query contracts/standards), and you can also tell the server what part of the overall response you want to be returned. With GraphQL, you don't need to always get/accept an entire response, you can actually pre-emptively tell the server what subset of the overall possible response you want. For software and application development, this gives you a level of flexibility that otherwise wouldn't be innately available in a common RESTful API where responses are usually fixed.

There are, of course, ways to support configurability in RESTful `POST` or `GET` requests with your API's server-side application, but then you will also have to document all of that configurability, and essentially you're inventing your own custom approach, even if you follow some semi-standard "best practices". So what GraphQL really offers is a proper standardization of how queries need to be generally structured, and then by your server implementing Schemas for your supported queries, you can then provide those schemas to the client developers so they can implement the queries that they want.

Arguably, this is a major improvement, but any standardization also enforces strictness. So, you may not find that working in GraphQL is _as easy_ as working with a RESTful API, since you need to not only understand `GET` and `POST` HTTP Requests themselves, but you then also need to be strict and stringent in your JSON queries, otherwise you'll get server error messages indicating a failure to construct a valid query. It's not _that_ much more difficult, but it does add another layer to everything, so that's something just to keep in mind.

<a id="restful-api-flask"></a>
## RESTful API (`flask`)

> 👻 _TBD_ ...

<a id="fast-webserver-tornado"></a>
## Fast Webserver (`tornado`)

> 👻 _TBD_ ...

<a id="references"></a>
## References

- https://en.wikipedia.org/wiki/OSI_model
- https://flask.palletsprojects.com/en/2.2.x/ (Web Framework)
- https://www.tornadoweb.org/en/stable/ (Webserver)
- https://strawberry.rocks/ (GraphQL)
