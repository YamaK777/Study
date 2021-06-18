from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('card-age.html',
                            username='フラスク',
                            age=18,
                            email='flask@flask.com')

if __name__ == "__main__":
  app.run(host='127.0.0.1')
