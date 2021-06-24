import qrcode
#QR コードの生成で細かい設定を行う場合 --①
qr = qrcode.QRCode(
    # QRの大きさ
    box_size=4,
    # 余白
    border=8,
    # バージョン
    version=12,
    # 誤り訂正レベル
    error_correction=qrcode.constants.ERROR_CORRECT_Q)
#描画するデータを指定する --②
qr.add_data('https://richitschool.com/')
#QR コードの元データを作成する --③
qr.make()
#データを Image オブジェクトとして取得する --④
img = qr.make_image()
#Image をファイルに保存する --⑤
img.save('qrcode2.png')
print('ok')
