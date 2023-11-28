#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Use a private attribute to store size initially
        self.size = size  # Use the property setter to set the initial value
        self.repaired = False  # Initialize repaired status to False
        self.condition = "Used"  # Initialize condition to "Used"

    def get_size(self):
        return self._size  # Return the private attribute

    def set_size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.repaired = True
        self.condition = "New"

    size = property(get_size, set_size)

                    