#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = 'Mutt'):
        self.name = name
        self.breed = breed
    def bark(self):
        print('Woof!')
    def get_adopted(self, owner_name):
        self.owner = owner_name

fido = Dog('Fibo')
# print(fido.name)
fido.owner = 'Sophie'
# print(fido.owner)
# print(fido.favorite_toy)

snoopy = Dog('Snoopy', 'Tennis Ball')
snoopy.name
# print(snoopy.favorite_toy)

