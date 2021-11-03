# Name : Ogi Wemy Corinta
# Date : 21 October 2021
# Class : Computer Programing
# Execise 10

print("MENU KONVERSI")
print("--------------")
print("1. BBM")
print("2. Mata Uang")
pilihan = int(input("Masukan Pilihan Anda: "))

if pilihan == 1:
    for i in range(1, 11):
        pertalite = i * 7850
        pertamax = i * 9200
        pertamaxTurbo = i * 12500
        dexlite = i * 9700
        print("%d liter pertalite = %d" % (i, pertalite))
        print("%d liter pertamax = %d" % (i, pertamax))
        print("%d liter pertamax turbo = %d" % (i, pertamaxTurbo))
        print("%d liter dexlite = %d" % (i, dexlite))

elif pilihan == 2: 
    for i in range(5000, 100000, 5000):
        usd = i / 14150
        sgd = i / 10534
        twd = i / 500
        yen = i/ 124
        print("%d IDR = %.2f USD" % (i, usd))
        print("%d IDR = %.2f SGD" % (i, sgd))
        print("%d IDR = %.2f TWD" % (i, twd))
        print("%d IDR = %.2f Yen" % (i, yen))
    
else:
    print("Masukan kembali pilihan anda")

