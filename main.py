from functions import *

loadResults() 
choice = ''
while choice != '0':
    choice = menu()
    if choice == '1':
        addNewResults()
    elif choice == '2':
        choice1 = ''
        while choice1 != '0':
            choice1 = menu1()
            if choice1 == '1':
                print('A legtöbb pontot elért diák neve: ',legnagyobb())
                input('Tovább (Enter)...')
            elif choice1 == '2':
                print('A legtöbb pontot elért diák neve: ',legkisebb())
                input()
            elif choice1 == '3':
                printAllResults()
                
    elif choice == '3':
        deleteResults() 
 




