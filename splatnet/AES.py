from Crypto.Cipher import AES
from secrets import token_bytes

#Using a 256 bit key for extra security. My Database is farily small so I can afford the extra computation. 
key = token_bytes(32)

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_GCM)  #Creates a cipher object and sets the mode to EAX
    nonce = cipher.nonce         #creates a number used onc
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

nonce, ciphertext, tag = encrypt(input('Enter a message: '))
plaintext = decrypt(nonce, ciphertext, tag)
print(f'Cipher text: {ciphertext}')
if not plaintext:
    print('Message is corrupted')
else:
    print(f'Plain text: {plaintext}')