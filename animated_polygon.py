from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time

user_polygon, user_color = [], []
angle_step = 1  # Angle step for rotation
pivot_point = (0, 0)  # Pivot point for rotation

def get_user_polygon():
    '''
    Gets and returns x, y coordinates of a polygon
    from user input, coordinates to be specified in anti-clockwise manner
    '''
    list_of_coordinates = []
    while True:
        print("Enter the x, y coordinates of your Polygon (Enter 'done' to finish):")
        x_input = input("x: ")
        if x_input.lower() == 'done':
            break
        y_input = input("y: ")
        try:
            x = float(x_input)
            y = float(y_input)
            coordinates = (x, y)
            list_of_coordinates.append(coordinates)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    return list_of_coordinates

def get_user_color():
    '''
    Gets and returns the color specified from user input in RGB format
    values to range from 0.0 to 1.0
    '''
    print("Enter color you wish in RGB format (values between 0 and 1):")
    r = float(input("Red: "))
    g = float(input("Green: "))
    b = float(input("Blue: "))
    return r, g, b

def get_maximum_coordinate(list_coordinates):
    '''Get and return the maximum value from a list of x, y coordinates
    '''
    max_coord = 0.0
    for coord in list_coordinates:
        max_coord = max(max_coord, max(coord))
    return max_coord

def choose_ortho(max_coordinate):
    '''
    Automatically determines the best values for gluOrtho2D based on the maximum coordinate
    '''
    margin = 3.0  # Margin to add around the maximum coordinate
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-max_coordinate - margin, max_coordinate + margin, -max_coordinate - margin, max_coordinate + margin)

def draw_polygon(coordinates, color):
    '''
    Draws a polygon based on the given coordinates and color
    '''
    glColor3f(*color)
    glBegin(GL_POLYGON)
    for x, y in coordinates:
        glVertex2f(x, y)
    glEnd()

def rotate_polygon(coordinates, angle):
    '''
    Rotates the polygon around the pivot point by the given angle
    '''
    rotated_coordinates = []
    for x, y in coordinates:
        x_rotated = pivot_point[0] + (x - pivot_point[0]) * math.cos(math.radians(angle)) - (y - pivot_point[1]) * math.sin(math.radians(angle))
        y_rotated = pivot_point[1] + (x - pivot_point[0]) * math.sin(math.radians(angle)) + (y - pivot_point[1]) * math.cos(math.radians(angle))
        rotated_coordinates.append((x_rotated, y_rotated))
    return rotated_coordinates

def display():
    global user_polygon, user_color
    # Clear the color buffer
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw the polygon with user-specified coordinates and color
    draw_polygon(user_polygon, user_color)
    
    # Swap the buffers to display the polygon
    glutSwapBuffers()

def idle():
    global user_polygon, angle_step
    # Rotate the polygon by the angle step
    user_polygon = rotate_polygon(user_polygon, angle_step)
    
    # Redisplay the window
    glutPostRedisplay()

    # Introduce a small delay to slow down the animation
    time.sleep(0.02)  # Adjust the delay as needed (in seconds)

def main():
    global user_polygon, user_color, angle_step
    # Get user input for polygon coordinates and color
    user_polygon = get_user_polygon()
    user_color = get_user_color()
    max_coord = get_maximum_coordinate(user_polygon)

    # Initialize OpenGL
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow("Rotating Polygon Animation")

    # Define viewport and projection
    glViewport(0, 0, 600, 600)
    choose_ortho(max_coord)  # Automatically adjust gluOrtho2D based on max coordinate
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Set clear color and display function
    glutDisplayFunc(display)
    glutIdleFunc(idle)  # Register idle function for animation

    # Start the main loop
    glutMainLoop()

if __name__ == "__main__":
    main()
