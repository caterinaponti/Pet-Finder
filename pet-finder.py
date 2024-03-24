#Caterina Ponti
#Project 3 Part 1 and 2  
#CS110

#import the Dog, Cat, Fish and Bird Class 
from dog import Dog  
from cat import Cat
from fish import Fish
from bird import Bird

import csv

filename = open("pets.csv", "r") #open the csv file

pets = [] #Create an empty pets list to store the objects
rows = []

csvreader = csv.reader(filename)

for row in csvreader: #Iterate through the rows of the csv file
	rows.append(row) #To count number of rows

	pet_type = row[0] #Set the first element of teh row as pet_type 
	name = row[1]
	birthdate = row[2]
	breed = row[3]
	color = row[4]

	#Check the pet type and create the corrsponding object
	if pet_type == "Dog":
		dog = Dog(name, birthdate, breed, color)
		dog.set_name(name) #set attributes for the created dog object
		dog.set_birthdate(birthdate)
		dog.set_breed(breed)
		dog.set_color(color)
		pets.append(dog) #Add the created dog object to the pets list
			
	elif pet_type == "Cat":
		cat = Cat(name, birthdate, breed, color)
		cat.set_name(name) #set attributes for the created cat object
		cat.set_birthdate(birthdate)
		cat.set_breed(breed)
		cat.set_color(color)
		pets.append(cat) #Add the created cat object to the pets list

	elif pet_type == "Fish":
		fish = Fish(name, birthdate, breed, color)
		fish.set_name(name) #set attributes for the created fish object
		fish.set_birthdate(birthdate)
		fish.set_breed(breed)
		fish.set_color(color)
		pets.append(fish) #Add the created fish object to the pets list
			
	elif pet_type == "Bird":
		bird = Bird(name, birthdate, breed, color)
		bird.set_name(name) #set attributes for the created bird object
		bird.set_birthdate(birthdate)
		bird.set_breed(breed)
		bird.set_color(color)
		pets.append(bird) #Add the created bird object to the pets list

	print(f'{name}, {birthdate}, {breed}, {color}') #print every object as a comma separated list 

#Check the lenght of the list of pets
if len(pets) == len(rows):
    print("Object creation successful.")
else:
    print("Object creation failed.")



def binarySearch(sorted_names, target):
	#Setting the low and high values 
	low = 0
	high = len(sorted_names) - 1

	while low <= high:
		mid = (low + high) // 2 #Find the middle
		mid_name = sorted_names[mid][1].strip()

		print(f"Debug: mid_name = {mid_name}, target = {target}")

		if mid_name == target: #If mid_name is equal as target return the index 
			return mid #Pet found return the index
		elif mid_name < target: #If the mid_name is smaller than the index target, the mid is the new low 
			low = mid + 1
		else: #If the mid_name is greater than the index target, the mid is the new high 
			high = mid - 1 

	return -1

def merge_sort(pets_list):
	# Creating a copy of the list to avoid modifying the original list
	pets_list_copy = pets_list.copy()

	if len(pets_list_copy) > 1: 
		mid = len(pets_list_copy) //2
		#Splitting the list of elements in half continuosly until there are undividual items 
		left_half = pets_list_copy[:mid] 
		right_half = pets_list_copy[mid:]

		#Recursion: the merge_sort function will call itself continuosly until there are individual items. 
		left_half = merge_sort(left_half) 
		right_half = merge_sort(right_half)

		#two iterators for trasversing the two halves 
		i = 0 
		j = 0 

		#Iterator for the main list
		k = 0 

		#Now begins the sorting process
		while i < len(left_half) and j < len(right_half):
			if left_half[i][1] < right_half[j][1]: 
				pets_list_copy[k] = left_half[i] #If the value i is smaller than the value j, left[i] is assigned to the pets_list[k]
				#Move foward, i is incremented 
				i += 1 
			else:	
				pets_list_copy[k] = right_half[j] #If element in the left is greater than the one in the right
				j += 1
			#Move to the next slot 
			k += 1


		#For all the remaining values
		while i < len(left_half):
			pets_list_copy[k] = left_half[i]
			i += 1
			k += 1
		
		while j < len(right_half):
			pets_list_copy[k] = right_half[j]
			j += 1
			k += 1

	return pets_list_copy


