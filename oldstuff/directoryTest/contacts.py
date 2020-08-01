class Contact:
	def __init__(self, name, phone, email):
		self._name = name
		self._phone = phone
		self._email = email

class ContactBook:

	def __init__(self):
		self._contacts = []

	def add(self, name, phone, email):
		contact = Contact(name,phone,email)
		self._contacts.append(contact)

	def show_all(self):
		for contact in self._contacts:
			self._print_contact(contact)
	
	def _print_contact(self,contact):
		print('---------------------------')
		print('Name: {}'.format(contact._name))
		print('Phone: {}'.format(contact._phone))
		print('Email: {}'.format(contact._email))
		print('---------------------------')

	def delete(self,name):
		for idx, contact in enumerate(self._contacts):
			if contact._name.lower() == name.lower():
				del self._contacts[idx]
				break
	
	def search(self,name):
		for contact in self._contacts:
			if contact._name.lower() == name.lower():
				self._print_contact(contact)
				break
		else:
			self.not_found()

	def not_found(self):
		print('Contact not found')

	def update(self, name):
		for contact in self._contacts:
			if contact._name.lower() == name.lower():
				while True:
                	self._print_contact(contact)
                    option = str(input('''
                    ¿Qué deseas hacer?

                    [n] Cambiar Nombre
                    [p] Cambiar Telefono
                    [e] Cambiar Email
                    [s] Salir

                    '''))

                    if option == 'n':
                        new_name = str(input('Escribe el nuevo nombre: '))
                        contact._name = new_name
                    elif option == 'p':

                        new_phone = str(input('Escribe el nuevo telefono: '))
                        contact._phone = new_phone
                    elif option == 'e':

                        new_email = str(input('Escribe el nuevo email: '))
                        contact._email = new_email
                    elif option == 's':
                        break
                    else:
                        print('Comando no reconocido')
            else:
                self._not_found()
	
def run():

	contact_book = ContactBook()

	while True:
		command = str(input('''
			Welcome, please, type an option to work on your contacts
			A) Add a contact
			B) Edit contact
			C) Search a contact
			D) Erase a contact
			E) List contacts
			F) Exit

		''')).upper()

		if command == 'A':
			name = str(input('Write the name of the contact:'))
			phone = str(input('Write the phone of the contact:'))
			email = str(input('Write the mail of the contact:'))

			contact_book.add(name, phone, email)

		elif command == 'B':
			print('g')
		elif command == 'C':

				name = str(input('Write the name of the contact that you wish to find: '))
				contact_book.search(name)

		elif command == 'D':

			name = str(input('Write the name of the contact that you wish to erase: '))
			contact_book.delete(name)

		elif command == 'E':
			
			contact_book.show_all()

		elif command == 'F':
			break
		else:
			print('That command does not exist, please, type a valid command')
			

if __name__ == '__main__':
	print('WELCOME BACK MY VALEDOR')
	run()