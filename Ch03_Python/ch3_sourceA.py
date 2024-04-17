################ p.102 #####################
f = open("test.txt")
data = f.readline()
print(data)
"""
while line:
	print(line)
	line = f.readline() 
"""  # Error 
f.close()

f1=open("out.txt","w")
f1.write("This file is %s" % ("out.txt"))
f1.close()



with open("out1.txt","w") as f2:
	f2.write("This file is %s" % ("out1.txt"))

f3 = open("out2.txt", "w")
print("This files is %s" % ("out2.txt"), file=f3)

################ p.103 #####################
import sys
sys.stdout.write("Enter your name: ")
#name = sys.stdin.readline()
name = input()
print("Your name is %s" % name) 

################ p.103a #####################
#importing pickle module
import pickle

#declaring a numbers list
o = [1,2,3,4,5,6,'Lee']

#pickling the list and storing in a file
f = open('test.pickle','wb')
pickle.dump(o,f)
f.close()
print("The list pickle is created successfully.")

#################### 
f = open("test.pickle","rb")
o = pickle.load(f)
print(o)
f.close()

################ p.104 #####################
x = input('Enter numenator : ')
y = input('Enter denomenator : ')

try:
	a = int(x)
	b = int(y)
	c = a/b
	print("Answer: %f" % c)
except ValueError as e:
    	print("%s. %s" % (e, 'Check if input string is parsable integer'))
except ZeroDivisionError:
    	print('Denomenator is zero.')
 
################ p.105 #####################
with open("test1.txt","a") as f:
	f.write("write string")
	f.write("end\n")






