from contact import Contact

from addressBook import  AddressBook



ab=  AddressBook()

def start():
        print("Welcome to Address Book program")

        while True:
            first_name=input("Enter first name : ")
            last_name=input("Enter last name : ")
            address=input("Enter address : ")
            city=input("Enter city : ")
            state=input("Enter state : ")
            zip_code=input("Enter Zip : ")
            phone_number=input("Enter phone number : ")
            email=input("Enter email : ")
        
            contact= Contact(first_name,last_name,address,city,state,zip_code,phone_number,email)
            
            ab.add_contact(contact)
            ab.display_contact()

            choice = input("Do you want to add another user ? (y/n) : ")
            if(choice.lower()!="y"):
                break

start()

choice =  input("Do you want to update details ? (y/n):")
if choice =="y" :
    edit_user(ab)

choice = input ("Do you want to delete details ? (y/n):")
if choice == "y":
    delete_user(ab)