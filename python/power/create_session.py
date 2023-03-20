import multiprocessing as mp
import socket
import pickle
import numpy as np
import session_resources as sr

global session, sessionStarted


def create_resources():
    print("Starting ONNX Runtime session ...")

    resources = sr.SessionResources()

    print("... session started")

    return resources

def start_server():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)

    resources = create_resources()

    while (True):

        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))

        data = pickle.dumps(resources)
    
        conn.send(data)  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    mp.set_start_method('spawn') # This is important and MUST be inside the name==main block.

    start_server()
