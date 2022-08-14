from flask import Flask, request, render_template
from app.frontend import frontend


# Set up debug boolean to pass on
debug = True
# debug = False


def flask():
    app = Flask(__name__, template_folder='app/htmlforms')

    @app.route('/')
    def starting_page():
        return render_template('text-form.html', words="Enter sentence")

    @app.route('/', methods=['POST'])
    def print_page():
        text = request.form['text']
        return render_template('text-form.html', words=frontend.input_system(frontend, text, debug))

    return app


if __name__ == "__main__":
    myapp = flask()
    myapp.run()
