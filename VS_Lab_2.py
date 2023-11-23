import random

interval = (4, 47)
n = int(input('eded daxil edin: '))  # dəyişən n-i seçin
massiv = [random.randint(interval[0], interval[1]) for _ in range(n)]
hasil = 1

for element in massiv:
    if element % 3 == 1:
        hasil = hasil * element

print("n sayda təsadüfi tam ədəddən ibarət massivdə 3-ə böldükdə qalıqda 1 olan elementlərin hasilı: ", hasil)
