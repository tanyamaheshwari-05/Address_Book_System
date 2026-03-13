from contact import Contact

from AddressBook import  AddressBook
from addressBookManager import AddressBookManager

address_bookmanager_obj=  AddressBookManager()
book_name = input("Enter Address Book Name : ")
address_bookmanager_obj.add_book(book_name)
addressBook = address_bookmanager_obj.get_book(book_name)

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
            
            addressBook.add_contact(contact)
            addressBook.display_contact()

            choice = input("Do you want to add another user ? (y/n) : ")
            if(choice.lower()!="y"):
                break

start()

choice =  input("Do you want to update details ? (y/n):")
if choice =="y" :
    addressBook.edit_user()

choice = input ("Do you want to delete details ? (y/n):")
if choice == "y":
    addressBook.delete_user()

location = input("Enter city or state to search : ")
results = addressBook.search_bycity_and_bystate(location)
for r in results:
    r.display()