import sqlite3
import csv
# 保存先の指定
dbname = 'zip.sqlite'
# DB に接続 ---①
conn = sqlite3.connect(dbname)
# with closing(sqlite3.connect('sqlite_test.db')) as db_connect:
# zipテーブルを作成
conn.execute('''
    CREATE TABLE IF NOT EXISTS zip (
    zip_id INTEGER PRIMARY KEY,
    code TEXT,
    pref TEXT,
    city TEXT,
    town TEXT)
  ''')
# 過去に入っているデータがあれば削除 ---②
conn.execute('DELETE FROM zip')

# CSV を読んで DB に入れる関数 ---③
# fname:ファイル名
def read_csv(fname):
  # sqliteを操作するカーソルオブジェクトを生成
  cur = conn.cursor()
  # with conn.cursor() as cur:
  # csv_file = open("./TEST_STOCK.csv", "r",
  #               encoding="ms932", errors="", newline="")

  # ファイルを開くclose()で閉じる→fname:csvファイル名、encoding:文字型
  # file = open(fname, encoding='cp932')
  # close()入れるのめんどうの場合
  # 参考
  # https://tonari-it.com/python-with-file-open-close/
  with open(fname, encoding="shift-jis") as file:
    # csvファイルを配列(リスト)にする
    reader = csv.reader(file)
    #リスト形式
    # f = csv.reader(csv_file, delimiter=",", doublequote=True,
    #                lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    #辞書形式
    # f = csv.DictReader(csv_file, delimiter=",", doublequote=True,
    #                    lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    # https: // qiita.com/motoki1990/items/0274d8bcf1a97fe4a869:参考
    # 必要なデータを抽出してインサート
    for row in reader:
      code = row[2]
      pref = row[6]
      city = row[7]
      town = row[8]
      if town == '以下に掲載がない場合':
        town = ''
      print(code, pref, city, town)
      # zipテーブルにINSERT
      cur.execute(
          'INSERT INTO zip (code,pref,city,town) ' +
          'VALUES (?,?,?,?)',
          [code, pref, city, town])
    # # ファイルを閉じる
    # file.close()
    # データベースへコミット
    conn.commit()
    # 操作を閉じる
    cur.close()


# 事業所用のデータを DB に入れる関数 ---④
def read_office_csv(fname):
    cur = conn.cursor()
    file = open(fname)
    reader = csv.reader(file)
    for row in reader:
      code = row[7]
      pref = row[3]
      city = row[4]
      town = row[5] + row[6] + ' ' + row[2]
      print(code, pref, city, town)
      conn.execute(
          'INSERT INTO zip (code,pref,city,town) ' +
          'VALUES (?,?,?,?)',
          [code, pref, city, town])
    file.close()
    conn.commit()
    cur.close()



# CSV ファイルを読む ---⑤
read_csv('KEN_ALL.CSV')
read_office_csv('JIGYOSYO.CSV')
# データベースの接続を切る
conn.close()
print('ok')
