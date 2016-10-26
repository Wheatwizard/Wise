class Interpreter(object):
	def __init__(self,source,output,*args):
		self.stack = list(args)
		self.source = source
		self.scope = []
		self.pointer = 0
		self.output = output
	def peak(self):
		return not(self.stack) or self.stack[-1]
	def pick(self):
		if self.stack:
			return self.stack.pop()
		else: return 0
	def step(self):
		if self.pointer >= len(self.source):return False
		command = self.source[self.pointer]
		if command == "[":
			if not self.peak:
				tempScope = 1
				while not tempScope and self.pointer <= len(self.source):
					self.pointer += 1
					if self.source[self.pointer] == "]":
						self.tempScope -= 1
					elif self.source[self.pointer] == "[":
						self.tempScope += 1
			else:
				self.scope.append(self.pointer)
		elif command == "]":
			if self.peak():
				self.pointer = self.scope[-1]
			else:
				self.scope.pop()
		elif command == "&":
			self.stack.append(self.pick()&self.pick())
		elif command == "|":
			self.stack.append(self.pick()|self.pick())
		elif command == "^":
			self.stack.append(self.pick()^self.pick())
		elif command == "~":
			self.stack.append(~self.pick())
		elif command == "-":
			self.stack.append(-self.pick())
		elif command == "<":
			self.stack.append(self.pick()<<1)
		elif command == ">":
			self.stack.append(self.pick()>>1)
		elif command == ":":
			if self.stack:
				self.stack.append(self.stack[-1])
			else:
				self.stack = [0]
		elif command == "?":
			if self.stack:
				self.stack = [self.stack.pop()] + self.stack
		elif command == "!":
			if self.stack:
				self.stack = self.stack[1:] + [self.stack[0]]
		self.pointer += 1
		return True
	def __str__(self):
		functions = {"i":str,"b":lambda x:"-"+bin(x)[3:] if x < 0 else bin(x)[2:],"a":lambda x:chr(x%256)}
		return ("" if self.output == "a" else" ").join(map(functions[self.output],self.stack))
