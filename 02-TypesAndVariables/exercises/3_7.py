###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#

# Całkowita populacja świata
total = 8000000000

# Liczba ludności na półkuli północnej
north = 7200000000

# Obliczamy ludność na półkuli południowej (całość minus północ)
south = total - north

# Wyświetlamy statystyki
print("World population: ", total) # wypisanie całkowitej populacji
print("Northern Hemisphere: ", north) # liczba populacji na półkuli północnej
print("Northern Hemisphere in %: ", north/total*100) # liczba populacji na półkuli północnej wypisana w procentach w stosunku do całego świata
print("Southern Hemisphere: ", south) # liczba popoulacji na półkuli południowej
print("Southern Hemisphere in %: ", south/total*100) # liczba populacji na półkuli południowej wypisana w procentach w stosunku do całego świata