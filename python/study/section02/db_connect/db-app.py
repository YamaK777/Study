import cx_Oracle
from flask import Flask, render_template

app = Flask(__name__)

# ルートにアクセスがあったとき ---③
@app.route('/')
def index():
  # DBに接続
    con = cx_Oracle.connect('richadmin', 'systemrich', 'localhost:1521')

    # DBを操作するカーソル
    cur = con.cursor()

    # SQL文で検索
    result = cur.execute(
        'SELECT * FROM USERS'
        )

    # 検索結果を抽出
    user_info = result.fetchall()

    # カーソル閉じる
    cur.close()

    # DB切断
    con.close()

    return render_template('db-show.html', users=user_info)


if __name__ == '__main__':
  app.run(host='127.0.0.1')

