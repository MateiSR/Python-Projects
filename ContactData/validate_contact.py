# Validate phone no + mail & register in a file, salvat in variabila username + domain mail; 2 siruri de elemente, cate elemente din a < toate din b
import os
mail_valid = False
phone_valid = False

mail_address = ''
phone_no = ''

mail_valid1 = mail_address.find('@')
mail_valid2 = mail_address.find('.com')

current_dir = os.getcwd()

while mail_valid == False: 
    mail_valid1 = mail_address.find('@')
    mail_valid2 = mail_address.find('.com')
    mail_valid3 = mail_address.find('.net')

    if mail_valid1 != -1 and mail_valid2 != -1 or mail_valid3 != -1:
        mail_valid = True

        print('Mail address valid (saving to file)')

    else:
        mail_valid = False
        mail_address = input('Enter your email address: ')
        continue
    
with open(current_dir + "/two_digit.txt", "r") as file1:
    list2 = eval(file1.readline())
with open(current_dir + "/three_digit.txt", "r") as file2:
    list3 = eval(file2.readline())


valid_prefix = False
while valid_prefix == False:
    phone_prefix = input('Enter your phone prefix: ')
    if len(phone_prefix) == 1:
        if phone_prefix == '1' or phone_prefix == '7':
            valid_prefix = True
            #print('ok 1')
    if len(phone_prefix) == 2 and valid_prefix == False:
        for i in range(0, len(list2)):
            if phone_prefix[0] == list2[i][0] and phone_prefix[1] == list2[i][1]:
                valid_prefix = True 
                #print('ok 2')
    if len(phone_prefix) == 3 and valid_prefix == False:
        for i in range(0, len(list3)):
            if phone_prefix[0] == list3[i][0] and phone_prefix[1] == list3[i][1] and phone_prefix[2] == list3[i][2]:
                valid_prefix = True 
                #print('ok 3')
done = False
while done == False:
    if valid_prefix == True:
        phone_no = input('Please enter your phone number (without the prefix): ')
        if len(phone_prefix) == 1:
            if len(phone_no) == 10:

                print('Contact info OK (saving to file)')

                done = True
            elif len(phone_no) != 10:
                print('Phone number should be 10 long.')
        if len(phone_prefix) == 2:
            if len(phone_no) == 9:

                print('Contact info OK (saving to file)')

                done = True
            elif len(phone_no) != 9:
                print('Phone number should be 9 long.')
        if len(phone_prefix) == 3:
            if len(phone_no) == 8:

                print('Contact info OK (saving to file)')

                done = True
            elif len(phone_no) != 8:
                print('Phone number should be 8 long.')

domain = mail_address[mail_address.index('@') + 1:len(mail_address)]
username = mail_address[0:mail_address.index('@')]

if done == True:
    if os.path.isdir(current_dir + '/output') != True:
        os.mkdir(current_dir + '/output')
        print('Creating directory \'/output/\'')
    if os.path.isfile(current_dir + '/output/users.txt') != True:
        os.mknod(current_dir + '/output/users.txt')
        print('Creating file \'output/users.txt\'')
    try:
        f = open(current_dir + '/output/users.txt', 'w')
        f.write('Username: \'' + username +'\'; Domain: \'' + domain + '\'; Phone: (' + str(phone_prefix) + ') ' + str(phone_no) + '\n')
        f.close()
    except OSError:
        print('Could not write to file')    