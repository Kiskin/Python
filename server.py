'''
Created on Mar 10, 2018

@author: Kisife Giles
COMP 348 Assignment 2.
ID: 40001926
'''
import socketserver
import QueryProcessing
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(2048).strip()
       # print("{} wrote:".format(self.client_address[0]))
        aQuery = self.data.decode("utf-8")
        splitQuery = aQuery.split("|")
        passedString =aQuery[:-2]
        bQuery = QueryProcessing.serverReply(splitQuery[len(splitQuery)-1],passedString)
       
       # Send the query results from the server to the client.
        if bQuery:
            self.request.sendall(str.encode(bQuery))
            
        else:self.request.sendall(str.encode("Customer not found in the database!"))

if __name__ == "__main__":
    HOST, PORT = "localhost", 5000

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()    
