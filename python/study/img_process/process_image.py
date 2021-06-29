# 画像加工に関するプログラム
import os
import cv2
from datetime import datetime
from flask import session

# 保存先のディレクトリの指定
app_dir = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = '/static/images'

messe = ["モノクロ","エッジ","リサイズ"]


# 加工前の画像を保存
def save_image(image):

  # 保存先のファイル名を決める
  time_s = datetime.now().strftime('%Y%m%d%H%M%S')
  fname = time_s + '.jpg'
  path = IMAGES_DIR + '/' + fname
  dir = app_dir + path
  # 一時ファイルを保存先ディレクトリへ保存
  image.save(dir)
  # 保存した画像(位置)を返す
  return path

# cv2を使用した加工
def process_cv2(path, process):
  dir = app_dir + path
  # モノクロ加工
  if process == 1:
    p_image = cv2.imread(dir,0)
  # エッジ加工
  elif process == 2:
    image = cv2.imread(dir,0)
    p_image = cv2.Canny(image,50,110)
  # リサイズ加工
  elif process == 3:
    image = cv2.imread(dir)
    p_image = cv2.resize(image,(200,200))

  # 加工後の画像を保存
  cv2.imwrite(dir,p_image)
  print(path)
  p_result = [path,messe[process-1]]
  # セッションスコープにdirを格納
  session['image'] = p_result
  return True


# JPEG ファイルかどうかを確認する
def is_jpgfile(image_stream):
  byte = image_stream.read(2) # 先頭 2 バイトを読む
  image_stream.seek(0) # ポインタを先頭に戻す
  return byte[:2] == b'\xFF\xD8'

