#!/usr/bin/env python3

instructions = [x.strip() for x in open("data.txt").readlines()]

class CPU:
	def __init__(self):
		self.clock = 0
		self.X = 1
		self.signal_beats = []
		self.display = []
	
	def log(self):
		if (self.clock+20) % 40 == 0:
			print(self.clock, self.X, self.signal_strength())
			self.signal_beats.append(self.signal_strength())
	
	def setPixel(self):
		if abs(self.clock%40 - self.X) <= 1:
			self.display.append('#')
		else:
			self.display.append('.')
	
	def drawDisplay(self):
		for i in range(self.clock):
			if i % 40 == 0:
				print()
			print(self.display[i], end="")
	
	def step(self):
		self.setPixel()
		self.clock += 1
		self.log()
		
	def noop(self):
		self.step()
	
	def addx(self, val):
		self.step()
		self.step()
		self.X += val
		
	def signal_strength(self):
		return self.clock * self.X

cpu = CPU()

signalSum = 0
for i in instructions:
	#print(">", i)
	if i == "noop":
		cpu.noop()
	elif i.startswith("addx"):
		val = int(i.split(" ")[1])
		cpu.addx(val)
		#print(">>", cpu.clock, cpu.X)

print("Signal sum:", sum(cpu.signal_beats))

cpu.drawDisplay()