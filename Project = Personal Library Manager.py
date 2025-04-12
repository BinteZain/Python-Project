# Personal Library Manager :

import streamlit as st

library = [
    {"title" :    "Maarif ul Hadees"         ,       "author" :       "Molana Muhammad Manzoor Naumani"      } ,
    {"title" :    "Qasas ul Nabiyyeen"       ,       "author" :       "Abbu ul Hasan Alal Husni"             } ,
    {"title" :    "Asan Tarjumat ul Quran"   ,       "author" :       "Molana Mufti Muhammad Taqi Usmani"    } ,
    {"title" :    "Ilm ul Nakhaw"            ,       "author" :       "Molana Mushtaq Ahmad Sahab Chrthaoli" } ,
    {"title" :    "Ilm ul Sarf"              ,       "author" :       "Molana Mushtaq Ahmad Sahab Chrthaoli" }
]     

def add_book() :
    title = input("Book ka name : ")
    author = input("Musannif ka name : ")
    library.append({"title" : title , "author" : author})

    print("Kitab add ho gai!")

def view_books() :
    if not library :

        print("Library khali hai.")
        return
 
    for i , book in enumerate(library , 1) :
        print(f"{i}. {book["title"]} by {book["author"]}")

def delete_book() :
    view_books()
    try :
        index = int(input("Konsi kitab delete karni hai (number) : ")) -1
        removed = library.pop(index)
        print(f"`{removed["title"]}` kitab delete ho gai hai.")

    except :
        print("Apka input ghalat hai!")

def menu() :
    while True :
        print("\n1. Add Book\n2. View Books\n3. Delete Book\n4. Exit")
        choice = input("Option chunein : ")

        if choice == "1" :
            add_book()

        elif choice == "2" :
            view_books()

        elif choice == "3" :
            delete_book()

        elif choice == "4" :
            break

        else :
            print("Apka option sahi nahi hai!")

menu()

# << practiced by Bint e Zain >>