#Caterina Ponti
#Project 3 
#CS110 


#Create the Bird Class
class Bird:
	def __init__(self, name, birthdate, breed, color):
		#Creating the following data attributes: name, birthdate, breed and color 
		self.__name = name
		self.__birthdate = birthdate
		self._breed = breed
		self.__color = color

	def set_name(self, name): #Setter method for name attribute 
		self.__name = name

	def get_name(self): #Getter method for name attribute
		return self.__name

	def set_birthdate(self, birthdate):
		self.__birthdate = birthdate 

	def get_birthdate(self):
		return self.__birthdate

	def set_breed(self, breed):
		self.__breed = breed

	def get_breed(self):
		return self.__breed

	def set_color(self, color):
		self.__color = color

	def get_color(self):
		return self.__color

	#The string method 
	def __str__(self):
		return f"Name: {self.__name}\n Type: {self.__birthdate}\n Breed: {self.__breed}\n Color: {self.__color}."
