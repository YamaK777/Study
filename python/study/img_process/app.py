# メインプログラム
from os import error, name
from typing import Annotated
from flask import Flask, request, session, flash, redirect, render_template
import user_info
import process_image

app = Flask(__name__)
app.secret_key = 'AEgarGer4qrhgJ6rhbe'

# エラー等のメッセまとめ
message=[["ログインに失敗しました","failed"],
        ["入力したIDはすでに使用されています","failed"],
        ]


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
def register_complete():

  return render_template('user_regist_complete.html')

# 加工後の画像表示画面
# ログイン必要
@app.route('/process_result')
def process_result():
  # ログイン確認
  if not user_info.is_login():
      return redirect('/login')
  image = request.args.get('image', None)
  return render_template('result.html', image=image)

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
      flash(message[0][0], message[0][1])
      return redirect('/login')

# ログアウト処理
@app.route('/try_logout')
def logout():
  # セッションを切る+ログインフラグを0に
  user_info.try_logout()
  # ログイン画面表示へ
  return redirect('/login')

# ユーザ登録処理
@app.route('/try_register', methods=['POST'])
def try_register():
  # 入力した値を取得
  id = request.form.get('id', '')
  name = request.form.get('name', '')
  pas = request.form.get('password', '')
  # 登録処理
  if user_info.register_user(id, name, pas):
    # 登録完了
    # ユーザ登録完了画面へ
    return redirect('/register_complete')

  # 登録済みの情報があった
  # # ユーザ登録画面へ
  flash(message[1][0], message[1][1])
  return redirect('/register')

# 画像加工処理
@app.route('/process_image', methods=['POST'])
def create_image():
  # 選択した値を取得
  image = request.files.get('image', None)
  process = int(request.form.get('process', None))

  # 加工を選択しなかったまたは、ファイルを読み込めなかった
  if process < 0 or not image:
    # メイン画面へ
    flash("画像の加工に失敗しました", "failed")
    return redirect('/')

  #画像を一時保存するフォルダ階層を取得
  url = process_image.save_image(image)
  # 加工処理
  image = process_image.process_cv2(url,process)

  return redirect('/register_complete',image = image)

if __name__ == '__main__':
    app.run(host='127.0.0.1')
