import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

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

def update(frame):
    global user_polygon, angle_step
    # Rotate the polygon by the angle step
    user_polygon = rotate_polygon(user_polygon, angle_step)
    
    # Clear the previous plot
    plt.clf()
    
    # Draw the rotated polygon
    plt.fill(*zip(*user_polygon), color=user_color)

def main():
    global user_polygon, user_color
    # Get user input for polygon coordinates and color
    user_polygon = get_user_polygon()
    user_color = get_user_color()

    # Set up the initial plot
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    
    # Set axis limits based on the maximum coordinate
    max_coord = max(np.abs(np.array(user_polygon).flatten()))
    ax.set_xlim([-max_coord, max_coord])
    ax.set_ylim([-max_coord, max_coord])

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=range(360), interval=20, repeat=True)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
