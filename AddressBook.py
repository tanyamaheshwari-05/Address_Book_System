class AddressBook:

    def __init__(self):
        self.contacts=[]

    def add_contact(self,contact):
        self.contacts.append(contact)
        print("\nContact Added Successfully")

    def display_contact(self):    
        for c in self.contacts:
            c.display()





