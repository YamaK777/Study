# メインプログラム
from re import S
from flask import Flask, request, session, flash, redirect, render_template
import user_info
import process_image

app = Flask(__name__)
app.secret_key = 'AEgarGer4qrhgJ6rhbe'

# エラー等のメッセまとめ
message=[["ログインに失敗しました"],
        ["入力したIDはすでに使用されています"],
        ["加工内容を選択してください"],
        ["JPG 以外アップできません"],
        ["エラーが発生しました"]
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
  result = session['image']
  return render_template('result.html',src = result[0],process = result[1])

# ユーザ退会確認画面
# ログイン必要
@app.route('/delete')
def delete():
  # ログイン確認
  if not user_info.is_login():
    return redirect('/login')

  return render_template('user_delete_check.html')

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
      flash(message[0][0])
      return redirect('/login')

# ログアウト処理
@app.route('/try_logout')
def logout():
  # セッションを切る+ログインフラグを0に
  if user_info.try_logout():
    # ログイン画面表示へ
    return redirect('/login')

  # ログアウトできなかった場合
  flash(message[4][0], message[4][1])
  return redirect('/')


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
  flash(message[1][0])
  return redirect('/register')

# ユーザ削除処理
@app.route('/try_delete')
def try_delete():

  # ユーザ削除処理
  if user_info.delete_user():
    # ログイン画面へ
    return redirect('/login')

  flash(message[4][0], message[4][1])
  return redirect('/delete')


# 画像加工処理
@app.route('/process_image', methods=['POST'])
def image():
  # 入力した値を取得
  image = request.files['image']
  process = int(request.form.get('process', None))
  # 加工を選択しなかったまたは、ファイルを読み込めなかった
  if process < 0:
    # メイン画面へ
    flash(message[2][0])
    return redirect('/')

  # JPEG ファイル以外は却下する
  if not process_image.is_jpgfile(image.stream):
    flash(message[3][0])
    return redirect('/')

  # イメージの保存+保存先の階層取得
  path = process_image.save_image(image)

  # 画像の加工、保存+保存したフォルダ階層の取得
  if process_image.process_cv2(path,process):
    return redirect('/process_result')

  flash(message[4][0])
  return redirect('/')


if __name__ == '__main__':
    app.run(host='127.0.0.1')
