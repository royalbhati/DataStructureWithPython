'''A decimal to binary converter using Stack Data Structure in Python
'''


class stack: #Defining a stack class to store our remainder in stck
	def __init__(self):
		self.items=[]

	def push(self,item):#push item in the stack
		self.items.append(item)

	def pop(self):#pop item from the stack using inbuilt pop method in python
		return self.items.pop(-1)

	def isempty(self):#checking if stack is empty or not
		if self.items==[]:
			return True
		else:
			return False


def dectobinary(number):#function to convert decimal to binary
	rem_stack=stack() #object of class stack
	binary_str='' #string variable
	while number>0: #while loop to perform logic 
		rem=number%2
		rem_stack.push(rem)
		number=number//2

	while not rem_stack.isempty():# removing elemts from stack and appending it in a string
			binary_str=binary_str+str(rem_stack.pop())
	return binary_str
	
  if __name__='__main__':
  
      print(dectobinary(33))


