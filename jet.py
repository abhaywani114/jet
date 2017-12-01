# @author Abrar Ajaz Wani
# @email abhaywani114@gmail.com'
# Dec-2017
import socket
class conx(object):
    port = int('80')
    addr = '127.0.0.1'
    encoding = 'utf-8'
    lis = ''
    data_length = 2024
    data_flow = 'Send_Recv'

    def __init__(self,family,protocol):
        self.family = family
        self.protocol = protocol

    def status(self):
        print((''))
        print('@JET:Status')
        print('Address: '+ self.addr)
        print('Port: ' + str(self.port))
        print('Protocol: ' + str(self.protocol))
        print('Family: ' + str(self.family))
        print('Encoding: ' + str(self.encoding))
        print('Buffer: '+str(self.data_length))
        print("Data Flow: "+ str(self.data_flow))
        print('')

    def listen(self):
        try:
            print('')
            print('@Conx:listen')
            print("Creating New Socket...")
            self.s = socket.socket(self.family,self.protocol)
            print("Binding:"+ str(self.addr) + " At: "+ str(self.port) + '...')
            self.s.bind((self.addr,self.port))
            self.lis = True
            self.s.listen(int(input("Enter no of connection to listen for> ")))
            print("Started Listning")
        except:
            print("Some Error Occurred")
            print("Check settings... (Type 'status' to review)")

        print("Waiting for an connection!")
        conn, addr_in = self.s.accept()
        print("Connection from: " + str(addr_in))
        trans = True
        while trans:
            if self.data_flow == 'Send_Only':
                self.get_data(conn)
                while trans:
                    trans = self.snd(conn)
            elif self.data_flow == 'Send_Only+':
                while trans:
                    trans = self.snd(conn)
            elif self.data_flow == 'Recv_Only':
                while True:
                 self.get_data(conn)
            elif self.data_flow == 'Send_Recv':
                self.get_data(conn)
                trans = self.snd(conn)
            else:
                print("Invalid Data Flow!")

    def get_data(self,conn):
        print('')
        print("Listing to Client...")
        data = conn.recv(self.data_length)
        print(str(data, self.encoding))
        print('')

    def snd(self,conn):
        data = bytes(input("Enter Data to send> ")+'\n', self.encoding)
        try:
            conn.send(data)
        except:
            print("Some Error Occurred while sending data")
            print('')
            return False
        if str(data, self.encoding) == 'done':
            conn.close()
            print("Connection Closed")
            return False
        print("Data Sent...")
        print('')
        return True

    def open(self):
        print('')
        print("@Creating Socket")
        self.s = socket.socket(self.family, self.protocol)
        print("Accessing: " + self.addr + ' At port: '+str(self.port))
        try:
            conn = self.s.connect((self.addr,self.port))
            print('Connection Established!')
        except:
            print("Error in establishing connection.")
            return False

        trans = True
        if self.data_flow == 'Send_Only':
            while trans:
                trans = self.snd(self.s)
        elif self.data_flow == 'Send_Only+':
            while trans:
                trans = self.snd(self.s)
        elif self.data_flow == 'Recv_Only':
            while True:
                self.get_data(self.s)
        elif self.data_flow == 'Send_Recv':
            while trans:
                trans = self.snd(self.s)
                self.get_data(self.s)
        else:
            print("Invalid Data Flow!")

    def close(self):
        try:
            print('Closing Socket if open!')
            self.s.close()
            print("Socket Closed")
        except:
            print("No socket open! Exiting!")



sock_obj = conx(socket.AF_INET,socket.SOCK_STREAM)
print('''
            JET-SOCKET TESTER
    Simple But Powerful Sock Tester
    Developed By: Abrar Ajaz Wani
    E-Mail: abhaywani114@gmail.com 
''')
while True:
    print('')
    cmd = str(input("Please Enter a command> "))

    if cmd == 'status':
        sock_obj.status()
    if cmd == 'target':
        target = str(input("Enter target's IP address: "))
        sock_obj.addr = target
        print('Target Updated...')
    if cmd == 'port':
        target = str(input("Enter Port: "))
        sock_obj.port = target
        print('Port Updated...')
    if cmd == 'family':
        target = str(input("Enter Socket Family: "))
        sock_obj.family = target
        print('Family Updated...')
    if cmd == 'protocol':
        target = str(input("Enter Socket Protocol: "))
        sock_obj.protocol = target
        print('Protocol Updated...')
    if cmd == 'buffer':
        sock_obj.data_length = int(input("Enter buffer size: "))
        print('Buffer Size Updated...')
    if cmd == 'encoding':
        sock_obj.encoding = str(input("Enter encoding: "))
        print("Encoding Updated...")

    if cmd == 'help':
        print('''
        JET Help Page
JET is simply a socket testing tool developed in python.
Developer: Abrar Ajaz Wani
E-mail: abhaywani114@gmail.com
Facebook: @abhay.waniii.9
_____________________________________
    Command -> Description
    
1. status -> Review socket environment
2. target -> Change the address of socket
3. port -> Change the port of socket
4. family -> Change the socket family
5. protocol -> Change socket protocol
6. encoding -> Change data encoding
7. data_flow -> Change Data flow
8. L -> Start listning on a specified port
9. O -> Open a remote host
10. R -> Reset settings 

        ''')

    if cmd == 'data_flow':
        sock_obj.data_flow = str(input("Enter Data-Flow [Send_Recv, Send_Only, Recv_Only,Send_Only+] "))
        print('Dara Flow Updated')
    if cmd == 'L':
        sock_obj.listen()
    if cmd == 'R':
        print('')
        print('@Resetting')
        print("Destroying existing settings...")
        del(sock_obj)
        print("Creating new environment")
        sock_obj = conx(socket.AF_INET, socket.SOCK_STREAM)
    if cmd == 'O':
        sock_obj.open()
    if cmd == 'exit':
        sock_obj.close()
        break

