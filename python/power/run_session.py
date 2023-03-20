import socket
import pickle
import session_resources as sr
import score


def run_inference(tokenizer, model,  session):
    input = "{\"question\": \"What is Dolly Parton's middle name?\", \"context\": \"Dolly Rebecca Parton is an American singer-songwriter\"}"
 
    #return score.run(tokenizer, session, input)
    return score.run_pytorch(tokenizer, model, input)


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    data = client_socket.recv(1024000)

    print(data)
    
    resources = pickle.loads(data)  # receive response

    output = run_inference(resources.tokenizer, resources. model, resources.session)

    print(output)

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()