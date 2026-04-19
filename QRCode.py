import qrcode

# Format the data as a vCard
# Note: X-SOCIALPROFILE is a common way to include social handles
vcard_data = (
    "BEGIN:VCARD\n"
    "VERSION:3.0\n"
    "FN:Your Name\n"
    "ORG:A Y A Clothing\n"
    "TITLE:CEO\n"
    "TEL;TYPE=CELL:{+2348107623065}\n"
    "URL:https://instagram.com/a.y.a_clothing\n"
    "X-SOCIALPROFILE;type=tiktok:https://tiktok.com/@a.y.aclothing\n"
    "X-SOCIALPROFILE;type=Instagram:https://instagram.com/a.y.a_clothing\n"
    "X-SOCIALPROFILE;type=Snapchat:https://snapchat.com/@aya-clothing001\n"
    "PHOTO;VALUE=URL:ayaclothing.jpg\n"
    "END:VCARD"
)

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(vcard_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("contact_qr.png")
