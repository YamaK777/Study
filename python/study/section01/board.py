from flask import Flask, request, redirect
import os
app = Flask(__name__)
# データの保存先 --①
DATAFILE = './board-data.txt'

# ルートにアクセスしたとき --②
@app.route('/')
def index():
    msg = 'まだ書き込みはありません'
    # 保存データを読み込み --③
    if os.path.exists(DATAFILE):
      with open(DATAFILE, 'rt') as f:
        msg = f.read()
    # メッセージボードと投稿フォーム --④
    return """
      <html><body>
      <title>掲示板</title>
      <h1>メッセージボード</h1>
      <div style="background-color:yellow; padding:3em;">{0}</div>
      <h3>ボードの内容を更新する：</h3>
      <form action="/write" method="POST">
      <textarea name="msg" rows="6" cols="60"></textarea><br/>
      <input type="submit" value="書込">
      </form>
      </body></html>
      """.format(msg)
# POST メソッドで/write にアクセスしたとき --⑤


@app.route('/write', methods=['POST'])
def write():
    # データファイルにメッセージを保存する --⑥
    # POST メソッドで送信したフォームの値を受け取る
    if 'msg' in request.form:
      msg = str(request.form['msg'])
      with open(DATAFILE, 'wt') as f:
          f.write(msg)
    #ルートページにリダイレクトする --⑦
    return redirect('/')
if __name__ == "__main__":
  app.run(host='127.0.0.1')
