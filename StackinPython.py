''' A stack Class to implement stack data structure in python3 '''

class stack: #Defining a stack class to store our remainder in stck
	def __init__(self):# its a initializer that takes instance  and creates the list named items 
		self.items=[]

	def push(self,item):#method to push any element in the stack
		self.items.append(item)

	def pop(self):#pop item from the stack using inbuilt pop method in python
		return self.items.pop(-1)

	def isempty(self):#checking if stack is empty or not
		if self.items==[]:
			return True
		else:
			return False
	def peek(self):#returns top element of the stack
			if self.items==[]:
				return 'Empty Stack' #returns empty stack if the stack is empty
			else:
				return self.items[len(self.items)-1]	
	def size(self):#returns the number of elements
	      return len(self.items)
