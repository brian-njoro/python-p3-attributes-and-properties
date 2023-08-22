#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name):
        self._name = name
    
    def get_name (self):
        return self._name
    def set_name(self,name):
        if len(name) <= 25 :
            self._name = name
        else :
            print("Name must be string between 1 and 25 characters.")

    
    def dog_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else :
            print("Breed must be in list of approved breeds")
    

    breed = property(set_breed)
    name = property(get_name,set_name)
