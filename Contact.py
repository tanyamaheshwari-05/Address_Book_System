class Contact:
    def __init__(self,first_name,last_name,address,city,state,zip_code,phone_number,email):
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.city=city
        self.state=state
        self.zip_code=zip_code
        self.phone_number=phone_number
        self.email=email
    
    def display(self):
        print("First name : ",self.first_name)
        print("Last name : ",self.last_name)
        print("Address : ",self.address)
        print("City : ",self.city)
        print("State: ",self.state)
        print("Zip : ",self.zip_code)
        print("Phone number : ",self.phone_number)
        print("Email : ",self.email)
