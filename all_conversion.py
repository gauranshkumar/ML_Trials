

 #Takes Input From the user
#Declearing The Variable that hold remainder
rem = int()
rem1 = int()
def binary(decinum):  #Function For Binary conversion
	
	if decinum <=1: # If Statement For conversion
		print(decinum, end = "")
		return #returning the value of decinum to he compiler
	rem = decinum%2 # taking remainder from decinum
	binary(decinum//2)# giving value to the binary function as decinum/2
	print(rem, end="") #printing the binary output.
	
	
def octal(decinum):
	if decinum <=1:
		print(decinum, end = "")
		return
	rem1 = decinum%8
	octal(decinum//8)
	print(rem1, end="")
	

def hexadecimal(decinum):
	if decinum <=1:
		print(decinum, end = "")
		return
	rem2 = decinum%16
	hexadecimal(decinum//16)
	
	if rem2==10 :
		print("A", end="")
	elif rem2==11 :
		print("B", end="")
	elif rem2==12 :
		print("C", end="")
	elif rem2==13 :
		print("D", end="")
	elif rem2==14 :
		print("E", end="")
	elif rem2==15 :
		print("F", end="")
	else :
		print(rem2, end="")


def all():
	print("-----------------------xxx------------------------")
	
	print("\n              Number System Converter       \n")
	
	print("-----------------------xxx------------------------")

	
	
	while True:
		decinum = int(input("\n\nPlease Enter A Positive Integer : "))
		if decinum<0:
			print("\n\nSorry entered number is not a positive integer.")
			pass
			
		else :
			break
	
	print("\n\nPlease Choose A Function To Perform.\n")
	print("1) Binary Number")
	print("2) Octal Number")
	print("3) Hexadecimal Number")
	print("4) All Conversions")
	fun = int(input())
	if fun==1 :
		print("Binary Form : ",end="")
		binary(decinum)
		print("\n")
	elif fun==2:
		print("Octal Form : ",end="")
		octal(decinum)
		print("\n")
	elif fun==3:
		print("Hexadecimal Number : ",end="")
		hexadecimal(decinum)
		print("\n")
	elif fun==4:
		print("All Conversions are : \n")
		print("Binary Number : ", end="")
		binary(decinum)
		print("")
		print("Octal Number : ", end="")
		octal(decinum)
		print("")
		print("Hexadecimal Number : ", end="")
		hexadecimal(decinum)
		print("\n\n")
		
all()
while True:
	fu = str(input("Do You Want To Convert It Again ?\n"))
	if fu =="yes" :
		all()
		pass
		
	elif fu =="Yes" :
		all()
		pass
		
	elif fu =="YES" :
		all()
		pass
		
	elif fu =="Yeah" :
		all()
		pass
		
	elif fu =="yeah" :
		all()
		pass
		
	elif fu =="YEAH" :
		all()
		pass
		
	elif fu =="y":
		all()
		pass
	else :
		print(" Thank You For Using Our Service !! \n\n")
		print(" Hope It Helped :) \n\n")
		break



