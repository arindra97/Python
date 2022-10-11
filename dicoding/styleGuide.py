# disarankan
# Opsi 1
# Rata kiri dengan kurung atau pemisah dengan argumen utama
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Opsi 2
# Tambahkan indentasi ekstra - (level indentasi baru) untuk memisahkan parame-
# ter/argument dari bagian lainnya


def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)


# Opsi 3
# Hanging indents dengan penambahan level indentasi saja
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Contoh kesalahan 1
# uncomment baris 27-28 & 32-35
# Tidak rata kiri dengan bagian yang relevan
# foo = long_function_name(var_one, var_two,
#     var_three, var_four)

# Contoh kesalahan 2
# Sulit dibedakan antara baris lanjutan atau fungsi baru
# def long_function_name(
#     var_one, var_two, var_three,
#     var_four):
#     print(var_one)

# Style Guide 2
# Kondisi (IF)
# Contoh kondisi visual yang tidak diubah/tanpa indentasi
# if (sebuah kondisi dan
#     kondisi yang lain):
#     lakukanSesuatu()

# Tambahkan komentar
# if (sebuah kondisi dan
#     kondisi yang lain):
#     #Mengingat Keduanya Benar, lakukan hal berikut
#     lakukanSesuatu()

# Tambahkan ekstra indentasi pada baris lanjutan
if (sebuahKondisi == 0 &
        kondisiYangLain):
    lakukanSesuatu()

# Kurung siku atau penutup
my_list = [
    1, 2, 3,
    4, 5, 6,
]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

# Mengganti baris : Sesudah Operator Binary
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# import
# kelompokkan import dalam urutan berikut:
# Standard Library
# Library Pihak Ketiga
# Local/Library spesifik
