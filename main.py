from flask import Flask, request, render_template, make_response

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():

   return render_template('index.html')

if __name__ == '__main__':
   app.run()

Here is the breakdown