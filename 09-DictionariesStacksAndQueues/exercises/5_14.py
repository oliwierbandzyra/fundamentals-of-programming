###
# Obsługa klientów w urzędzie (kolejka)
#
import queue

customers = queue.Queue()
ticket_number = 0 # numer ostatnio wydanego biletu

while True:
    print('1. New customer (take a ticket)')
    print('2. Serve next customer')
    print('0. Quit')
    menu = input('Select an option: ')

    if menu == '1':
        # kolejny numer biletu i dodanie klienta na koniec kolejki
        ticket_number += 1
        customers.put(ticket_number)
        print('Your ticket number is', ticket_number)
        print('Customers waiting:', customers.qsize())

    elif menu == '2':
        if not customers.empty():
            # get() bierze klienta z początku kolejki - tego, który czeka najdłużej
            customer = customers.get()
            print('Customer with ticket number', customer, 'please come to the desk.')
        else:
            print('There are no customers waiting.')

    elif menu == '0':
        break

    print()
