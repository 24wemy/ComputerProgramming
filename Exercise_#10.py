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
        pl = 7850
        pm = 9200
        pt = 12500
        dl = 9700
        a = i * pl + pl
        b = i * pm + pm
        c = i * pt + pt
        d = i * dl + dl
        print(i, "Liter Pertalite = Rp.%d" % a)
        print(i, "Liter Pertamax = Rp.%d" % b)
        print(i, "Liter Pertamax Turbo = Rp.%d" % c)
        print(i, "Liter Dexlite = Rp.%d" % d)
elif pilihan == 2:
    for i in range(1,11):
        usd = 14150
        sgd = 10534
        twd = 500
        yen = 124
        a = i * usd + 5000
        b = i * sgd + 5000
        c = i * twd + 5000
        d = i * yen + 5000
        print(i, "Dollar America = Rp.%d" % a)
        print(i, "Dollar Singapore = Rp.%d" % b)
        print(i, "Dollar Taiwan = Rp.%d" % c)
        print(i, "yen = Rp.%d" % d)
else:
    print("Masukan pilihan yang benar!")


        