clients= 'leon,sofia,'

def client_create(client_name):
    global clients
    if client_name not in clients:
        clients+= client_name
        __add_comma()
        return True
    else:
        print("Client is already in the list")
        return False

def  delete_client(client_name):
    global clients
    if client_name in clients:
         clients = clients.replace(client_name + ',', '')

def _get_client_name():
    return input('What its the client name?')

def client_update(client_name,updated_client_name):
    global clients

    #if updated_client_name not in clients:
    if client_name in clients:
        clients = clients.replace(client_name, updated_client_name)
    else:
        print('The client that you are trying to update doesnt exist')
    #else:
      #      print('The client that you are trying to update already exist')

def __add_comma():
    global clients
    clients +=','


def read_client_list():
    global clients
    print(clients)


def __print_welcome():

    print('Welcome to leon ventas')
    print('*' * 50)
    print('What would you like to do today? ')
    print('1. Create client')
    print('2. Read the list')
    print('3. Update Client')
    print('4. Delete client ')

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
    else:
        print('invalid command')