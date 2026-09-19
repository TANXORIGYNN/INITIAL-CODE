nama = input("Masukkan nama: ")
kode =  ""

for huruf in nama:
    if huruf in "aiueoAIUEO":
        continue
    kode += huruf 

    if len(kode) == 4:
        break

print("kode:", kode)