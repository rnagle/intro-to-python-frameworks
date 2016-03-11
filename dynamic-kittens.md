# A dynamic page for each of our cats

See the `flask/app.py` for a finished and fully-commented version.

For this part of the app, let's assume we have one cat per unique name identified in US Census data (see: `flask/first_names.py`).

That would mean we have 5,000+ cats. Creating individual HTML files for each would be a burden. Instead, we can tell our Flask app to dynamically generate a page per cat.

We'll start with defining a route:

    @app.route('/kitten/<name>')
    def kitten(name):
        pass

The `<name>` in the route definition is a placeholder for whatever value happens to be in the URL.

For example, this route definition would respond to requests for '/kitten/adam' as well as '/kitten/not_a_name'

The value of `<name>` corresponds to the `name` parameter passed to the `kitten()` function.

So, the next thing we'll do is lookup the name in our list of first names:

    @app.route('/kitten/<name>')
    def kitten(name):
        try:
            index = FIRST_NAMES.index(name.upper())
        except ValueError:
            index = -1

If you're not familiar with `try` and `except`, don't worry. You can read more about them here: [Errors and Exceptions](https://docs.python.org/2/tutorial/errors.html).

What this block of code means is:

1. Try to find the value of `name` in the list of `FIRST_NAMES`
2. If we find the `name`, store its numerical index in the `FIRST_NAMES` list in the variable `index`.
3. If we can't fine the `name`, we've encountered an exception. Store `-1` in the variable `index`.

A non-negative number stored in the variable `index` means we have a match. Since our list of names contains over 5,000 names, this non-negative number can be anything in the range 0-5000+.

The next thing we'll do is check the value of `index` and either:

Return a dynamically-rendered page for our kitten

*OR*

Return an error message to let our users know we don't have a kitten by that name (e.g., a 404 Not found error)

    @app.route('/kitten/<name>')
    def kitten(name):
        try:
            index = FIRST_NAMES.index(name.upper())
        except ValueError:
            index = -1
        if index >= 0:
            return render_template("kitten.html", name=name.capitalize())
        else:
            return "Couldn't find a kitten named %s!" % name.capitalize(), 404

Again, at the very bottom of the `app.py` file, we should have:

    if __name__ == "__main__":
        app.run()

Next, run the app. From the command line, run:

    python app.py

You can run the pre-built example `flask/app.py` by changing to the `flask` directory before running the command above:

    cd flask
    python app.py

Then visit [http://localhost:5000/kitten/adam](http://localhost:5000/kitten/adam) to see your code in action!

Also try visiting a non-name URL: [http://localhost:5000/kitten/not_a_name](http://localhost:5000/kitten/not_a_name) to see your code fall back gracefully.
