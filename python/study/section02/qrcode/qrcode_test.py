import qrcode

img = qrcode.make('https://richitschool.com')
img.save('qrcode.png')
print('ok')
