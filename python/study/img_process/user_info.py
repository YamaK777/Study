# ユーザー情報に関するプログラム
import cx_Oracle
from flask import session, redirect

# DB接続用
def DB_connect():
    # DBに接続
    con = cx_Oracle.connect('img_process', 'systemrich', 'localhost:1521')

    # DBを操作するカーソル
    cur = con.cursor()
    # カーソルを戻り値に
    return con, cur

# DB切断用
def DB_disconnect(cur):
    # カーソル閉じる
    cur.close()

    # DB切断
    cx_Oracle.connect('img_process', 'systemrich', 'localhost:1521').close()

# ログインしてるか確認
def is_login():
    return 'login' in session


# ログイン機能
def try_login(id, name, pas):
    # DBの接続
    con, cur = DB_connect()

    # SQL文で検索
    login_result = cur.execute(
        'SELECT * FROM USER_INFO WHERE USER_ID = :user_id AND USER_NAME = :user_name AND PASSWORD = :password',
        user_id=id,
        user_name=name,
        password = pas)

    # 検索結果を抽出
    user_info = login_result.fetchall()

    # 情報なし
    if user_info == []:
        # DB切断
        DB_disconnect(cur)
        return False

    # 情報アリ
    # セッションにユーザー情報を格納→一応インジェクション対策
    session['login'] = user_info[0]
    # DB内のログインフラグを変更
    # cur.execute(
    #     'UPDATE USER_INFO SET LOGIN_FLAG = 1 where USER_ID = :id',
    #     id = user_id)
    # 変更をコミット
    # con.commit()

    # DB切断
    DB_disconnect(cur)
    return True

# ログアウト機能
def try_logout():
    # # DBの接続
    # cur = DB_connect()

    # # DB内のログインフラグを変更
    # cur.execute(
    #     'UPDATE USER_INFO SET LOGIN_FLAG = 0 where USER_ID = :id;',
    #     id=session['login'][0])

    # # DB切断
    # DB_disconnect(cur)

    session.pop('login', None)
    return True


# セッションからユーザー名を得る
def get_name():
    if is_login():
        user = session['login']
        name = user[1]
        return name
    return 'not login'

# ユーザ登録
def regist_user(id,name, pas):
    # DBに接続
    cur = DB_connect
    # DBにユーザIDがすでにあるか
    cur.execute('INSERT INTO USER_INFO VALUES (:user_id,:user_name,:password, DEFAULT)',
                user_id = id,user_name=name, password=pas)
    # DB切断
    DB_disconnect(cur)
