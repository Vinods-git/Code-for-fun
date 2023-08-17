import qrcode
img = qrcode.make('Vinod Karmenghe')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
