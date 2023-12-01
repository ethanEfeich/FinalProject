# Ethan Eichelberger


# Requirements
# ground plane with appropriate ground texture, NOT A SINGLE FLAT COLOR, grass dirt etc
# visible street
# some form of backgrounds (mountains, forest in the distance, cityscape, etc.)
#
# The scene must contain at least four constructed structures (houses, buildings, towers, etc.).  Houses must have a
# pitched roofs. Otherwise the shape of structures should be appropriate for the structure.  All houses must have a
# front door and two windows. One structure should be different than a house, like, for example,  a barn with a rounded
# roof or a dome (like an observatory), or a tower with with conical roof. The windows must be openings (not just black
# polygons).   The viewer must be able to see inside some structures.
#
# The one dwelling structures (houses)  must have a door. On at least one house (or similar building) the user must be
# able to toggle open and close the door
#
# The scene must be initially set in the daytime. At some point in the running of the application it should turn to
# night under user control.  This should result in low light conditions.  When night falls in the scene at least some
# of the habitable structures must have interior lighting and this must be visible in the application. And the user must
# be able to return the scene to daylight conditions
#
# The scene should have some vegetation in it (at least one tree, can have many)
#
# The sides of the structures must be distinguishable. That is, they may be different colors or different shades of
# colors, or you may apply textures to create this effect.
#
# The structures should not all be the same size. Although a collection of houses can be the same size but must vary in
# other ways.
#
# The scene must include light from the sun.  This should cast shadows of objects. It is not necessary to see the sun
# in the scene, only the lighting effects of the sun.
#
# During some portion of the application the viewer (camera) position must change under user control.  For example,
# panning to scan the scene. Also the user must be able to move the camera (referred to as tracking) across the scene
# (a view as if walking down the street).
#
# The view of the scene must be in perspective mode.
#
# The initial camera position should be  across from and looking at the constructed structures (houses).  It should be
# slightly above the street level, as if it is at eye level for a first-person viewer. An acceptable alternative is to
# place the camera in a slight aerial position as if looking down on the scene (but not straight down) from a slight
# elevation.
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

camerax = -1.0
lookx = 0.0


def init():
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_FLAT)

def draw_house():

    draw_backwall2()
    draw_frontwall()
    draw_sidewall1()
    draw_sidewall2()
    draw_roofside1()
    draw_roofside2()
    draw_roofend1()
    draw_roofend2()

def draw_backwall():
    glPushMatrix()
    glColor3f(0.0, 0.7, 0.7)
    glRotatef(180, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, -0.1)
    draw_frontwall()
    glPopMatrix()

def draw_frontwall():
    glPushMatrix()
    glColor3f(0.82, 0.7, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glEnd()
    glPopMatrix()

def draw_backwall2():

    glPushMatrix()
    glColor3f(0.0, 0.7, 0.55)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glEnd()
    glPopMatrix()

def draw_sidewall1():
    glPushMatrix()

    glColor3f(0.82, 0.7, 0.55)
    glBegin(GL_QUADS)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 0.0)
    glEnd()
    glPopMatrix()

def draw_sidewall2():
    glPushMatrix()

    glColor3f(0.82, 0.7, 0.55)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glEnd()
    glPopMatrix()

def draw_roofside1():
    glPushMatrix()
    glColor3f(0.82, 0.4, 0.1)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.5, -0.5)
    glVertex3f(-1.0, 1.5, -0.5)
    glEnd()
    glPopMatrix()

def draw_roofside2():
    glPushMatrix()
    glColor3f(0.82, 0.4, 0.1)
    glBegin(GL_POLYGON)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.5, -0.5)
    glVertex3f(1.0, 1.5, -0.5)
    glEnd()
    glPopMatrix()


def draw_roofend2():
    glPushMatrix()
    glColor3f(0.82, 0.4, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(-1.0, 1.5,-0.5)
    glVertex3f(-1.0, 1.0, -1.0)
    glEnd()
    glPopMatrix()

def draw_roofend1():
    glPushMatrix()
    glColor3f(0.82, 0.4, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.5, -0.5)
    glEnd()
    glPopMatrix()

def draw_rowofhouses():
    glPushMatrix()
    for i in range(0, 5):
        #draw_house()   #drawn at center, don't translate this one
        glTranslatef(3.0, 0.0, 0.0)
        draw_house()
    glPopMatrix()


def draw_street():
    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex3f(-20.0, 0.0, 3.0)
    glVertex3f(20.0, 0.0, 3.0)
    glVertex3f(20.0, 0.0, 1.0)
    glVertex3f(-20.0, 0.0, 1.0)
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex3f(-20.0, 0.3, 2.2)
    glVertex3f(20.0, 0.2, 2.0)
    glVertex3f(20.0, 0.3, 2.0)
    glVertex3f(-20, 0.2, 2.2)
    glEnd()
    glPopMatrix()


def draw_housesongreen():
    glPushMatrix()

    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.4, 0.2)
    glVertex3f(-20.0,0.0, 10.0)
    glVertex3f(20.0, 0.0, 10.0)
    glVertex3f(20.0, 0.0, -10.0)
    glVertex3f(-20.0, 0.0, -10.0)
    glEnd()
    draw_street()
    glTranslatef(-8.0, 0.0, 0.0)
    draw_rowofhouses()

    glPopMatrix()


def display():
    global camerax, lookx

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(camerax, 5.0, 5.0, lookx, 0.0, 0.0, 0.0, 1.0, 0.0)
#    draw_rowofhouses()
    draw_housesongreen()
#    draw_street()
    glDepthFunc(GL_LESS)  # this is default
    glEnable(GL_DEPTH_TEST)
    glFlush()
    glutSwapBuffers()


def reshape(w, h):

   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluPerspective(60.0, 1.0, 0.1, 50.0)
   glMatrixMode(GL_MODELVIEW)


def orbit(key, x, y):
    global camerax, lookx
    ch = key.decode("utf-8")
    if ch == 'l':
        camerax +=1
    if ch == 'r':
        camerax -=1
    if ch == "d":
        lookx +=1
    if ch == "a":
        lookx -=1
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE)
    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("A House")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(orbit)
    glutReshapeFunc(reshape)
    glutMainLoop()


main()
