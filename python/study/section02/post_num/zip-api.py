# -*- coding: Shift-JIS -*-

from flask import Flask, request
import sqlite3
import os
import json

# 郵便番号のデータベースのパスを特定 ---①
base_path = os.path.dirname(os.path.abspath(__file__))
db_path = base_path + '/zip.sqlite'
form_path = base_path + '/zip-form.html'
# Flask を取り込む ---②
app = Flask(__name__)
# ルートにアクセスがあったとき ---③
@app.route('/')
def index():
  with open(form_path) as f:
    return f.read()

# API にアクセスがあったとき ---④
@app.route('/api')
def api():
  # パラメータを取得 ---⑤
  q = request.args.get("q", "")
  # データベースから値を取得 ---⑥
  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  c.execute(
      'SELECT pref,city,town FROM zip WHERE code=?',
      [q])
  items = c.fetchall()
  conn.close()
  # 結果を JSON で出力 ---⑦
  res = []
  for i, r in enumerate(items):
    pref, city, town = (r[0], r[1], r[2])
    res.append(pref + city + town)
    print(q, ":", pref + city + town)
  return json.dumps(res)

# Flask を開始する ---⑧
if __name__ == '__main__':
  app.run(host='127.0.0.1')
