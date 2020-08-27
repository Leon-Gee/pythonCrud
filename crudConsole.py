import sys
import csv
import os

CLIENT_TABLE= '.clients.csv'
CLIENT_SCHEMA =['name','company','email','position']
clients=[]


def __initializeClientsFromDisk():
    with open(CLIENT_TABLE,mode='r') as f:
        reader = csv.DictReader(f,fieldnames=[])

        for row in reader:
            clients.append(row)


def __saveClientsToDisk():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name,mode='w') as f:
        writer = csv.DictWriter(f,fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name,CLIENT_TABLE)



def client_create(client):
    global clients

    if client not in clients:
        clients.append(client)
        return True
    else:
        print("Client is already in the list")
        return False




def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the {}?'.format(field_name))
    
    return field


def  delete_client(client_name):
    global clients
    for idx,client in enumerate(clients):
        if client['name'] == client_name:
            clients.pop(idx)
            print('The client: {} has been erased >:)'.format(client_name))
            break  


def client_update(client_name,client_updated):
    global clients

    for idx,client in enumerate(clients):
        if client['name'] == client_name:
            clients[idx] = client_updated
            print('The update was succesful')
            read_client_list()  
            break
    


def _client_search(client_name):
    global clients

    for idx,client in enumerate(clients):
        if client['name'] != client_name:
            continue
        else:
            return True 

def read_client_list():
    global clients
    for idx,client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))

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
    __initializeClientsFromDisk()
    __print_welcome()
    f = True

    command = input()   
    if command == '1':

        client={
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email':_get_client_field('email'),
            'position': _get_client_field('position')
        }

        if client_create(client):
            print('The client has been added succesfully')
            read_client_list()

    elif command == '2':

        read_client_list() 

    elif command == '3':

        client_name = _get_client_name()
        client_updated={
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email':_get_client_field('email'),
            'position': _get_client_field('position')
        }
        client_update(client_name, client_updated)
        

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
    
    __saveClientsToDisk()

 