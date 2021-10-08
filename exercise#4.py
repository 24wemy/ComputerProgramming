# Name : Corinta, Ogi Wemy
# date : 9 september 2021
# class : computer progamming
# Exercise #04


# NOMOR.1
# Buatlah pseudocode & program untuk menghitung luas dan volume suatu tabung.
# Adapun rumus luas dari tabung adalah luas = 2 x phi x r x t,
# sedangkan volume tabung adalah volume = phi x r2 x t.
# Catatan: r = jari-jari, t = tinggi tabung dan phi = 3.141593. Variabel input  dimasukan oleh user.

# pseudocode
# 1.INPUT jari-jari
# 2.INPUT tinggi
# 3.INPUT tinggi
# 4.CALCULATE luas tabung <--  2 x phi x r x t
# 5.CALCULATE volume tabung <-- phi x r2 x t
# 6.DISPLAY luas dan volume tabung

phi = 3.14
r = int(input("masukan jari-jari sebuah tabung = "))
t = int(input("masukan tinggi sebuah tabung = "))
luas = 2 * phi * r * t
volume = phi * r **2 * t

print("phi = %.2f , jari-jari tabung = %d , tinggi tabung = %d , maka luas tabung = %.2f." % (phi, r, t, luas))
print("phi = %.2f ,jari-jari tabung = %d , tinggi = %d , maka volume tabung = %.2f." % (phi, r, t, volume))


# NOMOR.2
# Buatlah pseudocode & program untuk menghitung luas dan volume suatu balok.
# Adapun rumus dari luas balok adalah luas = (2 x p x l) + (2 x p x t) + (2 x l x t),
# sedangkan volume balok adalah volume = p x l x t. Catatan: p adalah panjang, l adalah lebar dan t adalah tinggi. 
# Variabel input dimasukan oleh user.

# pseudoce
# 1.INPUT panjang
# 2.INPUT lebar
# 3.INPUT tinggi
# 4.CALCULATE luas balok <-- (2 x p x l) + (2 x p x t) + (2 x l x t)
# 5.CALCULATE volume balok <-- p x l x t
# 6.DISPLAY luas dan volume tabung

p = int(input("masukan panjang balok = "))
l = int(input("masukan lebar balok = "))
t = int(input("masukan tinggi balok = "))
luas = (2 * p * l) + (2 * p * t) + (2 * l * t)
volume =  p * l * t

print("panjang balok = %d,lebar balok = %d, tinggi balok = %d, maka luas balok tersebut = %d." % (p, l , t, luas))
print("panjang balok = %d,lebar balok = %d, tinggi balok = %d, maka volume balok tersebut = %d." %(p, l , t, volume))


# NOMOR.3
# Buatlah pseudocode & program untuk menghitung nilai dari persamaan berikut ini: 
# x = a3 + b2 + c
# Hitunglah nilai x dengan a, b dan c sebagai nilai input dan dimasukan oleh user.

# pseudocode
# 1.INPUT nilai a
# 2.INPUT nilai b 
# 3.INPUT nilai c
# 4.CALCULATE x <-- a3 + b2 + c 
# 5.DISPLAY x

a = int(input("masukan nilai a = "))
b = int(input("masukan nilai b = "))
c = int(input("masukan nilai c = "))
x = a **3 + b **2 + c

print("a = %d, b = %d, c = %d, maka x = %d" % (a, b , c , x))
