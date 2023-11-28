#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Use a private attribute to store page_count initially
        self.page_count = page_count  # Use the property setter to set the initial value
        self.current_page = 1
    def get_book(self):
        return self._page_count  # Return the private attribute

    def set_book(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        self.current_page += 1

    page_count = property(get_book, set_book)



    
        