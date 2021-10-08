# Name : ogi wemy corinta
# Date : 2 september 2021
# Exercise3

# No.2
# Buatlah program untuk menghitung BMI (Body Mass Index)
# Dimana tinggi dan berat minta input dari user
# Rumus : BMI = berat / (tinggi * tinggi), berat dalam kg dan tinggi dalam meter
# 170 cm = 1.7 m
# Tampilkan output dengan format:
# Tinggi: 1.7 meter, Berat: 96.2 Kg. BMI Anda adalah 33.3.
# Buat pseudocode & code program

# Pseudocode:
# 1. INPUT berat
# 2. INPUT tinggi
# 3. CALCULATE BMI <- berat / (tingi * tinggi)
# 4. DISPLAY BMI

tinggi = float(input("masukan tinggi badan anda (m): "))
berat = float(input("masukan berat badan anda (kg): "))
bmi = berat / (tinggi * tinggi)

print("tinggi: %.1f meter, Berat: %.1f kg. BMI anda adalah %.1f" % (tinggi, berat, bmi))
