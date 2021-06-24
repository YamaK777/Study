# メインプログラム
from os import name
from typing import Annotated
from flask import Flask, request, session, redirect, render_template
import user_info

app = Flask(__name__)
app.secret_key = 'AEgarGer4qrhgJ6rhbe'


# メイン画面
# ログイン必要
@app.route('/')
def index():
  # ログイン確認
  if not user_info.is_login():
      return redirect('/login')

  return render_template('index.html', name=user_info.get_name())

# ログイン画面
@app.route('/login')
def login():
  return render_template('user_login.html')

# ユーザ登録画面
@app.route('/register')
def register():
  return render_template('user_regist.html')

# ユーザ登録完了画面
@app.route('/register_complete')
def register():
  return render_template('user_regist_complete.html')

# ログイン処理
@app.route('/try_login', methods=['POST'])
def try_login():
  # 入力した値を取得
  id = request.form.get('id', '')
  name = request.form.get('name', '')
  pas = request.form.get('password', '')

  # ログインチェック
  if user_info.try_login(id, name, pas):
      # メイン画面へ
      return redirect('/')
  else:
      # ログイン画面へ
      return redirect('/login')

# ログアウト処理
@app.route('/try_logout')
def logout():
  # セッションを切る+ログインフラグを0に
  user_info.try_logout()
  # ログイン画面表示へ
  return redirect('/login')

# ユーザ登録処理
@app.route('/try_register')
def try_register():
  # 入力した値を取得
  id = request.form.get('id', '')
  name = request.form.get('name', '')
  pas = request.form.get('password', '')


  # ユーザ登録完了画面へ
  return redirect('/register_complete')







if __name__ == '__main__':
    app.run(host='127.0.0.1')
