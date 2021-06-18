from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
  username = 'リッチ太郎'
  age = 23
  email = 'teacher@richitschool.com'
  return render_template('card.html',
    username=username,
    age=age,
    email=email)

if __name__ == '__main__':
  app.run(host='127.0.0.1')
