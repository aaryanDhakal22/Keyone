from password_generator import Password
from file_manager import add_pass,view_pass
import pyperclip
from hashlib import sha256

# Dont show this to anyone  
key = b'nevergonagiveuUP'

print('#'*58)
print('\t\t\tKEYONE')
print('#'*58)

# Master Password Authentication
while True:

    master_pass = input('Enter the Master Password : ')

    if sha256(master_pass.encode('utf-8')).hexdigest() == sha256('rickroll'.encode('utf-8')).hexdigest():
        break
    else:
        print("Sorry! Please Try Again ")

#Password catalogue 
while True:
    print("\n   What would you like today?\n")
    print('[C]reate\t[V]iew\t\t [E]xit\n')
    operation = input("\t>").lower()

    if operation == 'c':
        username = input('\nUsername/email: ')
        website = input('\nWebsite: ')
        symbols = input('\nSymbols(y/n): ')
        symbols_req = True if symbols == 'y' else False
        new_password = Password(website,username,key,symbols_req)
        pyperclip.copy(new_password.password)
        add_pass(new_password)
        print('\n')
        print('-'*30)
        print("Password Copied to Clipboard")
        print('-'*30)
        print('\n')

    elif operation =='v':
        website = input('\nWebsite: ')
        password = view_pass(website,key)
        pyperclip.copy(password)
        print('\n')
        print('-'*20)
        print("Password Copies to Clipboard")
        print('-'*20)
        print('\n')


    elif operation =='e':
        break

    else:
        print("Invalid Option")
