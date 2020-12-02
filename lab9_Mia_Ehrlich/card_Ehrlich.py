import random

class Card:
    
    # Initialize the data attribute to null
    # 0 for integers
    # '' for strings
    def __init__(self):
        self.__value = 0

    # When a card is dealt, assigning a numeric value,
    # assign the face value at the same time
    def deal(self):
        self.__value = random.randint(1,13)

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    # Method to return the face value corresponding to the __value attribute
    # The first element in the list is a dummy value so the value could be
    # used as the index without adjusting it
    def get_face_value(self):
        face_values = ["Joker", "Ace", "Two", "Three", "Four", "Five", "Six",
                       "Seven", "Eight", "Nine", "Ten", "Jack","Queen", "King"]
        return face_values[self.__value]

    def __str__(self):
        return str(self.__value)

    
