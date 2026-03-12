def delete_user(AddressBook):
    name= input("Enter name of user want to delete : ")
    for d in AddressBook.contacts:
        if d.first_name == name :
            AddressBook.contacts.remove(d)
            print("User deleted successfully")
            return
    print("User not found.")
