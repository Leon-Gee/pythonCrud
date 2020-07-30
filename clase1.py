clients= 'leon,sofia,'

def create_client(client_name):
    global clients
    if check_client(client_name):
        clients+= client_name
        __add_comma()
        return True
    else:
        print("ERROR")
        return False


def check_client(client_name):
    global clients
    return ~(client_name in clients)


def __add_comma():
    global clients
    clients +=','

def list_clients():
    global clients
    print(clients)

def __print_welcome():
    print('Welcome to leon ventas')
    print('*' * 50)
    print('What would you like to do today? ')
    print('1. Create client')
    print('2. Delete Client')
    print('3. Print all the clients')
if __name__== '__main__':
    __print_welcome()

    command = input()

    if command == '1':
        client_name = input('What its the client name? ')
        if create_client(client_name):
            print('The client has been added succesfully')
            list_clients()
    elif command == '2':
        pass
    elif command == '3':
         list_clients()
    else:
        print('invalid command')