from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
  # URL パラメータを取得(--①)
  x = request.args.get('x')
  y = request.args.get('y')
  # パラメータが設定されているか確認する(--②)
  if(x is None) or (y is None):
    return 'パラメータが足りません。'

  # パラメータを数値に変換して計算する(--③)
  c = int(x) + int(y)
  # 結果を出力する(--④)
  return '<h1>' + str(c) + '<h1>'


if __name__ == '__main__':
  app.run(host='127.0.0.1')
