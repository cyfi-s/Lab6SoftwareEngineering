#Cyrus Smeltzer Lab 6 GitHub

def encode(password):
    encoded_password = ''
    for num in password:
        new_num = int(num) + 3
        encoded_password += str(new_num)
    return encoded_password



program = True

while program == True:
    print()
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()
    option = int(input('Please enter an option: '))
    if option == 1:
        encoded_password = encode(input('Please enter your password to encode: '))
        print('Your password has been encoded and stored!')

    if option == 2:
        print(f'The endcoded password is {encoded_password}, and the original password is {decoder(encoded_password)}.')
    if option == 3:
        program = False