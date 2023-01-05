from flask import Flask, request, render_template, make_response, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "this_is_not_a_good_key"

@app.route('/')
def index():
    number = random.randint(1, 50)

    http_response = make_response(render_template('index.html', number = number))
    cookie_flavor="Chocolate Chip"
    http_response.set_cookie("Favorite Cooke", cookie_flavor)
    return http_response


if __name__ == '__main__':
    app.run()