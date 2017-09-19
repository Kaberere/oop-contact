import csv
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

#getting contact input from users
name = input("Name: ")
phone = input("Phone number: ")
email = input("Email address: ")
birthday = input("DOB: ")
linkedIn = input("linkedIn URL: ")

class ContactManager:
	def __init__ (self, contacts = []):
		self.contacts = contacts

#add contacts
	def add_contact(self, contact):
		self.contacts.append(contact)#append adds content
		the_manager.display_contacts()

#remove contacts
	def remove_contact(self, phone):
		for contact in self.contacts:
			if contact.phone == phone:
				self.contacts.remove(contact)
				return "Success"
				the_manager.display_contacts()
		else:
			return "Contact doesn't exist"

#search contacts
	def search_contact(self, name):
		for contact in self.contacts:
			if contact.name == name:
				return contact
		else:
			return "Contact not found."

	def display_contacts(self):
		for contact in self.contacts:
			print(contact)

if __name__ == '__main__':
	the_manager = ContactManager()

#call
newContact = ContactManager()
newContact.add_contact(Contact(name = name, phone = phone, email = email, birthday = birthday, linkedIn = linkedIn))
remove = int(input("Number to be deleted."))
print(newContact.remove_contact(remove))
search = input("What name would you like to search for?")
print(newContact.search_contact(search))





