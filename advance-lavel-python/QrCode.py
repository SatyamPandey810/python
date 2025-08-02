import qrcode 
from PIL import Image
import qrcode.constants

img=qrcode.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")

img.save("hello_world.png")

# qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)

# qr.make(fit=True)
# img=qr.make_image(fill_color='black',back_color="blue")

# img.save('img.png')

