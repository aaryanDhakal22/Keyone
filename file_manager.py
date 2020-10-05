from Crypto.Cipher import AES
from ast import literal_eval as levl
key = b'nevergonagiveuUP'


def add_pass(password):
    # nonce, tag, ciphertext = password.AES
    ciphered = password.AES

    website = password.website   
    username = password.username 
    file_out = open("encrypted.af", "a")
    for i in [website,username,str(ciphered)]:
        file_out.write(i)
        file_out.write("\n")
    file_out.close()
    
    

def view_pass(website,key):
    file_in = open("encrypted.af",'r')
    contents = file_in.readlines()
    filtered_contents = [contents[i][:-1] for i in range(len(contents)) if contents[i] != '\n']
    storage = dict()
    a = 0
    for i in range(int((len(filtered_contents)/3))):
        storage.setdefault(filtered_contents[a],{'username':filtered_contents[a+1],'aes':filtered_contents[a+2]})
        a+=3

    aes_info = levl(storage[website]['aes'])
    username = storage[website]['username']
    
    nonce = aes_info['nonce']
    tag = aes_info['tag']
    ciphertext = aes_info['ciphertext']
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data.decode('utf-8')