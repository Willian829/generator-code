import qrcode

myqr = qrcode.make("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
myqr.save("myqr.png")