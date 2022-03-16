import requests
from contextlib import closing
import csv
# STEP 1: 
# Baca file "harga_rumah.txt"
url = "https://storage.googleapis.com/dqlab-dataset/harga_rumah.txt"
data_harga_rumah = []
with closing(requests.get(url, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())
    data_harga_rumah = [row for row in csv.reader(f)]
# Buat list of dict dengan nama harga rumah
key_harga_rumah = daftar_harga_rumah[0]
harga_rumah = []
for baris_harga_rumah in daftar_harga_rumah[1:]:
	dict_harga_rumah = dict()
	for i in range(len(daftar_harga_rumah)):
		dict_harga_rumah[key_harga_rumah[i]] = baris_harga_rumah[i]
	harga_rumah.append(dict_harga_rumah)
print(harga_rumah)