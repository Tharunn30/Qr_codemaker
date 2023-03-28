import qrcode

link = input("Enter the link you want to convert into qrcode: ")
img = qrcode.make(link)
print("Please save in png form")
title = input("Enter the title you want to the qr code to be saved as: ")
img.save(f"{title}.png")
