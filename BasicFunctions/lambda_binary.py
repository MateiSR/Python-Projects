global num, num_string, length
num_string = input('Input a number: ')
num = int(num_string)
numStart = num
length = int(len(num_string))

def binary_func(num):
    done = False
    num_binary_reverse = ''
    while done == False:
        current_digit = num % 2
        num = int(num / 2)
        num_binary_reverse += str(current_digit)
        if num == 0:
            done = True
        print(num_binary_reverse[::-1])

binary = lambda num : binary_func(num)

binary(numStart)