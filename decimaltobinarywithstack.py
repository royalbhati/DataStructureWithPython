class stack:
	def __init__(self):
		self.items=[]

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop(-1)

	def isempty(self):
		if self.items==[]:
			return True
		else:
			return False


def dectobinary(number):
	rem_stack=stack()
	binary_str=''
	while number>0:
		rem=number%2
		rem_stack.push(rem)
		number=number//2

	while not rem_stack.isempty():
			binary_str=binary_str+str(rem_stack.pop())
	return binary_str
	
  if __name__='__main__':
  
      print(dectobinary(33))


