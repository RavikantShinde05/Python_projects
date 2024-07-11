import qrcode
from sqlalchemy import true

print =(" Wellcome to QRCode Generator ")

features = qrcode.QRCode(version=1,box_size=40, border=3)

features.add_data('./photo.avif')
features.make(fit=true)
image = features.make_image(fill_color="black", back_color="white")
image.save('Generated QRCode.png')
