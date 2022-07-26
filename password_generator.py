import string
import random
print('PASSWORD GENERATOR')

alphabet = list(string.ascii_letters)
digits = list(string.digits)
symbols = list("!@#$%^&*()")
characters = list(alphabet+digits+symbols) 

random.shuffle(alphabet)
random.shuffle(digits)
random.shuffle(symbols)



def len():
    lenght = int(input('How long your password should be? '))
    alphabet_number = int(input('How many letters should your password have? '))
    digits_number = int(input('How many digits should your password have? '))
    symbols_number = int(input('How many symbols should your password have? '))

    if lenght < alphabet_number + digits_number + symbols_number:
        print('Number of choosen characters is bigger than chosen lenght of the password!')
        len()
    else:
        password = []

        for i in range(alphabet_number):
            password.append(random.choice(alphabet))

        for i in range(digits_number):
            password.append(random.choice(digits))

        for i in range(symbols_number):
            password.append(random.choice(symbols))

        if lenght > alphabet_number + digits_number + symbols_number:
            for i in range(lenght-alphabet_number + digits_number + symbols_number):
                password.append(random.choice(characters))


        random.shuffle(password)

        print("".join(password))

len()   
    

