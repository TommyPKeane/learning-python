# Learning Python

__tommy teaches tommy__ (and anyone who wants to actually read this) how to code in Python, with a major focus on all the functionality available in the Python Standard Library (PSL) and Python syntax.

I've been doing various amounts of Python coding since 2009-ish in personal, professional, and academic projects, but you're never too old to learn, and they keep making computers better and worse all the time.

Currently in 2023, I'd say that Python is my preferred programming language and the one in which I feel most experienced.

<!-- MarkdownTOC -->

- [Setup](#setup)
- [What is Python?](#what-is-python)
- [What's this "tommy teaches tommy" thing all about?](#whats-this-tommy-teaches-tommy-thing-all-about)
- [License](#license)
- [References](#references)

<!-- /MarkdownTOC -->

<a id="setup"></a>
## Setup

See the [`CONTRIBUTING.md`](./CONTRIBUTING.md) file for the overall setup design and details about this repository, or how to make sure your system is setup with any prerequisites.

Also note that each self-contained directory will also have a top-level `README.md` file which should explain exactly how to use or run the code contained within.

<a id="what-is-python"></a>
## What is Python?

Python is an interpreted Programming Language, meaning that the written code is passed through an "interpreter" runtime, which reactively parses the code and then runs the interpreted instructions.

<!--
Other interpreted languages are those like Ruby, SQL, JavaScript (TypeScript), R, Julia, and MATLAB (Octave). With an interpreter, the intention is that the code itself is portable between any system where the interpreter can run, and then to run the code you need the relevant interpreter to be installed.

This is in contrast to compiled languages like C, C++, D, _etc._, where you actually take the code and compile it into a self-contained executable or portable library. With compiled languages, as long as the relevant external/shared libraries are available on a system, you can simply bring the compiled executable to that system and run the software without needing to have the compiler installed.
 -->

Python is a relatively strict Object-Oriented Programming (OOP) Language, where almost everything is an object; an instantiation of a `class` definition (custom types). In contrast to a statically-typed language like C++, though, Python is dynamically-typed, meaning that the "variables" (aliases) can refer to different types (classes) throughout the runtime of the code, depending on context/assignment.

So if you define `x = 3` and then later in the same file (module) you say `x = "hello"`, then `x` can separately (in the same program/script) be known as an integer and then as a string.

<a id="whats-this-tommy-teaches-tommy-thing-all-about"></a>
## What's this "tommy teaches tommy" thing all about?

_"What's in a name?"_

You can see a rambly explanation [here at my personal website](https://tommypkeane.com/about-tommy/tommy-teaches-tommy.html); but, in short:

I'm just trying to say that I'm writing out what I think is helpful/interesting to me, and I'm sharing it in case it's helpful to anyone else, but please know that I'm ___not___ trying to talk _down_ to anyone :smile: (except maybe myself :ghost:).

<a id="license"></a>
## License

Copyright (c) 2023, Tommy P. Keane (https://www.tommypkeane.com)

See the [LICENSE](./LICENSE) file for details.


<a id="references"></a>
## References

- https://www.python.org/
- https://pip.pypa.io/en/stable/user_guide/
- https://python-poetry.org/
- https://hub.docker.com/_/python/tags
- https://direnv.net/
