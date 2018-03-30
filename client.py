'''Created on Mar 8, 2018

@author: Kisife Giles
COMP 348 Assignment 2.
ID: 40001926
'''
import socket
import sys

HOST, PORT = "localhost", 5000
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect((HOST, PORT))   

# Method request a query category and presents user with corresponding input options.
def runningQuery():
    
    category = input("Please, select a query category->: 1,2,3 ...8.")
    query_statement=""
    
    if category=='1':
        print("Category 1")
        query_statement = input("Enter the name of the customer to find: ")
        print(" ")
      
    elif category== '2':
        name = input("Enter customer name: ")
        print(" ")
        age = input("Enter customer's age: ")
        print(" ")
        address= input("Enter customer's address: ")
        print(" ")
        telNr = input("Enter customer's phone number: ")
        print(" ")
        entry = name +"|"+age+"|"+address+"|"+telNr
        reportEntry = entry
        print(" ")
        print("Adding customer customer: "+ reportEntry)
        query_statement= entry
        print(" ")
        
    elif category== '3':
        print("Query category is : 3, delete customer")
        name = input("Enter customer's name")
        confirmation = input("Are you sure you want to DELETE " +name+" from the database?:-> Y/N")
        if confirmation =="Y" or confirmation=="y":
            query_statement=name 
            print(" ")
        else: pass
        
        
    elif category=='4':
        print("Query category is : 4, update customer age: ")
        name = input("Enter customer's name")
        correctAge = input("Enter "+name+ " 's correct age: ")
        query_statement=name +"|"+ correctAge
        print(" ")
        
    elif category== '5':
        print("Query category is : 5, update customer address: ")
        name = input("Enter customer's name")
        correctAge = input("Enter "+name+ " 's correct address: ")
        query_statement=name +"|"+ correctAge
        print(" ")
        
    elif category=='6':
        print("Query category is : 6, update customer phone nr: ")
        name = input("Enter customer's name")
        correctAge = input("Enter "+name+ " 's correct telephone number: ")
        query_statement=name +"|"+ correctAge
        print(" ")
        
    elif category=='7':
        print("Query category is : 7, print report")
        print(" ")
        
    elif category=='8':
        print("Good bye and thank you for using my client/server application. The client application will now EXIT. ")
        sys.exit()
        
    return query_statement+"|"+category

received = None
#Method establishes a connection and sends data from client side to server side.
def runQuery(data_to_send):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))   
    
    try:
        # Connect to server and send data
        sock.sendall(bytes(data_to_send + "\n", "utf-8"))
        
        # Receive data from server.
        received = str(sock.recv(2048), "utf-8")
        print(" {}".format(received))
    finally:
        sock.close()
 # Method continuously ask user for input options.        
def running ():
    while True:
        myQuery = runningQuery()
        if myQuery is not None:
            runQuery(myQuery)
            print(" ")
            status = input("Do you wish to run a query?: -> Y/N")
            if status =="Y" or status =="y":
                running()
            else:
                status = input("Do you want to exit?: -> Y/N")
                if status =="Y" or status =="y":
                    print("Thank you for using my application!")
                    sys.exit()
        else:
            pass
    
running()
    