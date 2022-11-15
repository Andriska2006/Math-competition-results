from functions import *

loadResults() 
choice = ''
while choice != '0':
    choice = menu()
    if choice == '1':
        addNewResults()
    elif choice == '2':
        legnagyobb()
    elif choice == '3':
        printAllResults()
    elif choice == '4':
        deleteResults()
