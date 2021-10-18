# data type

# primitive non-primitive
variable = True
variable_list = ['hung', 'hieu', 'tien', 'nhi']


# print(variable_list)

# index - starts from 0
# print(variable_list[0]) #tien
# print(variable_list[2]) #tien
# print(variable_list[1]) # hieu
# print(variable_list[-1]) # nhi
# print(variable_list[-4]) # hung
#
# variable_list_again = ['hung', 'hieu', 'tien', 'nhi', 'hung']
# print(variable_list_again)
#
# unique_set = set(variable_list_again)
# print(unique_set)
#
# hieu_list = ['hieu', '12345', 'vietnam']
# hieu_list[0]
# hieu_list[1]
# hieu_list[2]
#
# hieu_dictionary = dict()
# # { key : value }
# name_key = 'name'
# phone_key = 'phone'
# country_key = 'country'
#
# hieu_dictionary[name_key] = 'hieu'
# hieu_dictionary[phone_key] = '12345'
# hieu_dictionary[country_key] = ['vietnam', 'finland']
#
# print(hieu_dictionary[name_key])
#
# tien_dictionary = dict()
# tien_dictionary[name_key] = 'tien'
# tien_dictionary[phone_key] = '456789'
# tien_dictionary[country_key] = ['finland', 'vietnam']
#
# print(tien_dictionary)

# name = input('Enter name: ')
# print(name)
# second_name = input('Enter name: ')
# print(second_name)
#
# print('lala')
# print(name)

# save unknown numbers of name - for loop
#
# number1 = 4
# number2 = 5
# print(number1 + number2)
#
# first_number = input('Enter the first number ')
# second_number = input('Enter the second number ')
# print(first_number + second_number)
# string concatenation (concatenate)
# print('4' + '5')

[0,1,2,3,4,5]
for hung in range(0,6):
    print(hung)
    first_number = input('Enter the first number ')
    second_number = input('Enter the second number')
    first_number = int(first_number)
    second_number = int(second_number)
    print(first_number + second_number)

# co so du lieu
# database = list()
# occurences = input('Enter number of names that you would like to input: ')
# for i in range (0, int(occurences)):
#     name = input('Enter a name: ')
#     print(name)
#     database.append(name)
#
# print(database)

# indentation , when why and how?

# while loop