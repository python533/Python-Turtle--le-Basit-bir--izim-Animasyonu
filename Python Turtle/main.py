from turtle import *

print("Merhaba Benimle Çizmek İster misin?")
isim = input("İsmin Ne?")

if isim:
    def geriyeBosluk(mesafe):
        penup()
        back(mesafe)
        pendown()


    def ileriyeBosluk(mesafe):
        penup()
        forward(mesafe)
        pendown()


    def yukariBosluk(mesafe):
        penup()
        left(90)
        forward(mesafe)
        right(90)
        pendown()


    def asagiBosluk(mesafe):
        penup()
        right(90)
        forward(mesafe)
        left(90)
        pendown()


    def cokgen(uzunluk, kenarSayisi, kalinlik, disRenk, icRenk):
        pensize(kalinlik)
        color(disRenk, icRenk)
        begin_fill()
        for a in range(kenarSayisi):
            forward(uzunluk)
            left(360 / kenarSayisi)
        end_fill()


    bgcolor("cyan")
    speed(0)

    penup()
    goto(-300, -400)
    pendown()
    cokgen(400, 4, 5, "black", "yellow")
    yukariBosluk(400)
    cokgen(400, 3, 5, "black", "brown")
    asagiBosluk(200)
    ileriyeBosluk(50)
    cokgen(75, 6, 3, "black", "white")
    ileriyeBosluk(220)
    cokgen(75, 6, 3, "black", "white")
    geriyeBosluk(150)
    asagiBosluk(200)
    cokgen(150, 4, 5, "black", "orange")
    done()









