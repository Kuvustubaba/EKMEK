
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
