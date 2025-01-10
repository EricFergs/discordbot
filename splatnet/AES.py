from Crypto.Cipher import AES
from secrets import token_bytes
import os
from dotenv import load_dotenv
import base64

load_dotenv(override=True)
#Using a 256 bit key for extra security. My Database is farily small so I can afford the extra computation. 

#Key stored privately 
key = base64.b64decode(os.getenv("AES_KEY"))


def encrypt(token):
    cipher = AES.new(key, AES.MODE_GCM)  #Creates a cipher object and sets the mode to EAX
    nonce = cipher.nonce         #creates a number used onc
    ciphertext, tag = cipher.encrypt_and_digest(token.encode('ascii'))
    return nonce, ciphertext, tag  #Nonce and tag will need to be stored for decryption

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False


nonce, ciphertext, tag = encrypt("hello")
plaintext = decrypt(nonce, ciphertext, tag)
if not plaintext:
    print('Message is corrupted')
else:
    print(f'Plain text: {plaintext}')

 