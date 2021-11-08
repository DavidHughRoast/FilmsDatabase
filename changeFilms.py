import sqlite3
import printFilms


def new():
    entry = []
    title = input("enter the film title")
    year = input("enter the films release year")
    age = input("enter the age rating")
    duration = int(input("how long is the film(minutes)?"))
    genre = input("enter the film genre")
    Id = input("enter the film Id")
    entry.append(Id)
    entry.append(title)
    entry.append(year)
    entry.append(age)
    entry.append(duration)
    entry.append(genre)

    with sqlite3.connect("MyFilms.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("insert into tblfilms values (?,?,?,?,?,?)", entry)
            print("new film added")
        except:
            print("No record added please try again")


def delete():
    with sqlite3.connect("MyFilms.db") as conn:
        cursor = conn.cursor()
        keyfield = input("Enter the ID of the film you want to delete: ")
        try:
            cursor.execute(
                "DELETE FROM tblFilms WHERE filmID =" + keyfield)

            print("\nFilm deleted")
        except:
            print("\nNo film with this ID  exists")


def change():
    with sqlite3.connect("MyFilms.db") as conn:
        cursor = conn.cursor()
        ident = input("what is the id of the record?")
        field = input(
            "what is the field you want to change? (title, yearReleased, rating, duration, genre) ")
        replace = "'" + input("Enter the replacement value") + "'"
        try:
            cursor.execute("update tblFilms set " + field +
                           "=" + replace + "where filmID =" + ident)
            print("Successfully updated")
        except:
            print("Not updated please try again")


def menu():
    choice = '0'
    while choice not in ["1", "2", "3", "4", "5"]:
        print("Please choose an option (number)")
        print("1. add a new entry")
        print("2. delete an entry")
        print("3. change an entry")
        print("4. print records")
        print("5. Exit")
        choice = int(input("What would you like to do?"))
        if choice == 1:
            new()
        elif choice == 2:
            delete()
        elif choice == 3:
            change()
        elif choice == 4:
            printFilms.printf()
        elif choice == 5:
            print("Exiting")
            exit()
        else:
            print("Not available")
            menu()


menu()
