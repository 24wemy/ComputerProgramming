# Name : ogi wemy corinta
# Date : 2 september 2021
# Exercise3

# No.1
# Buatlah program untuk mengkonversi suhu dari fahrenheit ke celcius
# Dimana user dapat menginput suhu dalam fahrenheit
# Tampilkan dengan contoh format : 99.20 Fahrenheit = 37.33 Celcius
# Buat pseudocode & code program

# Pseudocode
# 1. INPUT fahrenheit
# 2. CALCULATE celcius = (fahrenheit - 32) * 5 / 9
# 3. DISPLAY celcius

fahrenheit = float(input("masukan suhu dalam fahrenheit: "))
celcius = (fahrenheit - 32) * 5 / 9
print("%.2f fahrenheit = %.2f celcius" % (fahrenheit , celcius))