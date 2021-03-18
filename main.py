from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    number = random.randint(1, 50)  # Select a random number from 1 - 50.

    # make_response() builds the HTTP response that Flask sends to our browser.
    # In this case, the HTML code from index.html is used as the argument.
    http_response = make_response(render_template('index.html', number = number))

    cookie_flavor = 'thin mints'  # This string will become the value for the cookie.
    
    # Use the .set_cookie() method to define the name and value for a new cookie.
    http_response.set_cookie('fav_cookie', cookie_flavor)
    # This key/value pair will be sent in the HTTP response and stored as a file on
    # our device.

    return http_response

if __name__ == '__main__':
    app.run()