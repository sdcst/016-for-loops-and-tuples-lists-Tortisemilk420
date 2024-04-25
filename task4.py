# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people=("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole")
num = int(input("Enter in a number less than 10: "))

if num < 11:
        print(f"{people[num]}")
if num >= 11:
        print("Enter a valid input")
