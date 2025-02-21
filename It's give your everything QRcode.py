import png
import pyqrcode as q

nam=input('enter your name so Convert to QR code: ')
file_name=input('enter your name file : ')

m=file_name+'.png'

qrcode=q.create(nam)
qrcode.show()
qrcode.png(m,scale=6)

