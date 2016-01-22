import cherrypy
import string
import random

class StringGenerator(object):
	@cherrypy.expose
	def index(self):
		return "<h1>Hello World!</h1> <h2>Welcome</h2>"
	@cherrypy.expose
	def generate(self, n):
		return ''.join(random.sample(string.hexdigits, int(n)))

if __name__ == "__main__":
	cherrypy.quickstart(StringGenerator())
