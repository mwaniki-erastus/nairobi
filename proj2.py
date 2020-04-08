#!/usr/bin/env python

def main(args):
	#defining accessing members of a list using their index numbers
	languages=['python','java script','java','bash','php','R','c#','c++']
	print(languages[3])
	last=languages[-1] #-1 is the index for the last value
	print("the last member of the list is " + last.upper())
	
	#defining an empty list whose members will be added dynamically using append
	#append will add at the end of he list by default
	motorcycles=[]
	motorcycles.append('ducati')
	motorcycles.append('honda')
	
	#inserting an element into a particular position in the list
	motorcycles.insert(0,'skygo')
	print(motorcycles)
	motorcycles.insert(2,'suzuki')
	print(motorcycles)
	print(motorcycles[2])
	
	
	#deleting an element when you already know its index
	del motorcycles[2]
	print(motorcycles)
	motorcycles.append('suzuki')
	print(motorcycles)
	
	#using pop() method to remove the last element and still use it
	last_added=motorcycles.pop()
	print("the recently bought motorcycle is " + last_added.upper())
	
	#pop by a peticular position
	second_bought=motorcycles.pop(1)
	print("the recently bought motorcycle is " + second_bought.upper())
	print(motorcycles)
	#using remove() to remove an element by its value
	cheapest=motorcycles.remove('skygo')
	print(motorcycles)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
