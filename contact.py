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
	def remove_contact(self, contact):
		self.contacts.append(contact)
	def search_contact(self, contact):
		for contact in self.contacts:
			if contact.name == name:
				self.contacts.search(contact)
				return contact
			return None

if __name__ == "__main__":
	new_contacts = ContactManager()
	new_contacts = Contact(name="Eve")
	new_contacts.add_contact(new_contacts)
	new_contacts.search_contact(Contact(name = "Eve"))
	new_contacts.remove_contact("")

print(new_contacts)



