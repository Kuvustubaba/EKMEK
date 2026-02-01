"""


print("Python egitimine hoş geldiniz!")

print(" Turkiyenin en guzel sehri \"Istanbul\"")


print(7+8)

print(7-8)

print(7*8)

print(7/8)

print(7%8)


print("fatih", "kaan", sep="***")


print("27","01","2026", sep="/")



print("{} {}".format("fatih", "kaan "))


help(print)


sayi1 = 155

sayi2 = 155

print(sayi + sayi2)


sayi1 = 165


sayi2 = 57


print("toplam:", sayi1 + sayi2)


print("cikarma:", sayi1 - sayi2)

print("carpma:", sayi1 * sayi2)

print("bolme:", sayi1 / sayi2)


print(type(sayi1))


isim = "Fatih"


soyisim = "Kaan"


print(isim)

print(soyisim)

print(isim, soyisim)

ismin_tamami = isim + " " + soyisim

print(ismin_tamami)


print(ismin_tamami[0], ismin_tamami[6])


kelime = "galata"

print(kelime)




kullanici_adi = input("Kullanici adinizi giriniz: ")


while True:


    chat = input(kullanici_adi + ": ")
    
end




while True:
    score = input("puan giriniz: ")


    print("Girdiginiz puan:", score)

end




tas = "tas"

kagit = "kagit"

makas = "makas"

while True:
    oyuncu1 = input("1. oyuncu seciminizi yapiniz (tas/kagit/makas): ")
    oyuncu2 = input("2. oyuncu seciminizi yapiniz (tas/kagit/makas): ")

    if oyuncu1 == oyuncu2:
        print("Berabere!")
    elif (oyuncu1 == tas and oyuncu2 == makas) or (oyuncu1 == kagit and oyuncu2 == tas) or (oyuncu1 == makas and oyuncu2 == kagit):
        print("1. oyuncu kazandi!")
    else:
        print("2. oyuncu kazandi!")




para = 100

print("kilic: 100" + " senin paran:", para)

while True:

    secim = input("kilic almak icin 'kilic' yaziniz: ")
    if secim == "kilic":
        if para >= 100:
            para -= 100
            print("Kilic alindi! Kalan paran:", para)
        else:
            print("Yeterli paraniz yok!")

End 


"""


para = 100


ekmek = 5

kac_tane = 0

print("Ekmek: 5" + " Senin paran:", para)


while True:
    secim = input("Ekmek almak icin 'ekmek' yaziniz: ")
    if secim == "ekmek":
        if para >= ekmek:
            para -= ekmek
            kac_tane += 1
            print("Ekmek alindi! Kalan paran:", para)
            print("Toplam aldigin ekmek sayisi:", kac_tane)
        else:
            print("Yeterli paraniz yok!")

    
