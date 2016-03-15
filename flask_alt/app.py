"""
Here we import a big list of names that we'll use as
the basis for our individual kitten pages
"""
import json

"""
Use the ALT_NAMES one of two ways:

1. Import from alt_names.py

    from alt_names import ALT_NAMES

2. Read from alt_names.json and use the json module to create a Python list data structure:
"""
with open('alt_names.json', 'r') as f:
    ALT_NAMES = json.loads(f.read())

"""
This import statement brings in the core Flask class
and a helper function which will allow us to render
the pages of our app and send them back to the user
"""
from flask import Flask, render_template

"""
Here, we create an instance of a Flask app.

We use the global `__name__` variable in doing so.

Don't worry too much about why we use `__name__` here, just
know that this is a Flask convention.

If you'd like, you can read more about the arguments
you can pass to Flask here: http://flask.pocoo.org/docs/0.10/api/#flask.Flask
"""
app = Flask(__name__)

"""
This defines the "route" for the homepage.

In other words, when a browser sends a request to our server
for the "/" URL, this function will handle the response to
said request.
"""
@app.route("/")
def home():
    """
    Here, we're just returning the contents of the files in the flask/templates/home.html file
    """
    first_names = map(lambda x: x.get('name'), ALT_NAMES)
    return render_template("home.html", names=first_names)


@app.route("/contact/")
def contact():
    """
    Again, we're simply returning the contents of a file.
    In this case, the flask/templates/contact.html file
    """
    return render_template("contact.html")


@app.route("/resume/")
def resume():
    """
    Return the contents of flask/templates/resume.html
    """
    return render_template("resume.html")


"""
Here we define a route for individual kitten pages.

The <name> you see here is a placeholder for whatever value is
in the URL when the request is made to our server.

The kitten function will handle requests for any URL that matches
this pattern:

    /kitten/adam
    /kitten/ben
    /kitten/jack
    /kitten/julia
    /kitten/NONSENSEGOESHERE

    etc.

The value of <name> corresponds with the value of the name parameter
that the kitten functions takes as its argument.
"""
@app.route('/kitten/<name>')
def kitten(name):
    """
    In this first line of the `kitten` function, we try to locate the passed name
    in the big list of `FIRST_NAMES` that we imported at the top of this file.

    We use `name.upper()` to make the name all caps, since all of the names in
    the `FIRST_NAMES` list are all caps.

    We use `FIRST_NAMES.index` to try to locate the requested name. If the requested name
    is present in `FIRST_NAMES`, `FIRST_NAMES.index(name.upper())` will return an
    integer greater than or equal to 0.

    If it is not present, Python will raise a ValueError exception. In this case, we'll
    explicitly set the value of index to -1.

    /kitten/jack
    """
    try:
        cat = filter(lambda x: x.get('name').lower() == name, ALT_NAMES)[0]
    except IndexError:
        cat = False

    if cat:
        """
        If the value stored in the variable `index` is greater than or equal to 0,
        we know we have a valid request and can return a page for the individual kitten.

        We use the `render_template` function to render the contents of the
        flask/templates/kitten.html file, and we pass in the dynamically determined value
        of `name` using the properly capitalized version of the name that was requested.

        In the flask/templates/kitten.html file, look for: {{ name }} to see how/where
        the dynamic value is placed.
        """
        return render_template(
            "kitten.html", name=cat.get('name'), desc=cat.get('desc'), photo=cat.get('photo'))
    else:
        """
        If the value stored in the variable `index` is not greater than or equal to 0
        (read: -1), then we don't have a kitten by that name.

        Respond to the request with a "404 Not Found" error.
        """
        return "Couldn't find a kitten named %s!" % name.capitalize(), 404


if __name__ == "__main__":
    """
    Setting the value of `app.debug` to `True` means we will see explicit
    error messages when thing go wrong, helping us to track down any issues
    we find in our application.
    """
    app.debug = True

    """
    Start the app!
    """
    app.run()
