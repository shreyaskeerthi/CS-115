#I pledge my honor that I have abided by the stevens honor system
#Shreyas Keerthi


'''converts decimal to binary'''
def decimalToBinary(x):
	if x==0:
		return []
	else:
		return [x%2]+decimalToBinary(x//2)


'''converts R2L binary to decimal'''
def binaryToDecimal(num):
	if(num==[0] or num==[]):
		return 0
	if (num[-1]==0):
		return 0+binaryToDecimal(num[:-1])
	else:
		return (2**(len(num)-1))+binaryToDecimal(num[:-1])


'''increments binary value by one'''
def incrementBinary(num):
	return (decimalToBinary(binaryToDecimal(num)+1))


'''adds binary digits'''
def binaryAddition(num1,num2):
	if len(num1)>len(num2):
		zeroes = len(num1)-len(num2)
		num2=num2+[0]*zeroes
	
	if len(num2)>len(num1):
		zeroes=len(num2)-len(num1)
		num1=num1+[0]*zeroes
	return helper(num1,num2,0)

'''helper function for binary addition, a rep num1, b rep num2, c is carried num '''
def helper(a,b,c):
	if (a==[] and b==[]):
		if c==1:
			return [c]
		else:
			return []
	zero=c+a[0]+b[0]
	if zero>1:
		c=1
		return[zero%2]+helper(a[1:],b[1:],c)
	else:
		c=0
		return[zero]+helper(a[1:],b[1:],c)
	return helper()

