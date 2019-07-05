import sys, getopt

# print("Hallo " + str(sys.argv[1]) + str(sys.argv[2]))

def hello(text):
	print("Hallo {}".format(text))	

def goodbye(text):
	print("Tschüss {}".format(text))	

if sys.argv[2] == "goodbye":
	goodbye(sys.argv[1])
else: 
	hello(sys.argv[1])