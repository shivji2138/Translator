import mysql.connector

# Connection to the Database
conn = mysql.connector.connect(
    host="localhost",        
    user="root",
    password="shivusql",
    database="translator" 
)

# Function to add a new recipe
def add_word():
    engword = input("Enter the english word: ")
    tamword = input("Enter the tamil word: ")
    hindiword = input("Enter the hindi word: ")
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO translator(english_word, tamil_word, hindi_word) VALUES (%s, %s, %s)", (engword,tamword,hindiword))
    conn.commit()
    print("Translation added successfully!")

# Function to search for existing recipes by title
def search_word():
    word = input("Enter the english word to search for: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM translator WHERE english_word = %s", (word,))
    translations = cursor.fetchone()
    if translations:
        print("Found Word:")
        print(f"TAMIL: {translations[2]}")
        print(f"HINDI: {translations[3]}")
    else:
        print("No match found.")

# Display menu options
def display_menu():
    print("Welcome to E-T&H translator") 
    print("Choose an option:")
    print("1. Translate a new word")
    print("2. Search for a word")
    print("3.Exit")
    choice = input("Enter your choice (1 or 2 or 3): ")
    if choice == "1":
        add_word()
        return True  
    elif choice == "2":
        search_word()
        return True  
    elif choice == "3":
        return False
    else:
        print("Invalid choice!")
        return True  

# Usage: Call the display_menu() function in a loop
while True:
    if not display_menu():
        break 
