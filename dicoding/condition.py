"""System module."""
# if condition
kelereng_ku = 10
if kelereng_ku:
    print("Cetak ini jika benar")
    print(kelereng_ku)

# if else
tinggi_badan = int(input("Masukkan tinggi badan Anda : "))
if tinggi_badan >= 160:
    print("Silakan, Anda boleh masuk")
else:
    print("Maaf, Anda belum boleh masuk")

# elif condition
nilai = int(input("Masukkan nilai tugas Anda : "))
if nilai > 80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai > 70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai > 60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")

# ternary
# condition_if_true if condition else condition_if_false
lulus = 1
kata = "selamat" if lulus else "perbaiki"
print(kata)

# ternary_tupples
lulus = True
kata1 = ("perbaiki", "selamat")[lulus]
print(kata1)

# ShortHand Ternary
hasil = None
pesan = hasil or "Tidak ada data"
print(pesan)
