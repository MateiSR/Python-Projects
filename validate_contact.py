# Validate phone no + mail & register in a file, salvat in variabila username + domain mail; 2 siruri de elemente, cate elemente din a < toate din b
import os
mail_valid = False
phone_valid = False

mail_address = ''
phone_no = ''

mail_valid1 = mail_address.find('@')
mail_valid2 = mail_address.find('.com')


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
    
list1 = ['1', 
'7']
list2 = ['30',
'31',
'32',
'33',
'34',
'35',
'36',
'37',
'38',
'39',
'40',
'41',
'42',
'43',
'44',
'45',
'46',
'47',
'48',
'49',
'50',
'51',
'52',
'53',
'54',
'55',
'56',
'57',
'58',
'59',
'60',
'61',
'62',
'63',
'64',
'65',
'81',
'82',
'83',
'84',
'90',
'91',
'92',
'93',
'94',
'95']
list3 = ['211',
'212',
'213',
'214',
'215',
'216',
'217',
'218',
'219',
'220',
'221',
'222',
'223',
'224',
'225',
'226',
'227',
'228',
'229',
'230',
'231',
'232',
'233',
'234',
'235',
'236',
'237',
'238',
'239',
'240',
'241',
'242',
'243',
'244',
'245',
'246',
'247',
'248',
'249',
'250',
'251',
'252',
'253',
'254',
'255',
'256',
'257',
'258',
'259',
'260',
'261',
'262',
'263',
'264',
'265',
'266',
'267',
'268',
'269',
'270',
'271',
'272',
'273',
'274',
'275',
'276',
'277',
'278',
'279',
'280',
'281',
'282',
'283',
'284',
'285',
'286',
'287',
'288',
'289',
'290',
'291',
'292',
'293',
'294',
'295',
'296',
'297',
'298',
'350',
'351',
'352',
'353',
'354',
'355',
'356',
'357',
'358',
'359',
'360',
'361',
'362',
'363',
'364',
'365',
'366',
'367',
'368',
'369',
'370',
'371',
'372',
'373',
'374',
'375',
'376',
'377',
'378',
'379',
'380',
'381',
'382',
'383',
'384',
'385',
'386',
'387',
'388',
'500',
'501',
'502',
'503',
'504',
'505',
'506',
'507',
'508',
'509',
'670',
'671',
'672',
'673',
'674',
'675',
'676',
'677',
'678',
'679',
'680',
'681',
'682',
'683',
'684',
'685',
'686',
'687',
'688',
'689',
'690',
'691',
'850',
'851',
'852',
'853',
'854',
'855',
'856',
'857',
'858',
'960',
'961',
'962',
'963',
'964',
'965',
'966',
'967',
'968',
'969',
'970',
'971',
'972',
'973',
'974',
'975',
'976',
'977',
'978',
'979',
'980',
'981',
'982',
'983',
'984',
'985',
'986',
'987',
'988',
'989',
'990',
'991',
'992',
'993',
'994',
'995',
'996',
'997']

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
        phone_no = input('Please enter your phone number (without the prefix: ')
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

# save 
if done == True:
    if os.path.isdir('output') != True:
        os.mkdir('output')
        print('Creating directory \'/output/\'')
    if os.path.isfile('output/users.txt') != True:
        os.mknod('output/users.txt')
        print('Creating file \'/output/users.txt\'')
    try:
        f = open('output/users.txt', 'w')
        f.write('Username: \'' + username +'\'; Domain: \'' + domain + '\'; Phone: (' + str(phone_prefix) + ') ' + str(phone_no))
        f.close()
    except OSError:
        print('Could not write to file')    