import random

hak = int(input('kaç hakkınız olsun?: '))
i=random.randint(1, 100)
can = hak
sayac = 0

while can > 0:
    can -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))

    
    if tahmin == i:
        print(f'Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 - (100/hak) * (sayac-1) }')
        break
    elif tahmin < i:
        print("Daha yüksek bir sayı girin.")
    else:
        print("Daha düşük bir sayı girin.")
    

if can == 0:
    print(f"Maalesef, can hakkınız bitti. Doğru sayı {i} idi.")
