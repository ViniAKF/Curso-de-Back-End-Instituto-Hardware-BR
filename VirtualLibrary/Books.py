"""
-------------------------Virtual Library--------------------------------  

Main file: System.py
************************************************************************
In this file, you can see the book features
"""

class Books():
    def __init__(self, title, author, genre, numPages, summary):
        self.title = title
        self.author = author
        self.genre = genre
        self.numPages = numPages
        self.summary = summary