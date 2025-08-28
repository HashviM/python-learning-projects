import qrcode
port = 'https://hashvim.github.io/my_portfolio/'
site = 'https://scan-ride.vercel.app/'

qr1 = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr1.add_data(port)
qr1.make()
img1 = qr1.make_image(fill_color = 'black', back_color = 'white')
img1.save('portfolio_qr.png')

qr2 = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr2.add_data(site)
qr2.make()
img2 = qr2.make_image(fill_color = 'black', back_color = 'white')
img2.save('website_qr.png')

