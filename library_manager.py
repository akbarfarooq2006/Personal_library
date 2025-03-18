import json 
import re



try:
    with open("library.json", "r") as file:
        # Agar file khali hai, to empty list load karo
        content = file.read().strip()
        if content:
            library = json.loads(content)  # Valid JSON content ko load karna
        else:
            library = []  # Khali file ke case mein empty list
except FileNotFoundError:
    library = []  # Agar file nahi milti, to empty list


def display_books(book):
    read_status = "Read" if book["read"] else "Unread"
    return (f"{book['Title']} by {book['Author']} ({book["Publication_Year"]}) - {book["Genre"]} - {read_status}")
    
    
    
    




def add():
    print("please add details of your book")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    while True:
        publication_year = int(input("Enter Publication Year: "))
        # if 1000 <= publication_year and publication_year <= 2025:
        if 1000 <= publication_year <= 2025:
            break
        else:
            print("Invalid Year. Please enter a valid year ")
    genre = input("Enter Genre: ")
    while True:
        read = input("have you read this Book (Yes|No): ").lower().strip()
        if read in ['yes', 'no']:
            read = (read == 'yes') # yes ---> true or no---> false
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No' ")
            
    book_details = {
        "Title": title,
        "Author": author,
        "Publication_Year": publication_year,
        "Genre": genre,
        "read": read,
        }
    # with open('library.json', 'a') as file:
    library.append(book_details)
    with open('library.json', 'w') as file:
        json.dump(library, file) 
    print("Book added successfully!")
    


def remove():
    title =input('Enter the title of the book to remove: ')
    for book in library:
        if book["Title"].lower() ==  title.lower():
            library.remove(book)
            with open('library.json', 'w') as file:
             json.dump(library, file)
            print("Book removed successfully!")
            return
    
    print("Book not found of this title!")     
    
    
def search():
    print("\nSearch by: "  )
    print("1. Title")
    print("2. Author")
    search_options=int(input("Enter your choice :"))
    matches=[]
    if search_options == 1:
        search_title=input("Enter the title :")
        matches=[book  for book in library if book["Title"].lower()==search_title.lower()   ]   # here it will make a new array of matches
    elif search_options == 2:
        search_author=input("Enter the author :")
        matches=[book  for book in library if book["Author"].lower()==search_author.lower()   ]
    else:
        print("Invalid option. Please try again!")
       
    
    if matches:
        print("\n","-"*10,"Matching books are ", "-"*10)
        for idx ,books in enumerate(library,1):
            print(f"{idx}. {display_books(books)}")
    else:
        print("No matching books found.")
            
        
    
    
def display_all():
    print("\n","-"*10,"Your Library is ", "-"*10)
    if library:
        for idx ,books in enumerate(library,1):
            print(f"{idx}. {display_books(books)}")
    else : 
        print("Your library is empty.")

            
        
    
    


def statistics():
    read_statistics=0
    length = len(library)
    for book in library:
        if book["read"]==True:
            read_statistics+=1
    
    print( "\n----------- Statistics -----------")
    print(f"Total number of books: {length}")
    percent = (read_statistics/length)*100
    print(f"Number of books read: {read_statistics}")
    print(f"Percentage of books read: {percent:.2f}%")
        
        
        
    
    
    
    

    












# Display Working Directory

while True:





    print("\nWelcome to your Personal Library Manager!")  # Har baar menu se pehle welcome message
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")
    
    choice=int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        remove()
    elif choice == 3:
        search()
    elif choice == 4:
        display_all()
    elif choice == 5:
        statistics()
    elif choice == 6:
        with open("test/lib.json", "w") as file:
            json.dump(library, file)  # Library ko JSON file mein save karna
        print("Library saved to file. Goodbye!")  # Exit message
        break
    else:
        print("Invalid choice. Please try again.")

    
