import json  # JSON ke liye import, file handling ke liye use hoga

# Library ko initialize karna: file se load karenge, agar file nahi hai to empty list
try:
    with open("test/lib.json", "r") as file:
        library = json.load(file)  # File se data load karna
except FileNotFoundError:
    library = []  # Agar file nahi milti, to empty list se shuru karna

# Helper function jo book ko format karta hai display ke liye
def format_book(book):
    """
    Book dictionary ko ek formatted string mein convert karta hai.
    Example: "The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read"
    """
    read_status = "Read" if book["read"] else "Unread"  # Boolean ko string mein convert karna
    return f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}"

# Function jo naya book add karta hai
def add_book():
    """
    User se book details mangta hai aur library mein add karta hai.
    Year integer hona chahiye, read status boolean.
    """
    title = input("Enter the book title: ")  # Title string mein lena
    author = input("Enter the author: ")     # Author string mein lena
    # Year ke liye loop, jab tak valid integer na mile
    while True:
        try:
            year = int(input("Enter the publication year: "))
            break  # Valid integer mil gaya to loop se bahar
        except ValueError:
            print("Please enter a valid year.")  # Agar galat input, to dobara mangna
    genre = input("Enter the genre: ")       # Genre string mein lena
    # Read status ke liye loop, jab tak 'yes' ya 'no' na mile
    while True:
        read = input("Have you read this book? (yes/no): ").lower()
        if read in ["yes", "no"]:
            read = (read == "yes")  # 'yes' to True, 'no' to False
            break
        else:
            print("Please enter 'yes' or 'no'.")  # Galat input pe dobara mangna
    # Book dictionary banana
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)  # Library list mein book add karna
    print("Book added successfully!")  # User ko confirmation dena

# Function jo book remove karta hai
def remove_book():
    """
    User se title mangta hai aur pehla matching book remove karta hai.
    Case-insensitive comparison karta hai.
    """
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():  # Title match karna, case-insensitive
            library.remove(book)  # Book ko list se hata dena
            print("Book removed successfully!")
            return  # Ek book remove karne ke baad function khatam
    print("Book not found.")  # Agar title nahi mila

# Function jo books search karta hai
def search_book():
    """
    User ko title ya author ke zariye search karne deta hai.
    Partial matches bhi show karta hai.
    """
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter the title: ")
        # Title mein search term dhoondna (partial match)
        matches = [book for book in library if title.lower() in book["title"].lower()]
    elif choice == "2":
        author = input("Enter the author: ")
        # Author mein search term dhoondna (partial match)
        matches = [book for book in library if author.lower() in book["author"].lower()]
    else:
        print("Invalid choice.")  # Galat option pe message
        return
    if matches:  # Agar matches milte hain
        print("Matching Books:")
        for idx, book in enumerate(matches, 1):  # Books ko number ke saath display karna
            print(f"{idx}. {format_book(book)}")
    else:
        print("No matching books found.")  # Agar koi match nahi mila

# Function jo saare books display karta hai
def display_all_books():
    """
    Library ke saare books ko numbered list mein show karta hai.
    """
    if library:  # Agar library khali nahi hai
        print("Your Library:")
        for idx, book in enumerate(library, 1):  # Har book ko number ke saath print karna
            print(f"{idx}. {format_book(book)}")
    else:
        print("Your library is empty.")  # Agar library khali hai

# Function jo statistics show karta hai
def display_statistics():
    """
    Total books aur percentage read calculate karta hai.
    Khali library ka case bhi handle karta hai.
    """
    total = len(library)  # Library mein kitne books hain
    if total == 0:
        print("Your library is empty.")
        return
    read = sum(1 for book in library if book["read"])  # Kitne books read hain
    percentage = (read / total) * 100  # Percentage calculate karna
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%")  # Ek decimal place ke saath percentage

# Main program loop
while True:
    print("\nWelcome to your Personal Library Manager!")  # Har baar menu se pehle welcome message
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_book()  # Naya book add karna
    elif choice == "2":
        remove_book()  # Book remove karna
    elif choice == "3":
        search_book()  # Books search karna
    elif choice == "4":
        display_all_books()  # Saare books display karna
    elif choice == "5":
        display_statistics()  # Statistics show karna
    elif choice == "6":
        # Exit karne se pehle library file mein save karna
        with open("test/lib.json", "w") as file:
            json.dump(library, file)  # Library ko JSON file mein save karna
        print("Library saved to file. Goodbye!")  # Exit message
        break  # Loop se bahar nikalna
    else:
        print("Invalid choice. Please try again.")  # Galat input pe message