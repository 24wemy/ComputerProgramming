# Name : Corinta, Ogi Wemy
# Date : 02 November 2021
# Computer Programming
# Exercise 11

print("MENU KONVERSI")
print("--------------")
print("1. BBM")
print("2. Mata Uang")
pilihan = int(input("Masukan Pilihan Anda : "))

if pilihan == 1:
    print("1. Pertalite")
    print("2. pertamax")
    print("3. pertamax turbo")
    print("4. dexlite")
    pilih = int(input("Masukan pilihan anda : "))
    if pilih == 1:
        i = 0
        while i < 10:
            i += 1
            pertalite = i * 7850
            print("%d liter pertalite = Rp. %d" % (i, pertalite))
    elif pilih == 2:
        i = 0
        while i < 10:
            i += 1
            pertamax = i * 9200
            print("%d liter pertamax = Rp. %d" % (i, pertamax))
    elif pilih == 3:
        i = 0
        while i < 10:
            i += 1
            pertamaxTurbo = i *12500
            print("%d liter pertamax turbo = Rp. %d" % (i, pertamaxTurbo))
    elif pilih == 4:
        i = 0
        while i < 10:
            i += 1
            dexlite = i * 9700
            print("%d liter dexlite = Rp. %d" % (i, dexlite))
    else:
        print("masukan pilihan yang benar")

elif pilihan == 2:
    print("1. Dollar Amerika (USD)")
    print("2. Dollar Singapore (SGD)")
    print("3. Dollar Taiwan (NTD)")
    print("4. Yen")
    pilih = int(input("Masukan Pilihan Anda: "))
    if pilih == 1:
        i = 5000
        while i < 100000:
            i += 5000
            usd = i / 14150
            print("%d IDR = %.2f USD" % (i, usd))
    elif pilih == 2:
        i = 5000
        while i < 100000:
            i += 5000
            sgd = i / 10534
            print("%d IDR = %.2f SGD" % (i, sgd))
    elif pilih == 3:
        i = 5000
        while i < 100000:
            i += 5000
            twd = i / 500
            print("%d IDR = %.2f TWD" % (i, twd))
    elif pilih == 4:
        i = 5000
        while i <= 100000:
            i += 5000
            yen = i / 124
            print("%d IDR = %.2f Yen" % (i, yen))
    else:
        ("Masukan pilihan benar")


        


