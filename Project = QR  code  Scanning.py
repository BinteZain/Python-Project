# QR code Scanning Project :

import qrcode

img = qrcode.make("https://github.com/BinteZain/Python-Project")

print(type(img))

img.save("Bint e Zain.png")

print("QR code has been generated successfully.")

# << practiced by Bint e Zain >>