from flask import Flask, request, session, redirect
app = Flask(__name__)
# セッション情報を暗号化するキー
app.secret_key = '8ATwIbtrE8w'  # 適当な値を設定 ---①


@app.route('/')
def index():
    # ユーザー名の入力フォームを出力 ---②
    return """
      <html><body><h1>ユーザー名を入力</h1>
      <form action="/setname" method="GET">
      名前: <input type="text" name="username">
      <input type="submit" value="開始">
      </form></body></html>
      """


@app.route('/setname')
def setname():
  # GET の値を取得 ---③
  name = request.args.get('username')
  if not name:
    return redirect('/')
  # セッションに値を保存 ---④
  session['name'] = name
  # 他のページにリダイレクト ---⑤
  return redirect('/morning')


def getLinks():
    return """
      <ul><li><a href="/morning">朝の挨拶</a></li>
      <li><a href="/hello">昼の挨拶</a></li>
      <li><a href="/night">夜の挨拶</a></li></ul>
      """


@app.route('/morning')
def morning():
    # セッションに name があるか確認 ---⑥
    if not ('name' in session):
      # name がない場合は入力フォームに飛ばす ---⑦
      return redirect('/')
    # セッションからユーザー名を得る ---⑧
    name = session['name']
    return """
      <h1>{0}さん、おはようございます！</h1>{1}
      """.format(name, getLinks())


@app.route('/hello')
def hello():
    if not ('name' in session):
      return redirect('/')
    # セッションから名前を得てメッセージ出力 ---⑨
    return """<h1>{0}さん、こんにちは！</h1>{1}
      """.format(session['name'], getLinks())


@app.route('/night')
def night():
    if not ('name' in session):
      return redirect('/')
    # セッションから名前を得てメッセージ出力 ---⑩
    return """<h1>{0}さん、こんばんは！</h1>{1}
      """.format(session['name'], getLinks())


if __name__ == '__main__':
    app.run(host='127.0.0.1')
