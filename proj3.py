def main(args):
	cars=['audi','toyota','kompressor','tesla','jeep','jaguar','maserati','porche','honda','bmw']
	print(cars)
	
	#sort function sorts members permanently and stores them in the variable
	cars.sort()
	print(cars)
	#members can also be sorted in a reverse order
	cars.sort(reverse=True)
	print(cars)
	
	#to sort temporarily use sorted
	'''/
	cars=['maserati','toyota','kompressor','tesla','jeep','jaguar','audi','porche','honda','bmw']
	print(cars)
	cars.stot()
	print(cars)
	'''
	#use the reverse() to reverse the chronological order of elements in a list(not really alphabetically
	cars=['maserati','toyota','kompressor','tesla','jeep','jaguar','audi','porche','honda','bmw']
	cars.reverse()
	print(cars)
	
	#use len() function to find the number of elements in a list
	length=len(cars)
	print('the number of cars is ' + str(length))
	
	#TO LOOP THROUGH A LIST
	#you can choose any name for the temporary variable erastus
	for erastus in cars:
		print(erastus)
	
	#generating a list using the range(start,end,increment) function
	#the end value will not be printed
	for i in range(0,21,3):
		print(i)
		
	#making the output of the range() function using the list() function
	even_numbers = list(range(0,51,2))
	print("even numbers between 0 and 50 are: " + str(even_numbers))
	squares = []
	for value in range(0,51,2):
		values = value**2
		squares.append(values)
	print("the squares of these even numbers are" + str(squares))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
