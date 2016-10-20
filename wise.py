import optparse
from Interpreter import Interpreter

if __name__ == "__main__":
	parser = optparse.OptionParser()
	parser.add_option(
		"-b",
		"--binary",
		dest="OUTPUT",
		action="store_const",
		const="b",
		default="i",
		help="Formats output as binary"
	)
	parser.add_option(
		"-a",
		"--ascii",
		dest="OUTPUT",
		action="store_const",
		const="a",
		help="Formats output as ASCII",
	)
	(options, args) = parser.parse_args()
	try:
		f = open(args[0])
	except:
		print "Please provide a valid file."
	else:
		interpreter = Interpreter(open(args[0]).read(),options.OUTPUT,*map(int,args[1:]))
		while interpreter.step():pass
		print interpreter
