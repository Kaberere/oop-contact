class Contact:

	def __init__ (self, name, phone, email, birthday, linkedIn):
		self.name = name
		self.phone = phone
		self.email = email
		self.birthday = birthday
		self.linkedIn = linkedIn

	def __repr__(self):
		return """
		Contact
		name = {}
		phone = {}
		email = {}
		birthday = {}
		linkedIn = {}
		""".format(self.name, self.phone, self.email, self.birthday, self.linkedIn)

name = input("Name: ")
phone = input("Phone number: ")
email = input("Email address: ")
birthday = input("DOB: ")
linkedIn = input("linkedIn URL: ")

# newContact = Contact(name, phone, email, birthday, linkedIn)
# print(newContact)

class ContactManager:
	def __init__ (self, contacts = []):
		self.contacts = contacts

	def add_contact(self, contact):
		self.contacts.append(contact)
		the_manager.displayContacts()

	def remove_contact(self, contact):
		for contact in self.contacts:
			self.contacts.remove(contact)
			print("Success")
			the_manager.displayContacts()
		else:
			return "Contact faulty"

	def search_contact(self, contact):
		for contact in self.contacts:
			self.contacts.search(contact)
			return contact
		else:
			return "Contact not found."

	def displayContacts(self):
		for contact in self.contacts:
			print(contact)

if __name__ == '__main__':
	the_manager = ContactManager()

newContact = ContactManager()
newContact.add_contact(Contact(name = name, phone = phone, email = email, birthday = birthday, linkedIn = linkedIn))
remove = input("Number to be deleted.")
newContact.remove_contact(remove)
search = input("What name would you like to search for?")
print(newContact.search_contact(search))






