from flask import Flask, request, redirect
from datetime import datetime
import os
# 保存先のディレクトリと URL の指定 ---①
IMAGES_DIR = './static/images'
IMAGES_URL = '/static/images'

app = Flask(__name__)
@app.route('/')
def index_page():
  # アップロードフォーム ---②
  return """
  <html>
  <body><h1>アップロード</h1>
  <form action="/upload" method="POST" enctype="multipart/form-data">
  <input type="file" name="upfile">
  <input type="submit" value="アップロード">
  </form>
  </body></html>
  """
@app.route('/upload', methods=['POST'])
def upload():
  # アップされていなければトップへ飛ばす ---③
  if not ('upfile' in request.files):
    return redirect('/')
  # アップしたファイルのオブジェクトを得る ---④
  temp_file = request.files['upfile']
  # JPEG ファイル以外は却下する ---⑤
  if temp_file.filename == '':
    return redirect('/')
  if not is_jpgfile(temp_file.stream):
    return '<h1>JPG 以外アップできません</h1>'
  # 保存先のファイル名を決める ---⑥
  time_s = datetime.now().strftime('%Y%m%d%H%M%S')
  fname = time_s + '.jpg'
  # 一時ファイルを保存先ディレクトリへ保存 ---⑦
  temp_file.save(IMAGES_DIR + '/' + fname)
  # 画像の表示ページへ飛ぶ
  return redirect('/photo/' + fname)


@app.route('/photo/<fname>')
def photo_page(fname):
  # 画像ファイルがあるか確認する ---⑧
  if fname is None: return redirect('/')
  image_path = IMAGES_DIR + '/' + fname
  image_url = IMAGES_URL + '/' + fname
  if not os.path.exists(image_path):
    return '<h1>画像がありません</h1>'
  # 画像を表示する HTML を出力する ---⑨
  return """
  <h1>画像がアップロードされています</h1>
  <p>URL: {0}<br>File: {1}</p>
  <img src="{0}" width="400">
  """.format(image_url, image_path)


# JPEG ファイルかどうかを確認する ---⑩
def is_jpgfile(fp):
  byte = fp.read(2) # 先頭 2 バイトを読む
  fp.seek(0) # ポインタを先頭に戻す
  return byte[:2] == b'\xFF\xD8'


if __name__ == '__main__':
  app.run(host='127.0.0.1')