from Stack import Stack

class Interpreter(object):
	def __init__(self,source,output,*args):
		self.stack = Stack(args)
		self.source = source
		self.scope = []
		self.pointer = 0
		self.output = output
	def step(self):
		if self.pointer >= len(self.source):return False
		command = self.source[self.pointer]
		if command == "[":
			if self.stack[-1]:
				self.scope.append(self.pointer)
			else:
				#If the TOS is zero jump to the next ]
				tempScope = 1
				while tempScope and (self.pointer < len(self.source)):
					self.pointer += 1
					if self.source[self.pointer] == "]":
						tempScope -= 1
					elif self.source[self.pointer] == "[":
						tempScope += 1
		elif command == "]":
			if self.stack[-1]:
				self.pointer = self.scope[-1]
			else:
				self.scope.pop()
		elif command == "&":
			self.stack.append(self.stack.pop()&self.stack.pop())
		elif command == "|":
			self.stack.append(self.stack.pop()|self.stack.pop())
		elif command == "^":
			self.stack.append(self.stack.pop()^self.stack.pop())
		elif command == "~":
			self.stack.append(~self.stack.pop())
		elif command == "-":
			self.stack.append(-self.stack.pop())
		elif command == "<":
			self.stack.append(self.stack.pop()<<1)
		elif command == ">":
			self.stack.append(self.stack.pop()>>1)
		elif command == ":":
			if self.stack:
				self.stack.append(self.stack[-1])
			else:
				self.stack = [0]
		elif command == "?":
			if self.stack:
				self.stack = Stack([self.stack.pop()] + self.stack)
		elif command == "!":
			if self.stack:
				self.stack = Stack(self.stack[1:] + [self.stack[0]])
		self.pointer += 1
		return True

	def __str__(self):
		functions = {"i":str,"b":lambda x:"-"+bin(x)[3:] if x<0 else bin(x)[2:],"a":lambda x:chr(x%256)}
		return (""if self.output=="a" else" ").join(map(functions[self.output],self.stack))
