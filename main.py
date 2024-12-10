import qrcode

data = 'Python course'

img = qrcode.make(data)

img.save('/Users/aleksandraj/qrcode-project/qrcode-images/myqrcode.png')