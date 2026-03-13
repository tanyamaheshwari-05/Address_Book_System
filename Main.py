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

choice = input("Do you view person by city or state?(y/n): ")
if choice == "y":
    option= input("Enter choice by which one ?(city /State) : ")
    if option =="city":
        city = input("Enter city you want to search person : ")
        addressBook.view_byCity(city)
    else:
        state=input("Enter state you want to search person : ")
        addressBook.view_byState(state)


choice = input("Do you want to count persons by city/state? (y/n): ")
if choice == "y":
    location = input("Enter city or state : ")
    addressBook.show_byCity_or_byState(location)

choice = input("Do you want to sort contact by name ?(y/n):")
if choice == "y":
    addressBook.sort_by_name()