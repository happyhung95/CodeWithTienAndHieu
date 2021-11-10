# print('Bookstore: THH')
# print('Date: 10/11/2021')
# print('Items:')
# print('Item 1: Book 1')
# print('Item 2: Book 2')
# print('Total price: 20.00')
#
# print('Bookstore: THH')
# print('Date: 09/11/2021')
# print('Items:')
# print('Item 1: Book 3')
# print('Item 2: Book 4')
# print('Total price: 25.00')

# DRY - Don't Repeat Yourself

# method / function
# scope
# parameters / arguments
# def print_receipt(date_time, item_1, item_2, price):
#     print('Bookstore: THH')
#     print('Date: ' + date_time)
#     print('Items:')
#     print('Item 1: ' + item_1)
#     print('Item 2: ' + item_2)
#     print('Total price: ' + price)

# invoke method / execute method
# print_receipt('11/10/2021 18:33', 'Book 1', 'Book 2', '20.00')
# print_receipt('11/10/2021 18:34', 'Book 3', 'Book 4', '25.00')
# print_receipt(date_time='11/10/2021 18:34', price='27.00', item_1='Book1', item_2= 'Book2')


def print_name_card(name, city = 'Helsinki', job = 'SW dev'):
    print('Name: ' + name)
    print('Job: ' + job)
    print('City: '+ city)

# print_name_card('Tien', 'UX designer', 'Helsinki')
# print_name_card('Hieu', 'Data analyst', 'Helsinki')
# print_name_card('Hung')

# print_receipt('11/10/2021', 'Book 1', 'Book 2', '25.00')

# date_time = '10/10/2021'
# book_1 = 'Clean code'
# book_2 = 'Alice in wonderland'
# book_price = '20.00'
# print_receipt(date_time, book_1, book_2, book_price)
#
# name = 'hung'
# print(name)


def print_receipt(date_time, item_1, item_2, price):
    age = 25
    # date_time = '1/1/1991'
    print('Bookstore: THH')
    print('Date: ' + date_time)
    print('Items:')
    print('Item 1: ' + item_1)
    print('Item 2: ' + item_2)
    print('Total price: ' + price)
    print(name)

# print_receipt('1','2','3','4')

name = 'hung'

a = 0

if name == 'hung':
    a = 1
else:
    print('It is not Hung')

print(a)

# scope
# global / local
# function scope / loop scope
