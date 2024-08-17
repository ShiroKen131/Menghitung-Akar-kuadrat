import math

def hitung_akar_kuadrat(a, b, c):
    # Menghitung diskriminan
    diskriminan = b**2 - 4*a*c
    
    # Jika diskriminan negatif, tidak ada akar nyata
    if diskriminan < 0:
        return "Persamaan tidak memiliki akar real"
    
    # Menghitung dua akar menggunakan rumus kuadrat
    akar1 = (-b + math.sqrt(diskriminan)) / (2*a)
    akar2 = (-b - math.sqrt(diskriminan)) / (2*a)
    
    return akar1, akar2
a = 1
b = -3
c = 2
akar = hitung_akar_kuadrat(a, b, c)
print(f"Akar-akar dari persamaan {a}x^2 + {b}x + {c} = 0 adalah {akar}")
