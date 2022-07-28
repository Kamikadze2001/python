from random import randint

random = []
number_of_plays = 0
user_input = 0
def number():
    global user_input
    user_input = int(input('Input a 4 digit number '))
    if user_input > 9999 or user_input < 1000:
        print('Wrong input')
        number()
    else:
        global number_of_plays
        if number_of_plays == 0:
            generate()
            number_of_plays += 1
            conversion()
        else:
            number_of_plays += 1
            conversion()

def conversion():           
    list_to_string()
    user_list = list(map(int, str(user_input)))
    cow = 0
    for i in range(4):
        if random[i] == user_list[i]:
            cow += 1
    bulls = 0
    bulls = len(set(random) & set(user_list)) - cow
        
    if cow != 4:
        print(random)
        print('Try again!',cow, 'cows', bulls, 'bulls')
        number()
    else:
        print('You won! The number was',list_to_string(),'Number of tries needed:',number_of_plays)

def generate():  
    for i in range(1):
        number = randint(1,9)
        random.append(number)
    for i in range(3):
        number = randint(0,9)
        random.append(number)    

def list_to_string():
    string = ""        
    string_list = [str(intiger) for intiger in random]
    string_number = string.join(string_list)
    return string_number

        
number()


