import qrcode

features = qrcode.QRCode(version=1,box_size=250,border=2)

features.add_data("email:taaahaaa.hmdi@gmail.com")
features.make(fit=True)

generate_image = features.make_image(fill_color="orange",backcolor="white")
generate_image.save("QRCode.png")
