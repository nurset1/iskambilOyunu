import random
import time
sayilar = ["A","K","Q","J","2","3","4","5","6","7","8","9","10"]
isimler = ["Maça","Kupa","Sinek","Karo"]
dagitilanKart = []
ortayakoyulankart = []
oyuncununKartlari = []
bilgisayarKartlari = []

#Kartlar oluşturuluyor
while len(dagitilanKart) < 52:
    sayi = random.sample(sayilar,1)
    isim = random.sample(isimler,1)
    birlestir = isim[0] + " " + sayi[0]
    if birlestir not in dagitilanKart:
        dagitilanKart.append(birlestir)
#Kartlar oyunculara dağıtılıyor
def kartlaridagit(dagitilankart):
    oyuncu = []
    bilgisayar1 = []
    #Bu koşulda ilk 4 kart ortaya koyuluyor
    if len(dagitilanKart) == 52:
        ilkDortKart = random.sample(dagitilanKart,4)
        ortayakoyulankart.append(ilkDortKart[0])
        ortayakoyulankart.append(ilkDortKart[1])
        ortayakoyulankart.append(ilkDortKart[2])
        ortayakoyulankart.append(ilkDortKart[3])
        for i in ilkDortKart:
            dagitilanKart.remove(i)

    if len(oyuncu) == 0:
        oyuncukarti = random.sample(dagitilankart,4)
        oyuncu.append(oyuncukarti)
        for i in oyuncukarti:
            dagitilanKart.remove(i)

    if len(bilgisayar1) == 0:
        bilgisayar1karti = random.sample(dagitilankart,4)
        bilgisayar1.append(bilgisayar1karti)
        for i in bilgisayar1karti:
            dagitilanKart.remove(i)

    oyunabasla(oyuncu[0],bilgisayar1[0])

def atilansonkart(sonkart):
    sonIndex = len(ortayakoyulankart)-2

    ortadaSonkart = ortayakoyulankart[sonIndex]
    ortadaSonkart = ortadaSonkart.split(" ")
    sonkart = sonkart.split(" ")

    if sonkart[-1] == ortadaSonkart[-1] and len(ortayakoyulankart)>1:
        if sonkart[0] == "Oyuncu":
            print("Oyuncu kartları aldı")
            ortayakoyulankart.clear()
        else:
            print("Bilgisayar kartları aldı")
            ortayakoyulankart.clear()
    elif sonkart[-1] =="J" and len(ortayakoyulankart) > 1:
        if sonkart[0] == "Oyuncu":
            print("Oyuncu kartları aldı")
            ortayakoyulankart.clear()
        else:
            print("Bilgisayar kartları aldı")
            ortayakoyulankart.clear()

def oyunabasla(oyuncu,bilgisayar1):
    kartSayisi = 0

    while kartSayisi <= 3:

        #Burada bilgisayar ortaya kart atıyor
        ortayakoy = random.sample(bilgisayar1,1)
        ortayakoyulankart.append(ortayakoy[0])
        bilgisayar1.remove(ortayakoy[0])
        print("Bilgisayar Oynuyor")
        time.sleep(1)
        """for i in ortayakoyulankart:
            print("Ortadaki Kartlar = ",i)"""
        if len(ortayakoyulankart) != 0:
            index = len(ortayakoyulankart)-2
            index2 = len(ortayakoyulankart)-1
            if len(ortayakoyulankart) > 1:
                print("Son Kart = " + ortayakoyulankart[index])
                print("Son Kart = " + ortayakoyulankart[index2])
            else:
                print("Son Kart = " + ortayakoyulankart[index2])
        else:
            print("Ortada Kart Yok")
        atilansonkart(ortayakoy[0])
        a = 1
        print("*****************************\n"
              "*****************************")
        for i in oyuncu:
            print(a,".Kart",i)
            a+=1
        print(len(dagitilanKart))
        #Burada oyuncu ortaya kart atıyor
        try:

            hangisi = int(input("Kart seçin:"))
            secilenkart = "Oyuncu " + oyuncu.pop(hangisi-1)
            ortayakoyulankart.append(secilenkart)
            atilansonkart(secilenkart)
        except:
            print("Rastgele Kart Atıldı")
            secilenkart = random.sample(oyuncu,1)
            oyuncu.remove(secilenkart[0])
            secilenkart = "Oyuncu " + secilenkart[0]
            ortayakoyulankart.append(secilenkart)
        """for i in ortayakoyulankart:
            print("Ortadaki Kartlar = ",i)"""
        if len(ortayakoyulankart) != 0:
            index = len(ortayakoyulankart)-2
            index2 = len(ortayakoyulankart)-1
            if len(ortayakoyulankart) > 1:
                print("Son Kart = "+ortayakoyulankart[index])
                print("Son Kart = " + ortayakoyulankart[index2])
            else:
                print("Son Kart = " + ortayakoyulankart[index2])
        else:
            print("Ortada Kart Yok")
        time.sleep(1.5)
        print("\n"*30)
        kartSayisi += 1
    if len(dagitilanKart) != 0:
        kartlaridagit(dagitilanKart)


    else:
        print("Oyun bitti")

kartlaridagit(dagitilanKart)


time.sleep(10)