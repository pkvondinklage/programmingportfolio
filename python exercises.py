#Python learning exercises

# functions
def echo(thing):
	return thing
	
def swap(n1, n2):
	return n2, n1
	
def main_function():
	print"testing echo('marco'): ", echo('marco')
	print"testing swap('1, 2'):",swap('1, 2')
	
	
#Arithmetic functions
def reverse(x):
	return -x
	

	
def main_arithmetic():
	print "test reverse(3): ",reverse(3)
	print "test reverse(-3): ",reverse(-3)
	
	
def main():
	main_function()
	main_arithmetic()
	
	
main()