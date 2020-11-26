Coding Bat

# hello_name
name = input("What's your name?")
print("Hey, {}.".format(name))

# make_abba
a = input("Enter Anything:")
b = input("Enter Anything:")
print(a + b + b + a)

# first_two
word = input("Enter Anything:")
first_two = word[:2]
print(first_two)

# ends_ly
word = input("Enter A Word:")
if word[len(word)-2:] == 'ly':
    print("This word ends in ly.")
else:
    print("This word doesn't end in ly.")

# without_end_2
word = input("Enter A Word:")
middle = word[1:len(word)-1]
print(middle)

# at_first
word = input("Enter A Word:")
at_first = word[:2]
if len(word)>1:
    print(at_first)
else:
    print(word + '@')

# first_half
word = input("Enter Anything:")
first_half = word[:int(len(word)/2)]
print(first_half)

# combo_string
a = input("Enter Anything:")
b = input("Enter Anything:")
if len(a)>len(b):
    print(b + a + b)
else:
    print(a + b + a)

# last_two
word = input("Enter A Word:")
last_2 = word[len(word) -2:]
print(last_2)

# non_start
a = input("Enter Anything:")
b = input("Enter Anything:")
print(a[1:] + b[1:])

Python Workbook

# Even or Odd?
number = int(input("Enter A Number:"))
if number % 2 == 0:
	print("This number is even.")
else:
	print("This number is odd")

# Dog Years
human_years = int(input("What's the age in human years?"))
if human_years == 1:
    print('10.5')
elif human_years == 2:
    print('21')
else:
    print(21 + (human_years-2) * 4)

# Vowel or Consanant
letter = input("Enter A Letter:")

if letter in "aeiou":
	print("This letter is a vowel.")
elif letter == 'y':
  print("The letter y is sometimes a vowel and sometimes a consonant.")
else:
	print("This letter is a consonant.")

# Name that Shape
sides = int(input("Enter the amount of sides of your shape:"))
if sides == 3:
    print("Your shape is a triangle.")
elif sides == 4:
    print("Your shape can be a square, rectangle, rhombus, kite or pallaogram.")
elif sides == 5:
    print("Your shape is a pentagon.")
elif sides == 6:
    print("Your shape is a hexagon.")
elif sides == 7:
    print("Your shape is a hectagon.")
elif sides == 8:
    print("Your shape is an octagon.")
elif sides == 9:
    print("Your shape is a nonagon.")
elif sides == 10:
    print("Your shape is a decagon.")
else:
    print("This shape is too large or does not exist.")

# Month Name to Number of Days
month = input("Enter A Month:").lower()
if month == 'January':
    print('January has 31 days.')
elif month == 'February':
    print('February can have either 28 or 29 days.')
elif month == 'March':
    print('March has 31 days.')
elif month == 'April':
    print('April has 30 days.')
elif month == 'May':
    print('May has 31 days.')
elif month == 'June':
    print('June has 30 days.')
elif month == 'July':
    print('July has 31 days.')
elif month == 'August':
    print('August has 31 days.')
elif month == 'September':
    print('September has 30 days.')
elif month == 'October':
    print('October has 31 days.')
elif month == 'November':
    print('November has 30 days.')
elif month == 'December':
    print('December has 31 days.')
else: 
    print('ERROR: THIS IS NOT A MONTH')

# Sound Levels
db = int(input("What is the deciel level of the noise?"))
if db == 130:
    print('This is a Jackhammer.')
elif db == 106:
    print('This is a Gas Lawnmower.')
elif db == 70:
    print('This is an Alarm Clock.')
elif db == 40:
    print('This is a Quiet Room.')
elif 40 < db < 70:
    print('The noise is between a Queit Room and an Alarm Clock.')
elif 70 < db < 106:
    print('The noise is between an Alarm Clock and a Gas Lawnmower.')
elif 106 < db < 130:
    print('The noise is between a Gas Lawnmower and a Jackhammer.')
elif db < 40:
    print('This noise is almost unhearable.')
else:
    print("This noise is louder than average.")

# Name that Triangle
triangle_side_1 = float(input('What is the triangles first length in CM?'))
triangle_side_2 = float(input('What is the triangles second length in CM?'))
triangle_side_3 = float(input('What is the triangles third length in CM?'))
if triangle_side_1 == triangle_side_2 and triangle_side_2 != triangle_side_3 or triangle_side_2 == triangle_side_3 and triangle_side_3 != triangle_side_1 or triangle_side_3 == triangle_side_1 and triangle_side_1 != triangle_side_2:
    print('This is an isosceles triangle.')
elif triangle_side_1 == triangle_side_2 == triangle_side_3:
    print('This is an equilateral triangle.')
else: 
    print('This is a scalene triangle.')

# Note To Frequency
note = input('What is your note?')
if note == 'C4':
    print("The note's frequency is 261.63.")
elif note == 'D4':
    print("The note's frequency is 293.66.")
elif note == 'E4':
    print("The note's frequency is 329.63.")
elif note == 'F4':
    print("The note's frequency is 349.23.")
elif note == 'G4':
    print("The note's frequency is 392.00.")
elif note == 'A4':
    print("The note's frequency is 440.00.")
elif note == 'B4':
    print("The note's frequency is 493.88.")

# Faces on Money
money_value = int(input('What is the value of the banknote? $:'))
if money_value == 1:
    print('George Washington is on this coin.')
elif money_value == 2:
    print('Thomas Jefferson is on this coin.')
elif money_value == 5:
    print('Abraham Lincoin is on this bill.')
elif money_value == 10:
    print('Alexander Hamilton is on this bill.')
elif money_value == 20:
    print('Andrew jackson is on this bill.')
elif money_value == 50:
    print('Ulysses S. Grant is on this bill.')
elif money_value == 100:
    print('Benjamin Franklin is on this bill.')
else: 
    print('There is no banknote of this value.')

# Date to Holiday Name
month = input('Enter the month:').lower()
day = int(input('Enter the day:'))
if month == 'January' and day == 1:
    print("New Year's Day is on January 1.")
elif month == 'July' and day == 1:
    print("Canada Day is on July 1.")
elif month == 'December' and day == 25:
    print("Christmas Day is on December 25.")
else:
    print('There is no holiday on this day.')
