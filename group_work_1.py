from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(ch))

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Set background color to brown
    glClearColor(0.4, 0.2, 0.0, 1.0)

    # Draw text "JKUAT" in green
    glColor3f(0.0, 1.0, 0.0)  # Set the color for the text (green)
    draw_text(5, 5, "JKUAT")

    # Draw text "ROCKS" in red
    glColor3f(1.0, 0.0, 0.0)  # Set the color for the text (red)
    draw_text(8, 5, "ROCKS")

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 300)  # Increase window size for larger text
    glutCreateWindow(b"Text Rendering")
    glutDisplayFunc(display)
    glClearColor(0.4, 0.2, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 15, 0, 10)  # Set the orthographic projection
    glutMainLoop()

if __name__ == "__main__":
    main()
