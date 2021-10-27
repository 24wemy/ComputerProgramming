# Name : Ogi Wemy Corinta 
# Date : 14 October 2021
# Computer Programming
# Exercise 09


# 1. Buatlah program untuk menampilkan bilangan genap antara 1 sampai 100.

for i in range(1, 101):
    if i % 2 == 0:
        print(i, end= " ")


# 2. Buatlah perkalian sampai 10 dari angka yang dimasukan 

bilangan = int(input("Masukan Angka = "))

for i in range(1, 11):
    hasil = i * bilangan
    print(i, "x" , bilangan, "= ", hasil)