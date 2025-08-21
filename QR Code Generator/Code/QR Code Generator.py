print("Welcome to QR Code Generator by Vampire")
#If you are running code make sure that you have qrcode and pillow library installed
import qrcode
a=input("Enter link or text you want to make QR code: ")
img = qrcode.make(a)
type(img)  # qrcode.image.pil.PilImage
img.save("qrcode.png")
print("Thanks for using")