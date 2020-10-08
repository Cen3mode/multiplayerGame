import os, pygame, socket, foundation
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "fbcon"




class renderQueue():

	def __init__(self):
		self.queue = []

	def addToQueue(self, mesh = foundation.mesh()):
		self.queue.append()

	def removeFromQueue(self, mesh = foundation.mesh()):
		self.queue.remove(mesh)

class renderer():
	
	def __init__(self):
		pass

	def render(self, ):
		pass

