#Cyrus Smeltzer Lab 6 GitHub

def encode(password):
    encoded_password = ''
    for num in password:
        num = int(num)
        new_num = (num) + 3
        if new_num > 9:
            new_num -= 10
        encoded_password += str(new_num)
    return encoded_password


# Harrison Chojnowski Decode Funciton
def decode(password):
    decoded_password = ''
    for num in password:
        num = int(num)
        num -= 3
        if num < 0:
            num += 10
        decoded_password += str(num)
    return decoded_password


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
        print(f'The endcoded password is {encoded_password}, and the original password is {decode(encoded_password)}.')
    if option == 3:
        program = False