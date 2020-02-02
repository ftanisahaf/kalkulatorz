
from os import system

print('='*50)
print('Author : AkbarAvila\nBlog : http://smel-unlimited.tk\nWeb Tools : http://coderto.com\nInstagram : that1akbar ')
print('='*50)
print('K A L K U L A T O R\vS E D E R H A N A\vPython3')
a = int(input("Masukan angka : "))
b = int(input("Angka kedua : "))

print ("1. Tambahan")
print ("2. Pengurangan")
print ("3. Perkalian")
print ("4. Pembagian")
print ("99. Exit")
opsi = int(input("Opsi Pilih Mana : "))

if opsi == (1):
   c = a + b
   print (c)
elif opsi == (2):
   c = a - b
   print (c)
elif opsi == (3):
	c = a * b
	print (c)
elif opsi == (4):
	c = a // b
	print (c)
else:
   print ("Maaf Proses Diakhiri")