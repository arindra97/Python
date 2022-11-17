## Search Bilangan Prima
for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            # print(n, ' equals ', x, 'x', n/x)
            break
    else:
        print(n, 'adalah bilangan prima')

# Pass
import sys
data=''
while(data!='exit'):
    try:
        data=input('Please enter an integer (type exit to exit): ')
        print('got integer: {}'.format(int(data)))
    except:
        if data == 'exit':
            pass  # exit gracefully without prompt any error
        else:
            print('error: {}'.format(sys.exc_info()[0]))

# ---------------------------------------------------------
# List Comprehension
# new_list = [expression for_loop_one_or_more conditions]

#Contoh
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

# List Comprehension
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

#Contoh menemukan item yang ada di kedua list
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = []
for a in list1:
  for b in list2:
    if a == b:
      duplikat.append(a)
     
print(duplikat)  # Output ['d','i']

# Implementasi dengan list comprehension
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = [a for a in list1 for b in list2 if a == b]
print(duplikat) # Output: ['d','i']

# Contoh kecilkan semua huruf
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [_.lower() for _ in list_a]
print(small_list_a)

list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)