# #! str - > string
# #? int - > integer
# #* bool - > True(1), False (0)
# #!dict - > dictionary
# #?set - > set
# #*list -> list
# #*tuple

# #? STRING

string1 = 'a'
string2 = "a"
string3 = """a"""
string4 = '''a'''

string = 'string'
# string = string.capitalize() #? Верхній реєстр першої букви
# string = string.casefold() #? Переводить в нижній реєстр
# string = string.upper()  #? Переводить все в верхній реєстр
# string = string.lower() #? Переводить все в верхній реєстр
# string = string.count('letter from the string') #? count all the same latters
# string = string.startswith("st") #? we will get boolean True if the this letter is the first letter of the string else Fales
# string = string.endswith("ing") #? we will get boolean True if the this letter is the last letter of the string else Fales


# string = string.index('r') #? display index of the letter
# string = string.find('r') #? display index of the letter
# string = string.replace('st','St') #? raplace letters (from old to new)
# string = string.title #? transfer first letter to uppercase
# string = string.swapcase() #? swapcase of whole lettters
# string = string.split('s') #? split the string by the letter(s)
# string = string.strip() #? remove all spaces from the edge of the word(s)
# string = string.zfill(10) #!
# string = string.join('HE') #* 

# print(string)


integer = 1

#! INTEFERS
# decimal = Decimal() десяток
# fraction = Fraction() дробь
#2j + 1
a = 1
b = 2
c = 0
# c = a % b
# c = 3 % 2
# c += a
# - + * / // % **

# #! BOOLEAN
print(4 != 5)

# #! DICTIONARY

dictionary = {
    'name': 'Ivan',
    'age': 19
}

dictionary['bio'] = 'gamer'

print(dictionary['bio'])
del dictionary['bio']

dictionary['bio'] = 'мамкин синок'

print(dictionary)

for obj in dictionary:
    print(obj, dictionary[obj])

b = dict()
print(b)

# #! LIST

list_of_numbers = [1,2,3,4,5,6]
# list_of_numbers += [1,2,3,4,5,6]

# list_of_numbers.append(10)
# list_of_numbers.pop()
print(list_of_numbers)
# print(list_of_numbers[0:2])

for item in list_of_numbers:
    print(item)

a = True
while a == True:
    print(list_of_numbers)
    a = False
else:
    print('fuck')

a = 5
if a == 2:
    print('hi')
elif a % 2 == 0:
    print('ye boy')
else:
    print('cyka')

# a = 'a'
# b = 'b'
# c = 'a' 'b'
# print(c)
# print(a+b)

# name= 'vanya'
# age = '19'
#p9dok = 'Hi, my name is {0}, I am {1} years old'.format(name,age)
# p9dok = 'Hi, my name is ' + name + ' I am ' + age + ' years old'.format(name,age)

# print(p9dok)

def full_name(first_name, last_name):
    # print (first_name + ' ' + last_name)
    return first_name + ' ' + last_name

name = full_name("Ivan", "Malashenko")
print(name)