from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
  # テンプレートエンジンにデータを指定する
  return render_template('card-age.html',
                          username='リッチ太郎',
                          age=23,
                          email='teacher@richitschool.com')

if __name__ == "__main__":
  app.run(host='127.0.0.1')
