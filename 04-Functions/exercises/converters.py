def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

# Zamienia centymetry na cale (1 cal = 2.54 cm)
def cm_to_inches(n):
    return n/2.54

# Zamienia stopy i cale na centymetry
def feet_inches_to_cm(feet, inches):
    # 1 stopa = 12 cali, więc najpierw liczymy wszystko w calach
    total_inches = feet*12 + inches
    # potem cale zamieniamy na centymetry (1 cal = 2.54 cm)
    return total_inches*2.54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'254cm = {cm_to_inches(254)}in')
    print(f'5ft 9in = {feet_inches_to_cm(5, 9)}cm')
