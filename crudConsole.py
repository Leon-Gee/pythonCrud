import sys


clients=[
    {
        'name': 'Oscar',
        'company': 'Google',
        'email': 'oscar.meza.leon@gmail.com'
        'position': 'developer'
    },
    {
        'name': 'Sofia',
        'company': 'tec',
        'email': 'sofia.algo@gmail.com'
        'position': 'RH'
    }
]
def client_create(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
        return True
    else:
        print("Client is already in the list")
        return False

def  delete_client(client_name):
    global clients
    if client_name in clients:
         clients.remove(client_name)

def _get_client_name():
    client_name = None


    while not client_name:
    
        client_name = input('What its the client name?')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name

def client_update(client_name,updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
        #clients[clients.index(client_name)] = updated_client_name
    else:
        print('The client doesnt exist')


def _client_search(client_name):
    global clients

    for client in clients:
        if client != client_name:
            continue
        else:
            return True

def read_client_list():
    global clients
    for idx,client in enumerate(clients):
        print('{}: {}'.format(idx,client))


def __print_welcome():

    print('Welcome to leon ventas')
    print('*' * 50)
    print('What would you like to do today? ')
    print('1. Create client')
    print('2. Read the list')
    print('3. Update Client')
    print('4. Delete client ')
    print('5. Search Client')

if __name__== '__main__':
    __print_welcome()
    f = True

    command = input()   
    if command == '1':
        client_name = _get_client_name()
        if client_create(client_name):
            print('The client has been added succesfully')
            read_client_list()
    elif command == '2':
        read_client_list()  
    elif command == '3':
        client_name = _get_client_name()
        client_name_update = _get_client_name()
        client_update(client_name,client_name_update)
        read_client_list()  
    elif command == '4':     
        delete_client(_get_client_name())
        read_client_list()
    elif command == '5':
        client_name = _get_client_name()
        found = _client_search(client_name)
              
        if found:
            print('The client: {} is in the list'.format(client_name))
        else:
            print('The client: {} is NOT the list'.format(client_name))
        
        read_client_list()  
    else:
        print('invalid command')    