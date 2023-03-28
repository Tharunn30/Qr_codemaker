import qrcode
from PIL import Image

link = input("Enter the link you want to convert into QR code: ")

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)
qr.add_data(link)
qr.make(fit=True)

fill_color = input("Enter the fill color for the QR code (in HEX format): ")
back_color = input("Enter the background color for the QR code (in HEX format): ")
img = qr.make_image(fill_color=fill_color, back_color=back_color)

title = input("Enter the filename to save the QR code as (without extension): ")
filename = f"{title}.png"

img.save(filename)
print(f"QR code saved as {filename}")
