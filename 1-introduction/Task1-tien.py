"""
Task:
    Ask the user for a number
    Tell the user if the number is odd or even
    Hint: use % operator
Extras:
    If the number is a multiple of 3, print "Third time's a charm"
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
        If {check} divides evenly into {num}, print "They are in a family".
        If not, print "They are strangers"
"""

#number = int(input('Enter a number'))
#answer = number % 2
#if answer > 0:
    #print("This is an odd number.")
#else:
    #print("This is an even number.")

charm = int(input('Enter a number'))
task_2 = charm % 3
print(charm)
print(task_2)
if task_2 == 0:
    print("Third time is a charm.")

#num = int(input("Enter the first number"))
#check = int(input("Enter the second number"))
#task_3 = check % num
#if task_3 > 0:
    #print("They are strangers")
#else:
    #print("They are in a family")