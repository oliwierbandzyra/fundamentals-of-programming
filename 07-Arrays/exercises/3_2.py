###
# Tworzenie różnych tablic i wypisanie ich zawartości
#
import random # potrzebne do losowania (random.randint)

arr1 = [3, 7, 1, 0, 4]
arr2 = [[2, 3], [7, 1], [0, 4]]
# [wyrażenie for i in range(n)] to skrócony zapis tworzenia listy w pętli
arr3 = [7 for i in range(5)]                      # pięć siódemek
arr4 = [i for i in range(1, 10)]                  # liczby 1..9
arr5 = [i * 2 for i in range(1, 10)]              # 2, 4, ..., 18
arr6 = [random.randint(1, 20) for i in range(10)] # 10 losowych liczb z <1,20>
arr7 = [[] for i in range(5)]                     # 5 pustych list
arr8 = [[1 for i in range(2)] for j in range(4)]  # 4 wiersze po 2 jedynki
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)] # 5x3 losowe

# tablice opisane słownie w poleceniu
arr10 = [4, 0, 3]                                          # tablica z wartościami 4,0,3
arr11 = [0 for i in range(15)]                             # 15 zer
arr12 = [i for i in range(1, 31)]                          # liczby całkowite z <1,30>
arr13 = [random.randint(0, 1) for i in range(20)]          # 20 losowych 0 lub 1
arr14 = [[False for i in range(2)] for j in range(5)]      # 5 wierszy, 2 kolumny, False

print('arr1 =', arr1)
print('arr2 =', arr2)
print('arr3 =', arr3)
print('arr4 =', arr4)
print('arr5 =', arr5)
print('arr6 =', arr6)
print('arr7 =', arr7)
print('arr8 =', arr8)
print('arr9 =', arr9)
print('arr10 =', arr10)
print('arr11 =', arr11)
print('arr12 =', arr12)
print('arr13 =', arr13)
print('arr14 =', arr14)
