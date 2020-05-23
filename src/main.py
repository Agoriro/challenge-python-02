# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
    numcaracters = random.randint(8,16)
    password = ''
    nummitad = int(numcaracters/2)
    contmin = 0
    contmay = 0
    contnum = 0
    contsym = 0
    for idx in range(numcaracters):
        opc = random.randint(1,4) 
        if idx == nummitad:
            if contmin == 0:
                opc = 1
            elif contmay == 0:
                opc = 2
            elif contnum  == 0:
                opc = 3
            elif  contnum == 0:
                opc = 4

        if opc == 1: #minusculas
            nummin = random.randint(97,122)
            password = password + chr(nummin) 
            contmin += 1
        elif opc == 2: #mayusculas
            nummay = random.randint(65,90)
            password = password + chr(nummay) 
            contmay += 1
        elif opc == 3: #numeros
            num = random.randint(48,57)
            password = password + chr(num) 
            contnum += 1
        elif opc == 4: #simbolos
            numidx = random.randint(0,len(SYMBOLS)-1)
            password =password + SYMBOLS[numidx]
            contsym += 1
    print(password)
    return password

    #pass

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
