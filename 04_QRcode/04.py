import qrcode

qr_data = "www.google.com"
qr_image = qrcode.make(qr_data)

save_path = qr_data + '.png'
qr_image.save(save_path)