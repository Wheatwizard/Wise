import optparse
from Interpreter import Interpreter

if __name__ == "__main__":
	parser = optparse.OptionParser()
	(options, args) = parser.parse_args()
	try:
		f = open(args[0])
	except:
		print "Please provide a valid file."
	else:
		interpreter = Interpreter(open(args[0]).read(),"i",*map(int,args[1:]))
		while interpreter.step():pass
		print interpreter
