# Ethan Eichelberger
import pygame.image

# Requirements
# ground plane with appropriate ground texture, NOT A SINGLE FLAT COLOR, grass dirt etc
# visible street
# some form of backgrounds (mountains, forest in the distance, cityscape, etc.)
#
# One structure should be different than a house, like, for example,  a barn with a rounded
# roof or a dome (like an observatory), or a tower with with conical roof.
#
#
# When night falls in the scene at least some
# of the habitable structures must have interior lighting and this must be visible in the application. And the user must
# be able to return the scene to daylight conditions
#
# The scene must include at least one animated character object.  One of the characters must be a human-like character.
# Other characters can be human or non-human character. More that one animated character is optional.
#
# he human-like character must initially, face a direction other than toward the camera, and, at some point,
# turn toward the viewer (camera) and wave.
#
# The nonhuman character or object may be animated also, performing some actions (walking, running, eating grass,
# chasing a ball, digging a hole, driving down the street, etc.)


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import image

camerax = -1.0
cameraz = 5
lookx = 0.0
lookz = 0
doorangle = 0
sunstate = 1


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)
    glEnable(GL_COLOR_MATERIAL)
    init_light()


def init_light():

    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1])
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 2, 0, 1])
    glEnable(GL_LIGHT0)


def draw_house(roof, wall, control):

    draw_backwall2(wall)
    draw_frontwall(wall)
    draw_sidewall1(wall)
    draw_sidewall2(wall)
    draw_roofside1(roof)
    draw_roofside2(roof)
    draw_roofend1(roof)
    draw_roofend2(roof)
    if control:
        draw_controlled_door()
    else:
        draw_door()


def draw_backwall(color):
    glPushMatrix()
    glColor3fv(color)
    glRotatef(180, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, -0.1)
    draw_frontwall()
    glPopMatrix()


def draw_frontwall(color):
    glPushMatrix()
    glColor3fv(color)
    glBegin(GL_QUADS)

    glVertex3f(-1, 0 , 0)
    glVertex3f(-1, 0.4, 0)
    glVertex3f(-0.2, 0.4, 0)
    glVertex3f(-0.2, 0, 0)

    glVertex3f(-1, .4, 0)
    glVertex3f(-1, 1, 0)
    glVertex3f(-.4, 1, 0)
    glVertex3f(-.4, .4, 0)

    glVertex3f(-.4, .6, 0)
    glVertex3f(-.4, 1, 0)
    glVertex3f(-.2, 1, 0)
    glVertex3f(-.2, .6, 0)

    glVertex3f(-.2, .4, 0)
    glVertex3f(0, .4, 0)
    glVertex3f(0, 1, 0)
    glVertex3f(-.2, 1, 0)

    glVertex3f(0, 1, 0)
    glVertex3f(1, 1, 0)
    glVertex3f(1, .4, 0)
    glVertex3f(0, .4, 0)

    glVertex3f(0, 0, 0)
    glVertex3f(.2, 0, 0)
    glVertex3f(.2, .4, 0)
    glVertex3f(0, .4, 0)

    glVertex3f(.2, 0, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(1, .2, 0)
    glVertex3f(.2, .2, 0)

    glVertex3f(.4, .4, 0)
    glVertex3f(1, .4, 0)
    glVertex3f(1, .2, 0)
    glVertex3f(.4, .2, 0)

    glEnd()
    glPopMatrix()


def draw_backwall2(color):

    glPushMatrix()
    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glEnd()
    glPopMatrix()


def draw_sidewall1(color):
    glPushMatrix()

    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 0.0)
    glEnd()
    glPopMatrix()


def draw_sidewall2(color):
    glPushMatrix()

    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glEnd()
    glPopMatrix()


def draw_roofside1(color):

    glPushMatrix()
    glColor3fv(color)
    glBegin(GL_POLYGON)
    glVertex3f(-1.1, .9, 0.1)
    glVertex3f(1.1, .9, 0.1)
    glVertex3f(1.1, 1.5, -0.5)
    glVertex3f(-1.1, 1.5, -0.5)
    glEnd()
    glPopMatrix()


