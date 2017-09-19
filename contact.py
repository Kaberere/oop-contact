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

# name = input("Name: ")
# phone = input("Phone number: ")
# email = input("Email address: ")
# birthday = input("DOB: ")
# linkedIn = input("linkedIn URL: ")

# newContact = Contact(name, phone, email, birthday, linkedIn)
# print(newContact)

class ContactManager:
	def __init__ (self, contacts = []):
		self.contacts = contacts

	def __repr__ (self):
		contact_str = ""
		for contact in self.contacts:
			contact_str += contact + "\n"
			return contact_str
	def add_contact(self, contact):
		self.contacts.append(contact)
		the_manager.displayContacts()

	def remove_contact(self, contact):
		self.contacts.remove(contact)
		for contact in self.contacts:
			if contact.phone == rm_phone:
				self.contacts.remove(contact)
				print("Success")
				the_manager.displayContacts()
			else:
				return "Contact faulty"

	def search_contact(self):
		search_name = input("Name: ")
		print("Contact found for: ")
		for contact in self.contacts:
			if search_name in contact.name:
				return contact
			else:
				return "Contact not found."

	def displayContacts(self):
		for contact in self.contacts:
			print(contact)
			



