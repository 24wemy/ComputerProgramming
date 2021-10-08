# Name : Ogi Wemy Corinta
# Date : 7 september 2021
# class : computer programming 
# Exercise #04

# NOMOR 1
# Buatlah pseudocode & program untuk menghitung luas dan keliling suatu persegi panjang. 
# Adapun rumus luas dari persegi panjang adalah luas = panjang x lebar, 
# sedangkan keliling persegi panjang adalah keliling = 2 x (panjang + lebar). 
# Panjang dan lebar dimasukan melalui input oleh user.

# psoudoce
# 1. INPUT panjang
# 2. INPUT lebar
# 3. CALCULATE luas persegi panjang <-- panjang x lebar
# 4. CALCULATE keliling persegi panjang <-- 2 x (panjang + lebar)
# 5. DISPLAY luas dan keliling suatu persegi panjang


panjang = int(input("masukan panjang sebuah persegi panjang (cm): "))
lebar = int(input("masukan lebar sebuah persegi panjang (cm):  "))
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print("Panjang: %d cm, Lebar: %d cm. Luas sebuah persegi panjang adalah %d" % (panjang, lebar, luas))
print("Panjang: %d cm, Lebar: %d cm. Keliling sebuah persegi panjang adalah %d" % (panjang, lebar, keliling))


# NOMOR 2
# Buatlah pseudocode & program untuk menghitung luas dan keliling suatu lingkaran. 
# Adapun rumus luas dari lingkaran adalah luas = phi x jari-jari2,
# sedangkan keliling lingkaran adalah keliling = 2 x phi x jari-jari.
# Jari-jari dimasukan melalui input oleh user.

# pseudocode
# 1. INPUT jari jari
# 2. CALCULATE luas lingkaran <-- phi x jari-jari2
# 3. CALCULATE keliling lingkaran <-- 2 x phi x jari-jari
# 4. DISPLAY luas dan keliling sebuah lingkaran

jari_jari = int(input("masukan jari-jari sebuah lingkaran: " ))
phi = 3.14 
luas = phi * jari_jari **2
keliling = 2 * phi * jari_jari

print("Jari-jari lingkaran: %d ,maka Luas lingkarannya = %d" % (jari_jari, luas))
print("Jari-jari lingkaran: %d ,maka Keliling lingkarannya = %d" % (jari_jari, keliling))


# NOMOR 3
# Buatlah pseudocode & program untuk mencari konversi suhu 
# dari celcius ke fahrenheit, reamur dan kelvin. Dengan rumus:
# fahrenheit = (9 / 5 x celsius) + 32
# reamur = (4 / 9 x celsius) + 32
# kelvin = 273 + celsius

# # pseudocode
# 1. INPUT celcius
# 2. CALCULATE celcius ke fahrenheit <-- (9 / 5 x celsius) + 32
# 3. CALCULATE celcius ke reamur <-- (4 / 9 x celcius) + 32
# 4. CALCULATE celcuis ke kelvin <-- 273 + celcuis
# 5. DISPLAY celcius ke farenheit
# 6. DISPLAY celcius ke reamur
# 7. DISPLAY celcius ke kelvin

celcius = float(input("masukan suhu dalam celcius: "))
fahrenheit = (9 / 5 * celcius) + 32
reamur = (4 / 9 * celcius) + 32
kelvin = 273 + celcius

print("%.2f Celcius = %.2f fahrenheit" % (celcius, fahrenheit))
print("%.2f Celcius = %.2f reamur" % (celcius, reamur))
print("%.2f Celcius = %.2f kelvin" % (celcius, kelvin))


