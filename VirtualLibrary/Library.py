"""
-------------------------Virtual Library--------------------------------  

Main file: System.py
************************************************************************
In this file, you can see the changes in the repository    
"""

import Books

class Library():
    def register(self, book): #here, I can consider that book is already a object of Books (initializing it inside System.py program, or I need to get all features and do this here)
        #I don´t know, beacause I need to know the features to insert into SQL commands
        print(book.title)