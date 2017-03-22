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
		"-f",
		"--file",
		dest="filename",
		help="File name for input arguments"
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
		if options.filename:
			try:
				g = open(options.filename)
			except:
				print "There was an error opening %s"%(options.filename)
			else:
				try:
					input = map(int,g.read().split())
				except:
					#TODO make more descriptive error
					print "Error reading file %s"%(options.filename)
				interpreter = Interpreter(f.read(),options.OUTPUT,*input)
				g.close()
				f.close()
				while interpreter.step():pass
				print interpreter
		else:
			interpreter = Interpreter(f.read(),options.OUTPUT,*map(int,args[1:]))
			f.close()
			while interpreter.step():pass
			print interpreter