pet_data = list(csv.reader(open("pets.csv", "r")))

print(pet_data)

#Creating the Menu.
while True: 
	print()
	print("Menu:")
	print("1 - Print the names of the pets.\n"
	"2 - Show only pets of a certain type.\n"
	"3 - Search for a Pet.\n"
	"4 - Sort list based on pet name.\n")
	"5 - Exit the program.\n"

	filename = open("pets.csv", "r") #Opening the file 
	csvreader = csv.reader(filename) #Reading the file

	choice = int(input("Enter your choice (1/2/3/4/5): ")) #Asking the user for input choice 

	if choice == 1:
		print("Pets names: ") #Printing all pets' names
		for row in csvreader: #Iterating through the pets list
			name = row[1].strip() 
			print(name) #Printing the names 

	elif choice == 2:
		print("What kind of pet would you like to see?")
		pet_choice = int(input("Enter 1- Dogs, 2- Cats, 3- Fishes, 4- Birds: ")) #Asking the user for input 

		if pet_choice in range(1, 5):
			if pet_choice == 1: 
				print("Dogs: ")
				for row in csvreader:
					if row[0] == "Dog": #Search for all the Dog in the rows 
						print(f"{row[1]}, {row[2]}, {row[3]}, {row[4]}") #Print all the dogs 

			elif pet_choice == 2:
				print("Cats: ")
				for row in csvreader:
					if row[0] == "Cat": #Search for all the Cat in the rows
						print(f"{row[1]}, {row[2]}, {row[3]}, {row[4]}") #Print all the cats 
            	
			elif pet_choice == 3:
				print("Fishes: ")
				for row in csvreader:
					if row[0] == "Fish": #Search for all the Fish in the rows
						print(f"{row[1]}, {row[2]}, {row[3]}, {row[4]}") #Print all the fishes 
            	
			elif pet_choice == 4:
				print("Birds: ")
				for row in csvreader:
					if row[0] == "Bird": #Search for all the Bird in the rows
						print(f"{row[1]}, {row[2]}, {row[3]}, {row[4]}") #Print all the birds  
            	
          
		else:
			print("Error! Invalid choice.") #Input validation 
			pet_choice = int(input("Enter 1- Dog, 2- Cat, 3- Fish, 4- Bird: "))


	elif choice == 3:
		print("Search for a Pet:")
		search_name = input("Enter the name of the pet: ").strip() #Asking the user to enter an input name 
		for row in rows: 
			row[1] = row[1].strip()

		sorted_pets = merge_sort(rows) #Sorting the list elements as pre-condition for binary search
		index = binarySearch(sorted_pets, search_name) #Calling the binary search function 
		#Storing the returning value in a variable called index

		if index != -1:
		#Printing the pet's information  
			print() 
			print(f"Pet found at index {index}: {sorted_pets[index][1]}, {sorted_pets[index][2]}, {sorted_pets[index][3]}, {sorted_pets[index][4]}")
		else: #If index = -1, the pet is not in the list 
			#Pet not found
			print(f"Pet '{search_name}' not found in the list.")


	elif choice == 4:
		print("Sorted List based on pet names: ")
		for row in rows: 
			row[1] = row[1].strip() #Stripping white spaces

		sorted_pets = merge_sort(rows) #Call the merge_sort function 

		for pet in sorted_pets: #Print the new sorted list 
			print(f'{pet[1]}, {pet[2]}, {pet[3]}, {pet[4]}.') 

	elif choice == 5: 
		break #Exit 

	else: #Input validation 
		print()
		print("Error! Invalid choice.")


#Closing the csv file 
filename.close()





