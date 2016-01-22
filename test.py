class MyClass:
	att = 5555;

	def hello (self):
		print "Hello"
	def changeAtt (self, numb):
		self.att = numb

inte = MyClass()
inte.hello()
inte.changeAtt(55)
print inte.att
inte.att = 555
print inte.att
print "yolo"
