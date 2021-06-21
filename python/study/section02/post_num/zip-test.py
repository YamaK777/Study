import sqlite3

#テスト用の郵便番号
code = '4600022'

#データベースに接続する
conn = sqlite3.connect('zip.sqlite')
#郵便番号を検索する
cur = conn.cursor()
res = cur.execute('SELECT * FROM zip WHERE code = ?', [code])
for row in res:
  print(row)