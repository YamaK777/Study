# 画像加工に関するプログラム
import cv2
from datetime import datetime

from flask.scaffold import F

# 加工前の画像を保存
def save_image(image):
  # 保存先のファイル名を決定
  url='/static/images/'
  file_name = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
  # ファイルを保存
  image.save('/static/images/image.jpg')

  return url

# cv2を使用した加工
def process_cv2(url, select):
  image = None
  # モノクロ加工
  if select == 1:
    image = cv2.imread(url,0)
  # エッジ加工
  elif select == 2:
    image = cv2.Canny(url,50,110)
  # リサイズ加工
  elif select == 2:
    image = cv2.resize(url,200,200)

  return image