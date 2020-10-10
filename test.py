from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0
res = (500, 400)

def draw():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(res[0], res[1])
glutInitWindowPosition(0,0)
window = glutCreateWindow("multiplayerGameOpenGLTest")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()