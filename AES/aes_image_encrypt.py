from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
import getpass

key = getpass.getpass('Key: ')
key = key.encode('UTF-8')
key = pad(key,AES.block_size)

def encrypt (file_name,key):
    with open(file_name,'rb') as entry:
        data = entry.read()
        data = pad(data,AES.block_size)
        cipher = AES.new(key,AES.MODE_CFB)
        ciphertext = cipher.encrypt(data)
        iv = b64encode(cipher.iv).decode('UTF-8')
        ciphertext = b64encode(ciphertext).decode('UTF-8')
        to_write = iv + ciphertext
    entry.close()
    with open (file_name + '.enc','w') as data:
        data.write(to_write)
    data.close()

encrypt('image.jpg',key)
