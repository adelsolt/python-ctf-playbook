enc = open("enc").read()
for c in enc:
    print(hex(ord(c)).lstrip("0x"), end='')
