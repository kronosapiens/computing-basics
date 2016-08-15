'''
Python Lab 2

The purpose of this lab is to give you exposure to looping and control flow,
    two very basic concepts in the design of programs.
'''

'''
Exercise 1: GPA Mean

In this exercise, you will write a function to calculate the average GPA
    of three students. Each student is represented as a dictionary,
    with a `gpa` field. You will write a function which loops over these
    students and returns the mean of their gpas.

You will find the `for x in y:` looping syntax useful here. In addition,
    consider possibilities for storing and manipulating values in variables.
'''

myStudents = [
    {
        'name': 'Leto',
        'gender': 'M',
        'gpa': 3.5
    },
    {
        'name': 'Jessica',
        'gender': 'F',
        'gpa': 3.9
    },
    {
        'name': 'Paul',
        'gender': 'M',
        'gpa': 4.0
    },
]

def gpaMean(students):
    ###################
    ### Your code here!

    # for element in iterable:
    #     <something involving element>







    ###################
    return mean

assert (gpaMean(myStudents) - 3.8) < .0001, 'Mean wrong or not precise!'

'''
Exercise 2: GPA Means, II

In this exercise, we will build on the previous exercise, introducing
    the idea of control flow. Here, we will only consider the mean gpa
    of the male students.

You will likely find the `if (condition):` syntax useful here.
'''

def gpaMeanMale(students):
    ###################
    ### Your code here!

    # if (condition):
    #     <do something>
    # else:
    #     <do another thing>










    ###################
    return mean

assert (gpaMeanMale(myStudents) - 3.75) < .0001, 'Mean wrong or not precise!'


print('Lab 2 complete!')