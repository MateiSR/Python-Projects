# Library for colored text
#from termcolor import colored, cprint
# List of movies
films = {
    "Sonic The Hedgehog": {'age': 13, 'seats': 100}, #1
    "The Invisible Man": {'age': 18, 'seats': 50}, #2
    "Onward": {'age': 13, 'seats': 95}, #3
    "Harley Quinn: Birds of Prey": {'age': 15, 'seats': 80}, #4
    "Bloodshot": {'age': 15, 'seats': 75}, #5
    "The Hunt": {'age': 15, 'seats': 80}, #6
    "Terminator: A Dark Fate": {'age': 15, 'seats': 120}, #7
    "Lassie Come Home": {'age': 13, 'seats': 90}, #8
    "Miami Bici": {'age': 15, 'seats': 100}, #9
    "Little Joe": {'age': 15, 'seats': 80} #10
}
# Clear function
def cls():
    print("\n" * 100)
# Print list
def print_list(films):
    print('~~         Which movie would you like to book a seat for?          ~~')
    print('1. Sonic The Hedgehog | Seats left: ' + str(films['Sonic The Hedgehog']['seats']) + ' | Age Rating: ' + str(films['Sonic The Hedgehog']['age']))
    print('2. The Invisible Man | Seats left: ' + str(films['The Invisible Man']['seats']) + ' | Age Rating: ' + str(films['The Invisible Man']['age']))
    print('3. Onward | Seats left: ' + str(films['Onward']['seats']) + ' | Age Rating: ' + str(films['Onward']['age']))
    print('4. Harley Quinn: Birds of Prey | Seats left: ' + str(films['Harley Quinn: Birds of Prey']['seats']) + ' | Age Rating: ' + str(films['Harley Quinn: Birds of Prey']['age']))
    print('5. Bloodshot | Seats left: ' + str(films['Bloodshot']['seats']) + ' | Age Rating: ' + str(films['Bloodshot']['age']))
    print('6. The Hunt | Seats left: ' + str(films['The Hunt']['seats']) + ' | Age Rating: ' + str(films['The Hunt']['age']))
    print('7. Terminator: A Dark Fate | Seats left: ' + str(films['Terminator: A Dark Fate']['seats']) + ' | Age Rating: ' + str(films['Terminator: A Dark Fate']['age']))
    print('8. Lassie Come Home | Seats left: ' + str(films['Lassie Come Home']['seats']) + ' | Age Rating: ' + str(films['Lassie Come Home']['age']))
    print('9. Miami Bici | Seats left: ' + str(films['Miami Bici']['seats']) + ' | Age Rating: ' + str(films['Miami Bici']['age']))
    print('10. Little Joe | Seats left: ' + str(films['Little Joe']['seats']) + ' | Age Rating: ' + str(films['Little Joe']['age']))
    
# List of numbers
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# Define verification
correct = False
input_valid = True

# Infinite Loop, Movie Selection
while correct == False and input_valid != False:
    cls()
    print_list(films)
    input_one = input('Which movie would you like to watch? ').strip().title()
    
    # If input is valid, pass, else ask again
    if input_one in nums: input_valid = True
    else: del input_one
    
    # Ask for age
    
    age = input('How old are you? ')
    
    # Check for selection
    if input_one == '1': 
        if int(age) >= films['Sonic The Hedgehog']['age']:
            print('Age is valid.')
            if films['Sonic The Hedgehog']['seats'] > 0:
                print('Reserving seat..')
                films['Sonic The Hedgehog']['age'] = str(int(films['Sonic The Hedgehog']['age']) - 1)
                break
            
    elif input_one == '2': 
        if int(age) >= films['The Invisible Man']['age']:
            print('Age is valid.')
            if films['The Invisible Man']['seats'] > 0:
                print('Reserving seat..')
                break
            
    elif input_one == '3': 
        if int(age) >= films['Onward']['age']:
            print('Age is valid.')
            if films['Onward']['seats'] > 0:
                print('Reserving seat..')
                break
            
    elif input_one == '4': 
        if int(age) >= films['Harley Quinn: Birds of Prey']['age']:
            print('Age is valid.')
            if films['Harley Quinn: Birds of Prey']['seats'] > 0:
                print('Reserving seat..')
                break
            
    elif input_one == '5': 
        if int(age) >= films['Bloodshot']['age']:
            print('Age is valid.')
            if films['Bloodshot']['seats'] > 0:
                print('Reserving seat..')
                break
            
    elif input_one == '6': 
        if int(age) >= films['The Hunt']['age']:
            print('Age is valid.')
            if films['The Hunt']['seats'] > 0:
                print('Reserving seat..')
                break
            
    elif input_one == '7': 
        if int(age) >= films['Terminator: A Dark Fate']['age']:
            print('Age is valid.')
            if films['Terminator: A Dark Fate']['seats'] > 0:
                print('Reserving seat..')
                break
            
    elif input_one == '8': 
        if int(age) >= films['Lassie Come Home']['age']:
            print('Age is valid.')
            if films['Lassie Come Home']['seats'] > 0:
                print('Reserving seat..')
                break
            
    elif input_one == '9': 
        if int(age) >= films['Miami Bici']['age']:
            print('Age is valid.')
            if films['Miami Bici']['seats'] > 0:
                print('Reserving seat..')
                break
            
    elif input_one == '10': 
        if int(age) >= films['Little Joe']['age']:
            print('Age is valid.')
            if films['Little Joe']['seats'] > 0:
                print('Reserving seat..')
                break