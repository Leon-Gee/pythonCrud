clients= 'leon,sofia'

def create_client(client_name):
    global clients
    __add_comma()
    clients+= client_name
 


def __add_comma():
    global clients

    clients +=','


if __name__== '__main__':
    create_client('Scarm')
    print(clients)