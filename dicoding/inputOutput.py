# argumen specifier / Output
# %s - String
# %d - Integers
# %f - Bilangan Desimal
# %.<digit>f - Bilangan desimal dengan sejumlah digit angka dibelakang koma.
# %x/%X - Bilangan bulat dalam representasi Hexa (huruf kecil/huruf besar)

nama = "Dicoding"
umur = 5
print("Umur %s adalah %d tahun." % (nama, umur))

a, b = 10, 11
print('10: %x and 11: %X' % (a, b))

# Input
nilai = input('Masukkan angka : ')
angka = int(nilai)
print(angka)
print(type(angka))
string = input('Masukkan angka : ')
print(string)
print(type(string))
