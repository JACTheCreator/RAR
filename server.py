import socket 
from _thread import *
import threading 
  
print_lock = threading.Lock() 
key = '7r128iawNRAJVPoZDcR2rh4Oz_En3XW8UboAfM4keSg='
  
def threaded(c): 
    while True: 
        file_name = input("Enter the file that you want to Encrpyt: ")
        
        # C:\Users\JAC\Documents\UTECH\Software and System Security\4\Test.txt
        
        instructions = str(key) + ',' + (file_name)
        c.send(instructions.encode('utf-8'))

        data = c.recv(1024) 
        if not data: 
            print('Bye') 
            print_lock.release() 
            break
             
        print('STATUS: ', str(data.decode('utf-8'))) 

    c.close() 
  
  
def main(): 
    host = "" 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
    s.listen(5) 
    print("socket is listening") 
  
    while True: 
        c, addr = s.accept() 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
if __name__ == '__main__': 
    main() 