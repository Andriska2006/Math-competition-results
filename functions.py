from data import *
from os import system

filename = 'math.csv'
cimsor = ''                  


def menu():
    system('cls')
    print('0 - Kilépés')
    print('1 - Új eredmény hozzáadása')
    print('2 - Eredmények')
    print('3 - Eredmény törlése')
    return input('Kérem válasszon: ')

def menu1():
    system('cls')
    print('0 - Vissza a főmenübe')
    print('1 - Legjobb eredmény')
    print('2 - Legrosszabb eredmény')
    print('3 - Összes eredmény')
    return input('Kérem válasszon: ')

def loadResults():
    file = open(filename, 'r', encoding='utf-8')
    global cimsor
    cimsor = file.readline()
    for row in file:
        splitted = row.strip().split(';')
        mathcompetition[splitted[0]] = float(splitted[1])
    file.close()

def addNewResults():
    system('cls')
    print('Új eredmény')
    student = input('Diák neve: ')
    result = input('Eredménye: ')
    mathcompetition[student] = result 
    saveResultsToFile(student, result)
    input('Eredmény felvéve. Tovább (Enter)...')

def saveResultsToFile(student, result):
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'{student};{result}\n')
    file.close()

def printAllResults():
    system('cls')
    print('Eredmények listája')
    for key, value in mathcompetition.items():
        print(f'{key} - {value}pont.')
    input('Tovább (Enter)...')

def deleteResults():
    system('cls') 
    print('Eredmény törlése')
    student = input(' A törlendő diák neve: ')
    if student in mathcompetition:
        mathcompetition.pop(student)
        saveAllToFile()
        input('Eredmény törölve.  Tovább (Enter)...')
    else:
        input('Nincs ilyen eredmény.  Tovább (Enter)...')
        
def saveAllToFile():
    file = open(filename, 'w', encoding='utf-8')

    file.write(cimsor)
    for student,result in mathcompetition.items():   
        file.write(f'{student};{result}\n')
    
    file.close()

def legnagyobb():
    maxvalue = 0
    maxkey = ''
    for key,value in mathcompetition.items():
        if value > maxvalue:
            maxvalue = value
            maxkey = key
    return maxkey
    
def legkisebb():
    minvalue = 999999
    minkey = ''
    for key,value in mathcompetition.items():
        if value < minvalue:
            minvalue = value
            minkey = key
    return minkey