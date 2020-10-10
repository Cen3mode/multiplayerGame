import os, pygame, socket, foundation
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "fbcon"


class renderQueue:
    def __init__(self):
        self.queue = []
        self.queuePointer = 0

    def addToQueue(self, mesh=foundation.mesh()):
        self.queue.append(mesh)

    def removeFromQueue(self, mesh=foundation.mesh()):
        self.queue.remove(mesh)

    def queueLen(self):
        return len(self.queue)

    def getFromQueue(self):
        if self.queuePointer >= len(self.queue):
            self.queuePointer = 0
        self.queuePointer += 1
        return self.queue[self.queuePointer - 1]


class renderer:
    def __init__(self, queue=renderQueue(), resolution=(800, 600)):
        self.queue = queue
        self.resolution = resolution
        pygame.init()
        pygame.display.set_mode(self.resolution, DOUBLEBUF | OPENGL)

        gluPerspective(45, (self.resolution[0] / self.resolution[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for _ in range(self.queue.queueLen()):
            mesh = self.queue.getFromQueue().getMesh()
            glBegin(GL_LINES)
            for edge in mesh[1]:
                for vertex in edge:
                    glVertex3fv(mesh[0][vertex])
            glEnd()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()

    def camera(self, pos = (0,0,0), rotation = (0,0,0), fov = 45):
    	glTranslatef(pos[0], pos[1], pos[2])
    	glRotatef(rotation[0],1,0,0)
    	glRotatef(rotation[1],0,1,0)
    	glRotatef(rotation[2],0,0,1)
    	gluPerspective(fov, (self.resolution[0] / self.resolution[1]), 0.1, 50.0)
