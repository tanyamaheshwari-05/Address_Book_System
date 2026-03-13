from addressBook import AddressBook
class AddressBookManager:

    def __init__(self):
        self.book={}
    
    def add_book(self,book_name):
        if book_name not in self.book:
            self.book[book_name]=AddressBook()
        else:
            raise ValueError("Book already exists")
    
    def get_book(self,book_name):
        if book_name in self.book:
            return self.book[book_name]
        else:
            raise ValueError("Book not found")


    
