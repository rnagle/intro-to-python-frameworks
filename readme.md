# Introduction to Python Frameworks

## Framework

A fundamental structure used as the support for something being built.

More literally: skeletal support. Like the frame of the house:

![Wood frame house](wood-frame-house.jpg)

## These are building blocks you can use to save yourself time.

Build on the work of other smart people that came before you.

### Example: building a modest web site

Let's say we want to build a site with three pages:

- Home
- Resume
- Contact

The URLs for each page:

- /
- /resume/
- /contact/

Python has minimal web server built-in that can help you get up and running: [SimpleHTTPServer](https://docs.python.org/2/library/simplehttpserver.html)

### Using the SimpleHTTPServer

You can fire up a web server for testing by changing to a directory and running:

    python -m SimpleHTTPServer

This will run a server at this address: `localhost:8000`.

With this, you'll be able to view your files with a web browser.

Try this by going to the `simple` directory and running `python -m SimpleHTTPServer`.

### Drawbacks

- SimpleHTTPServer is *not* a production-ready solution
- It does not support dynamic pages out of the box

## What if I want to serve dynamic content?

Serving dynamic content means having a web server interpret the requested URL and deliver a page that it renders on-the-fly.

In other words, there are no static HTML files.

For example, if you wanted to add pages to your simple resume to share information about your pets, you might want to do so via dynamic pages.

Let's say you have A LOT of cats. An entire spreadsheet worth of cats. How might you save yourself a bit of time and still achieve a page per cat?

## Using Flask

[Flask](http://flask.pocoo.org/) calls itself "a microframework for Python."

It provides a relatively simple way of building dynamic web applications.

*Aside:*

A bespoke solution probably isn't the right approach no matter if you're building a website or processing a dataset. Someone else has probably dealt with a similar issue and published open source code that can help.

Take a look at the [complexity of Flask](https://github.com/mitsuhiko/flask), for example:

- Large code base with many thousands of lines of code.
- Large user base/community, which means lots of users to test and file bug reports.
- [Unit tests](https://en.wikipedia.org/wiki/Unit_testing) written and [run regularly](https://travis-ci.org/mitsuhiko/flask) to help the developers ensure the software is stable.

Check the [Python Package Index](https://pypi.python.org/pypi) and [Github](http://github.com/) before you write your own custom solution.

### Flask app essentials

Set up is a two-part process:

Installation:


    pip install Flask


Structure of an `app.py` file:


    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()


See the project's homepage: http://flask.pocoo.org/

These nine lines of code comprise a fully-functioning Flask application. Let's take a look at what's going on here...

### Defining routes

In the example above, note the line: `@app.route("/")`. This is a route definition.

Routes are equivalent to URLs. By defining routes, you explicitly specify the URLs your application will respond to.

Take the example above:

    @app.route("/")
    def hello():
        return "Hello World!"

Below `@app.route("/")`, we're defining a function called "hello" which returns a value of "Hello World!"

In other words, we're saying "when the '/' URL is requested, respond with the string, 'Hello World!'"

*Aside:* the `@app.route("/")` is called a function decorator (indicated by the "@" prefix).

No need to worry much about how function decorators work behind the scenes. What's important is the function decorator applies to the function that immediately follows it.

So, in this example `@app.route("/")` applies to `def hello()`.

### Routes for our site:

To start, we'll transfer all of the pages from our "simple" example over to a Flask-based `app.py` file.

[Read about the set up of our `app.py` file](/simple-to-flask.md).

### As promised, dynamic pages for our cats:

[We'll cover setting up dynamic routes in our `app.py` file](/dynamic-kittens.md).

## Resources:

- [Flask homepage](http://flask.pocoo.org/)
- [SimpleHTTPServer](https://docs.python.org/2/library/simplehttpserver.html)
- [More about function decorators.](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)
- [Errors and Exceptions](https://docs.python.org/2/tutorial/errors.html)
