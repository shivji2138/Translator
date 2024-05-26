import mysql.connector

# Connection to the Database
conn = mysql.connector.connect(
    host="localhost",        
    user="root",
    password="shivusql",
    database="translator" 
)

# Function to add a word to the translations table
def add_word():
    english = input("Enter English word:")
    tamil =  input("Enter Tamil word:")
    hindi = input("Enter Hindi word:")
    bengali = input("Enter Bengali word:")
    telugu = input("Enter Telugu word:")
    marathi = input("Enter Marathi word:")
    gujarati = input("Enter Gujarathi word:")
    kannada = input("Enter Kannada word:")
    malayalam = input("Enter Malayalam word:")
    punjabi = input("Enter Punjabi word:")
    cursor = conn.cursor()
    sql = "INSERT INTO translations (english, tamil, hindi, Bengali, Telugu, Marathi, Gujarati, Kannada, Malayalam, Punjabi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (english, tamil, hindi, bengali, telugu, marathi, gujarati, kannada, malayalam, punjabi)
    cursor.execute(sql, values)
    conn.commit()
    print("Word added successfully!")
    print()

# Function to search for a word in the translations table
def search_word():
    word = input("Enter english word to search:")
    cursor = conn.cursor()
    sql = "SELECT * FROM translations WHERE english = %s"
    cursor.execute(sql, (word,))
    result = cursor.fetchone()
    if result:
        print("English:", result[1])
        print("Tamil:", result[2])
        print("Hindi:", result[3])
        print("Bengali:", result[4])
        print("Telugu:", result[5])
        print("Marathi:", result[6])
        print("Gujarati:", result[7])
        print("Kannada:", result[8])
        print("Malayalam:", result[9])
        print("Punjabi:", result[10])
        print()
    else:
        print("Word not found!")
        print()

# Display menu options
def display_menu():
    print("Welcome to Indian Languages translator") 
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
    
conn.close()

