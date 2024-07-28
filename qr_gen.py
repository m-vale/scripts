import segno

x = input("QR-ify this: \n")

qrcode = segno.make_qr(x)
qrcode.save(
    "qoncertr.png",
    scale=10,
    #light="lightgreen",
    #dark="darkgreen",
    #data_dark="green",
)

