'''
Python Lab 0

The purpose of this lab is to get you comfortable with lists and dictionaries,
    the two fundamental data structures in Python.
'''

'''
Exercise 1: Sum To Ten

In this exercise, you will create a list of four integers,
    such that the elements sum to 10.

There are many ways to approach this problem, and there is no right answer.
    The `append` and `extend`, and `+` methods of the list may prove useful.
'''

myList = []

###################
### Your code here!







###################

assert len(myList) == 4, 'Wrong number of elements!'
assert sum(myList) == 10, 'Sum does not equal 10!'

'''
Exercise 2: Band of Heros

In this exercise, you will edit the dictionaries representing
    three generic magical heroes.

You must edit these dictionaries in the following ways:

1. Each hero must have a magical ability (a string), with the key 'ability'.
2. Each ability must have a power (an integer), with the key 'strength'.
3. The powers must sum to 25.
'''

fighter = {'name': 'Aragorn'}
archer = {'name': 'Legolas'}
mage = {'name': 'Gandalf'}

###################
### Your code here!







###################

heros = [figher, archer, mage]

for hero in heros:
    assert hasattr(hero, 'ability'), 'Hero has no magical ability!'
    assert hasattr(hero, 'power'), 'Ability has no power!'

assert sum(hero['power'] for hero in heros) == 25, 'Powers do not sum to 25!'

print('Lab 0 complete!')