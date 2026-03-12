from Contact import Contact
from Operations.edit import edit_user
from AddressBook import  AddressBook


ab=  AddressBook()

def start():
        print("Welcome to Address Book program")

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
start()

choice =  input("Do you want to update details ? (y/n):")
if choice=="y" :
    edit_user(ab)