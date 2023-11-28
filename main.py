# Ethan Eichelberger

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# pygame.init()
# display = (800, 600)
# pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
# glPerspective(45, (display[0] / display[1]), 0.1, 50.0)
# glTranslatef(0.0, 0.0, -5)
#

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)


# function to draw house, should take in parameters for postion to draw multiple houses, and assign colors
def draw_house():
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(0, 2, -1)
    glEnd()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_house()
    pygame.display.flip()
    pygame.time.wait(10)
