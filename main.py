from flask import Flask, request, render_template
import random

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    number = random.randint(1, 50)

    return render_template('index.html', number = number)

if __name__ == '__main__':
    app.run()