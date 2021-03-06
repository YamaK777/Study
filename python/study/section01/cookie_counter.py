from flask import Flask
from flask import make_response, request  # Cookie のため ---①
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def index():
    # Cookie の値を取得 ---②
    cnt_s = request.cookies.get('cnt')
    if cnt_s is None:
      cnt = 0
    else:
      cnt = int(cnt_s)

    # 訪問回数カウンタに 1 加算 ---③
    cnt += 1
    response = make_response("""
      <h1>訪問回数: {}回</h1>
      """.format(cnt))
    # Cookie に値を保存 ---④
    max_age = 60 * 60 * 24 * 90  # 90 日(秒)
    # 有効期限の日時を表す,今日+
    expires = int(datetime.now().timestamp()) + max_age
    response.set_cookie('cnt', value=str(cnt),
                        max_age=max_age,
                        expires=expires)
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