def draw_roofside2(color):
    glPushMatrix()
    glColor3fv(color)
    glBegin(GL_POLYGON)
    glVertex3f(1.1, .9, -1.1)
    glVertex3f(-1.1, .9, -1.1)
    glVertex3f(-1.1, 1.5, -0.5)
    glVertex3f(1.1, 1.5, -0.5)
    glEnd()
    glPopMatrix()


def draw_roofend2(color):
    glPushMatrix()
    glColor3fv(color)
    glBegin(GL_TRIANGLES)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(-1.0, 1.5,-0.5)
    glVertex3f(-1.0, 1.0, -1.0)
    glEnd()
    glPopMatrix()


def draw_roofend1(color):
    glPushMatrix()
    glColor3fv(color)
    glBegin(GL_TRIANGLES)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.5, -0.5)
    glEnd()
    glPopMatrix()


def draw_rowofhouses():
    glPushMatrix()
    glTranslatef(3.0, 0.0, 0.0)
    draw_house((0.82, 0.7, 0.55), (0.82, 0.4, 0.1), False)
    glTranslatef(3.0, 0.0, 0.0)
    draw_house((0.365,0.247,0.827), (0.902,0.902,0.98), False)
    glTranslatef(3.0, 0.0, 0.0)
    draw_house((0.502,0.,0.125), (0.933,0.294,0.169),False)
    glTranslatef(3.0, 0.0, 0.0)
    draw_house((0.,0.639,0.424), (0.376,0.51,0.714),True)
    glPopMatrix()


# draw the door, set rotation angle to a global variable to be toggled on keyboard
# input need to add this to push
def draw_controlled_door():
    global doorangle
    glPushMatrix()
    glColor3f(0.545, 0.412, 0.078)
    glRotatef(doorangle, 0 , 0.1, 0.0)
    glTranslatef(0.0, 0, 0.0)
    glBegin(GL_QUADS)

    glVertex3f(-0.2, .4, 0.0)
    glVertex3f(0, 0.4, 0.0)
    glVertex3f(0, 0, 0.0)
    glVertex3f(-0.2, 0, 0.0)
    glEnd()
    glPopMatrix()


def draw_door():
    glPushMatrix()
    glColor3f(0.545, 0.412, 0.078)
    glRotatef(0, 0, 0.1, 0.0)
    glTranslatef(0.0, 0, 0.0)
    glBegin(GL_QUADS)

    glVertex3f(-0.2, .4, 0.0)
    glVertex3f(0, 0.4, 0.0)
    glVertex3f(0, 0, 0.0)
    glVertex3f(-0.2, 0, 0.0)
    glEnd()
    glPopMatrix()

def draw_street():
    glPushMatrix()
    glColor3f(0.0, 0.0, 0.1)
    glBegin(GL_POLYGON)
    glVertex3f(-20.0, 0.1, 3.0)
    glVertex3f(20.0, 0.1, 3.0)
    glVertex3f(20.0, 0.1, 1.0)
    glVertex3f(-20.0, 0.1, 1.0)
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex3f(-20.0, 0.3, 2.2)
    glVertex3f(20.0, 0.2, 2.0)
    glVertex3f(20.0, 0.3, 2.0)
    glVertex3f(-20, 0.2, 2.2)
    glEnd()
    glPopMatrix()


