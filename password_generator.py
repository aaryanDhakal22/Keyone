import random as rd
import pyperclip
from Crypto.Cipher import AES

class Password():

    def __init__(self,website, username,key, symbols=False):
        self._website = website
        self._username = username
        self._symbols = symbols
        self._key = key
        self._password = Password.pass_gen(self,self._symbols)
        self._AES = Password.AES_cipher(self._password,self._key)
        

    
    @staticmethod
    def symbol_pass_gen():
        results = Password.normal_pass_gen()
        result_list = list(results)

        # Randomly inserts symbols into the password
        for _ in range(5):
            symbol = str(chr(rd.randint(33,47)))
            index = rd.randint(0,17)
            result_list.insert(index,symbol)
        return ''.join(result_list)

    @staticmethod
    def normal_pass_gen():
        password = ''

        #Actual Randomizer
        for _ in range(18):
            uppers = chr(rd.randint(65,90))
            lowers = chr(rd.randint(97,122))
            numbers = rd.randint(0,9)
            password += str(rd.choice([uppers,lowers,numbers,lowers]))
        return password

    def pass_gen(self,symbol):
        #Password Generation according to symbol specification
        if symbol:
            func = Password.symbol_pass_gen()
        else:
            func = Password.normal_pass_gen()
        return func

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,text):
        print("Sorry this function is not allowed")

    @property
    def AES(self):
        return self._AES
        
    @property
    def website(self):
        return self._website

    @property
    def username(self):
        return self._username


    # Converts into AES cipher
    @classmethod
    def AES_cipher(cls,password,key):
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(bytes(password,'utf-8'))
        return {'nonce':cipher.nonce,'tag':tag,'ciphertext':ciphertext}


