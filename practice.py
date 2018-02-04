class students:
	def __init__(self, name, contact):
		self.name = name
		self.contact = contact
		
	def getdata(self):
		self.name = input("enter the name ")
		self.contact = input("enter the contact ")
		
	def putdata(self):
		print(self.name+"  "+ self.contact)


john = students("blank",4)
john.getdata()
john.putdata()
