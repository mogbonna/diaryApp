import datetime

def add_entry():
    entry = input("Write your diary entry: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as diary:
        diary.write(f"[{date}] {entry}\n")
    print("Entry saved!\n")

def view_entries():
    print("\n--- All Diary Entries ---")
    try:
        with open("diary.txt", "r") as diary:
            content = diary.readlines()
            if content:
                for line in content:
                    print(line.strip())
            else:
                print("No entries found.")
    except FileNotFoundError:
        print("No diary file found.")
    print()

def search_entries():
    keyword = input("Enter a keyword to search: ").lower()
    found = False
    print("\n--- Search Results ---")
    try:
        with open("diary.txt", "r") as diary:
            for line in diary:
                if keyword in line.lower():
                    print(line.strip())
                    found = True
        if not found:
            print("No matching entries found.")
    except FileNotFoundError:
        print("No diary file found.")
    print()

def edit_entry():
    try:
        with open("diary.txt", "r") as diary:
            lines = diary.readlines()
        
        if not lines:
            print("No entries to edit.\n")
            return
        
        print("\n--- Diary Entries ---")
        for i, line in enumerate(lines):
            print(f"{i + 1}. {line.strip()}")

        choice = int(input("\nEnter the entry number to edit: "))
        if 1 <= choice <= len(lines):
            new_text = input("Enter the new diary entry: ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            lines[choice - 1] = f"[{timestamp}] {new_text}\n"
            
            with open("diary.txt", "w") as diary:
                diary.writelines(lines)
            
            print("Entry updated!\n")
        else:
            print("Invalid entry number.\n")

    except FileNotFoundError:
        print("No diary file found.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main Menu
while True:
    print("==== My Diary App ====")
    print("1. Add Entry")
    print("2. View All Entries")
    print("3. Search Entries")
    print("4. Edit Entry")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entries()
    elif choice == "4":
        edit_entry()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
