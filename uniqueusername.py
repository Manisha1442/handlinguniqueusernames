usernames=set()
def add_username():
    username=input("Enter username you want to add: ")
    if username in usernames:
        print(f"The username '{username}' already taken.")
    else:
        usernames.add(username)
        print(f"Ussername '{username}' added successfully.")
def check_username():
    username=input("Enter username you want to check: ")
    if username in usernames:
        print(f"Username '{username}' already taken.")
    else:
        print(f"Username '{username}' is available.")
def update_username():
    old_username=input("Enter the username you want to update: ")
    if old_username in usernames:
      new_username=input("Enter the new username: ")
      if new_username in usernames:
          print(f"The username '{new_username}' is already taken.")
      else:
          usernames.remove(old_username)
          usernames.add(new_username)
          print(f"Username updated from '{old_username}' to '{new_username}.'")
    else:
        print(f"The username '{old_username}' does not exist.")
def delete_username():
    username=input("Enter username you want to delete: ")
    if username in usernames:
        usernames.remove(username)
        print(f"Username '{username}' deleted successfully.")
    else:
        print(f"Username '{username}' does not exist.")
def view_usernames():
    if usernames:
        print("Current Usernames: ",usernames)
    else:
        print("No usernames available.")
while True:
    print("Choose an action")
    print("1. Add a username")
    print("2. Check username availabilty")
    print("3. Update a username")
    print("4. Delete a username")
    print("5. View all usernames")
    print("6. Quit")
    
    choice=input("Enter the number of choice: ")
    if choice=='1':
        add_username()
    elif choice=="2":
        check_username()
    elif choice=="3":
        update_username()
    elif choice=="4":
        delete_username()
    elif choice=="5":
        view_usernames()
    elif choice=="6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice please enter a number from 1 to 6.")
        
