class AddressBook:

    def __init__(self):
        self.contacts=[]

    def add_contact(self,contact):
        self.contacts.append(contact)
        print("\nContact Added Successfully")

    def display_contact(self):    
        for c in self.contacts:
            c.display()

    def delete_user(self):
        name= input("Enter name of user want to delete : ")
        for d in self.contacts:
            if d.first_name == name :
                self.contacts.remove(d)
                print("User deleted successfully")
                return
        print("User not found.")

    def edit_user(self):
            name= input("enter name of user to update contact: " )

            for c in self.contacts:
                if c.first_name ==name:

                    edit=True
                    print("Contact Found ! Enter new details")
                    
                    while (edit):
                        print("1. Edit First Name")
                        print("2. Edit Last Name")
                        print("3. Edit address")
                        print("4. Edit city")
                        print("5. Edit state")
                        print("6. Edit zip")
                        print("7. Edit phone_Number")
                        print("8. Edit Email")
                        print("0. quit")
                    
                        choice=int(input("Enter number which needs to edit : "))
                        match choice:
                            case 1:
                                c.first_name=input("Enter new first name : ")

                            case 2:
                                c.last_name= input("Enter enw last name :")

                            case 3:
                                c.address= input("Enter new address :")

                            case 4:
                                c.city= input("Enter new city :")

                            case 5:
                                c.state= input("Enter new state : ")

                            case 6:
                                c.zip_code= input("Enter new zip code : ")

                            case 7 :
                                c.phone_number=input("Enter phone number :")

                            case 8 :
                                c.email= input("Enter new email :")

                            case 0:
                                edit= False
    
                        print("Contact updated successfully !")
                
                print("Contact not found !")



