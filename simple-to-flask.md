# Porting our "simple" example to Flask

Let's transfer the pages we set up in our "simple" example over to a Flask-based `app.py`.

We'll cover the basic set up here. See the `flask/app.py` for a finished and fully-commented version.

Recall that we have three pages in the simple site example:

- Home
- Resume
- Contact

The URLs for each page:

- /
- /resume/
- /contact/

We'll need to call `@app.route()` at least three times:

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    @app.route("/resume/")
    @app.route("/contact/")

Which means we'll also need at least three functions:

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        pass

    @app.route("/contact/")
    def contact():
        pass

    @app.route("/resume/")
    def resume():
        pass

Then, we'll use a helper function, `render_template`, for the return value of each function:

    from flask import Flask, render_template

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/contact/")
    def contact():
        return render_template("contact.html")

    @app.route("/resume/")
    def resume():
        return render_template("resume.html")

At this point, we can finish `app.py` by adding this next bit to the very bottom of the file:

    if __name__ == "__main__":
        app.run()

Next, run the app. From the command line, run:

    python app.py

You can run the pre-built example `flask/app.py` by changing to the `flask` directory before running the command above:

    cd flask
    python app.py
