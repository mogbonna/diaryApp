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

# Main Menu
while True:
    print("==== My Diary App ====")
    print("1. Add Entry")
    print("2. View All Entries")
    print("3. Search Entries")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entries()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
