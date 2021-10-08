# name : Ogi Wemy Corinta
# date : 14 september 2021
# # Test #01 Computer Programming



# Buatlah pseudocode dan program untuk menghitung sisi miring suatu segitiga siku-siku. 
#  Sisi miring segitiga dapat dihitung menggunakan rumus phitagoras yaitu:
	
# 	dimana :
# 	a = panjang sisi tegak
# 	b = panjang sisi alas
# 	c  = panjang sisi miring
# Input minta masukan dari user.
# Notes: Akar sama saja dengan pangkat ½

# Pseudocode
# 1. INPUT panjang sisi tegak 
# 2. INPUT panjang sisi alas 
# 3. CALCULATE  sisi miring suatu segitiga <-- menggunakan rumus phitagoras
# 4. CALCULATE akar dari sisi miring
# 5. DISPLAY sisi miring segitiga
# 6. DISPLAY akar dari sisi miring

a = int(input("masukan panjang sisi tegak sebuah segitiga: "))
b = int(input("masukan panjang sisi alas sebuah segitiga: "))
c =  (a **2 + b **2)
C_2 = c**(1/2)


print("a = %d, b = %d, c = %d " % (a, b, c))
print("jadi sisi miring segitiga tersebut  = %d " % (C_2))



# Buatlah pseudocode dan program untuk menghitung waktu dari sebuah benda yang jatuh sampai tanah.
# 	Gunakan rumus:  

# 	dimana:
# 	h = tinggi
# 	g = gaya gravitasi 9.81 m/s2
# Input minta masukan dari user. 
# Notes: Akar sama saja dengan pangkat ½

# pseudocode
# 1. INPUT tinggi 
# 2. CALCULATE waktu benda yang jatuh sampai tanah
# 3. CALCULATE akar dari waktu benda yang jatuh ke tanah
# 4. DISPLAY waktu benda yang jatuh sampai tanah
# 5. DISPLAY akar dari waktu benda yang jatuh ke tanah


h = int(input("masukan tinggi: "))
g = 9.81 
waktu = (2 * h / g)
waktu_2 = waktu**(1/2)

print("tinggi benda = %d , gravitasi benda = %.2f , waktu benda = %.2f " % (h, g, waktu))
print("jadi waktu dari sebuah benda yang sampai ke tanah = %.2f " % (waktu_2))


