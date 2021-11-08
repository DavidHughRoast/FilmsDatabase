import sqlite3


def printall():
    data = sqlite3.connect("MyFilms.db")
    cursor = data.cursor()
    for row in cursor.execute("select * from tblFilms"):
        print(row)


def printrate():
    with sqlite3.connect("MyFilms.db") as data:
        cursor = data.cursor()
        for row in (cursor.execute("select * from tblFilms order by rating")):
            print(row)


def printgenre():
    with sqlite3.connect("MyFilms.db") as data:
        cursor = data.cursor()
        for row in (cursor.execute("select * from tblFilms order by genre")):
            print(row)


def menu():
    choice = '0'
    while choice not in ["1", "2", "3", "4"]:
        print("Please choose an option (number)")
        print("1. View all")
        print("2. View by rating")
        print("3. View by genre")
        print("4. Exit")
        choice = int(input("What would you like to do?"))
        if choice == 1:
            printall()
        elif choice == 2:
            printrate()
        elif choice == 3:
            printgenre()
        elif choice == 5:
            print("Exiting")
            exit()
        else:
            print("Not available")
            menu()


menu()
