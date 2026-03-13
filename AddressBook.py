class AddressBook:

    def __init__(self):
        self.contacts=[]
        self.city_dict={}
        self.state_dict={}

#Add contact 
    def add_contact(self,contact):
        
        if any(c.first_name==contact.first_name for c in self.contacts):
            print("Duplicate contact not allowed")
            return

        self.contacts.append(contact)

        if contact.city not in self.city_dict:
            self.city_dict[contact.city]= []
            self.city_dict[contact.city].append(contact)

        if contact.state not in self.state_dict:
            self.state_dict[contact.state]=[]
            self.state_dict[contact.state].append(contact)
        print("\nContact Added Successfully")

    def display_contact(self):    
        for c in self.contacts:
            c.display()

# delete contact
    def delete_user(self):
        name= input("Enter name of user want to delete : ")
        for d in self.contacts:
            if d.first_name == name :
                self.contacts.remove(d)
                print("User deleted successfully")
                return
        print("User not found.")

  # edit contact       
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

# Search by city or state 
    def search_bycity_and_bystate(self,location):
        result =[]

        for c in self.contacts:
            if c.city == location or c.state == location:
                result.append(c)
        return result

# view by city
    def view_byCity(self,city):
        if city in self.city_dict:
            for c in self.city_dict[city]:
                c.display()
        else:
            print("No contact found in this city")

# view by state
    def view_byState(self,state):
        if state in self.state_dict:
            for s in self.state_dict[state]:
                s.display()
        else:
            print("No contact found in this state")



