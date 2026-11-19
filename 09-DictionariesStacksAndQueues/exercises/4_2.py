###
# Zarządzanie kolejką plików do wydruku (kolejka)
#
import queue

# Queue to kolejka: pierwszy dodany element jest pobierany jako pierwszy
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')

    if menu == '1':
        file_name = input('Enter file name to print: ')
        # put() dodaje nowy plik na koniec kolejki
        files_to_print.put(file_name)

    elif menu == '2':
        # sprawdzamy, czy w kolejce są jakieś pliki
        if not files_to_print.empty():
            # get() pobiera plik z początku kolejki (ten, który czeka najdłużej)
            file_to_print = files_to_print.get()
            print(f'File {file_to_print} is currently being printed. Please wait!')
        else:
            print('There are no files in the print queue.')

    elif menu == '0':
        break

    print()
