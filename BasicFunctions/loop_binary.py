num_string = input('Input a number: ')
num = int(num_string)
length = int(len(num_string))

done = False
num_binary_reverse = ''

while done == False:
    current_digit = num % 2
    num = int(num / 2)
    num_binary_reverse += str(current_digit)
    if num == 0:
        done = True

num_binary = num_binary_reverse[::-1]
print(num_string + ' is equal to ' + num_binary + ' in binary')