# draws the ground plane
def draw_ground():
    # #global grass_textureData
    # grass_texture = pygame.image.load("grass20.png")
    # grass_textureData = pygame.image.tostring(grass_texture, "RGBA", 1)
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.4, 0.2)
    #glTexCoord2f(0.0, 0.0)
    glVertex3f(-20.0,0.0, 10.0)
    #glTexCoord2f(0.0, 1.0)
    glVertex3f(20.0, 0.0, 10.0)
    #glTexCoord2f(1.0, 1.0)
    glVertex3f(20.0, 0.0, -10.0)
    glVertex3f(-20.0, 0.0, -10.0)

    # adding a slope
    glVertex3f(20.0, 0.0, -10.0)
    glVertex3f(20, 1, -20)
    glVertex3f(-20, 1, -20)
    glVertex3f(-20.0, 0.0, -10.0)
    # slope to right of above slope
    glVertex3f(20, 1, -20)
    glVertex3f(30, 1, -20)
    glVertex3f(30, 0, -10)
    glVertex3f(20, 0, -10)



    # glTexCoord2f(1.0, 0.0)
    #glVertex3f()
    glEnd()
    draw_street()
    glTranslatef(-8.0, 0.0, 0.0)
    draw_rowofhouses()

    glPopMatrix()


def draw_tree():
    glPushMatrix()
    #glBegin(GL_QUADS)
    # drawing the stump
    quad = gluNewQuadric()
    glColor3f(0.545, 0.271, 0.075)
    glRotatef(90, 1, 0, 0)
    glTranslatef(2.5, -0.2, -.2)
    gluCylinder(quad, .1, .1, .4, 16, 8)
    #glEnd()
    glPopMatrix()
    # drawing the top of the tree
    glPushMatrix()
    glColor3f(0.035, 0.475, 0.412)
    glRotatef(270, 1, 0, 0)
    glTranslatef(2.5, 0.2, 0.2)
    glutSolidCone(.3, 1, 9, 3)
    glPopMatrix()

def draw_sky():
    glPushMatrix()

    glColor3f(0.529, 0.808, 0.922)
    glRotatef(-5, 1, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(-100, 30, -25)
    glVertex3f(100, 30, -25)
    glVertex3f(100, 0, -25)
    glVertex3f(-100, 0, -25)

    # glColor3f(0.529, 0.808, 0.922)
    # glVertex3f(50, 30, -25)
    # glVertex3f(50, 0, -25)
    # glVertex3f(50, 0, 25)
    # glVertex3f(50, 30, 25)
    glEnd()
    glPopMatrix()


def display():
    global camerax, cameraz, lookx, lookz
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(camerax, 1.0, cameraz, lookx, 0.0, lookz , 0.0, 1.0, 0.0)
    draw_ground()
    draw_tree()
    draw_sky()
    glDepthFunc(GL_LESS)  # this is default

    glFlush()
    glutSwapBuffers()


def reshape(w, h):

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 1.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def key_inputs(key, x, y):
    global camerax, cameraz, lookx, lookz, doorangle, sunstate
    ch = key.decode("utf-8")
    if ch == 'l':
        if camerax < 10:
            camerax += 1
    if ch == 'r':
        if camerax > -10:
            camerax -= 1
    if ch == "d":
        if lookx < 10:
            lookx +=1
    if ch == "a":
        if lookx > -10:
            lookx -=1
    if ch == 'u':
        cameraz -= 1
        lookz -= 1
    if ch == 'j':
        cameraz += 1
        lookz += 1
    if ch == 's':
        if doorangle == 90:
            doorangle = 0
            #print("door angle changed")

        else:
            doorangle = 90
            #print("door angle changed")
    if ch == 'y':
        if sunstate == 1:
            sunstate = 0
            glDisable(GL_LIGHT0)
            glLightfv(GL_LIGHT1, GL_AMBIENT, [0.0, 0.0, 0.0, 1])
            glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.0, 0.0, 0.0, 1])
            glLightfv(GL_LIGHT1, GL_POSITION, [0, 2, 0, 1])
            glEnable(GL_LIGHT1)
        else:
            sunstate = 1
            glDisable(GL_LIGHT1)
            glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
            glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1])
            glLightfv(GL_LIGHT0, GL_POSITION, [0, 2, 0, 1])
            glEnable(GL_LIGHT0)
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE)
    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Ethan Eichelberger FinalProject")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(key_inputs)
    glutReshapeFunc(reshape)
    glutMainLoop()


main()
