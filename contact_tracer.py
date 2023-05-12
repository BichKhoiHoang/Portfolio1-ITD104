# -----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  ITD104, "Building IT Systems", TP2, 2021.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 10578919  # put your student number here as an integer
student_name = 'Bich Khoi Hoang'  # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------------------------------------------------#


# -----Task Description-----------------------------------------------#
#
#  CONTACT TRACER
#
#  This assessment item tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "visualise".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various symbols, using data stored in a list to
#  determine which symbols to draw and where.  See the various
#  "client requirements" in Blackboard for full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by the client.
#  This single template file will be used for all parts and you will
#  submit your final solution as a single Python 3 file only, whether
#  or not you complete all requirements for the assignment.
#
# --------------------------------------------------------------------#


# -----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.
# YOU MUST NOT CHANGE ANY OF THE CODE IN THIS SECTION.
#

# Import standard Python modules needed to complete this assignment.
# [No other modules are needed for your solution.
# Your solution MUST NOT rely on any other modules.]
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values unless
# instructed.
cell_size = 90  # pixels (default is 90)
grid_width = 8  # squares (default is 8)
grid_height = 6  # squares (default is 6)
x_margin = cell_size * 2.75  # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2  # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', cell_size // 6, 'normal')  # font for the coords
big_font = ('Arial', cell_size // 5, 'normal')  # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 6, 'Grid must be at least 6 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'


#
# --------------------------------------------------------------------#

# -----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  Do NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour='light grey',
                          line_colour='slate grey',
                          draw_grid=True,
                          label_spaces=True):  # NO! DON'T TOUCH THIS!

    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0)  # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)

        # Draw the vertical grid lines
        setheading(90)  # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3  # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(str(x_label + 1), align='center', font=small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 10, cell_size // 10  # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(chr(y_label + ord('A')), align='right', font=small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(cell_size // 6)

    # Optionally mark the blank spaces ... NO! YOU CAN'T CHANGE ANY OF THIS CODE!
    if label_spaces:
        # Left side
        goto(-((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align='right', font=big_font)
        # Right side
        goto(((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align='left', font=big_font)

        # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor=True):
    tracer(True)  # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()


#
# --------------------------------------------------------------------#


# -----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "visualise" function.  ALL of your solution code
#  must appear in this area.  Do NOT put any of your code in other
#  parts of the program and do NOT change any of the provided code
#  except as allowed in the main program below.
#
house_length = 30
house_width = 40
house_roof = 30


# Define a function to draw the house
def draw_house(frame_color, house_color, door_window_color, roof_color):
    # step1: draw the house
    pencolor('black')
    fillcolor(frame_color)
    setheading(0)
    pendown()
    begin_fill()
    for i in range(4):
        forward(cell_size)
        left(90)
    end_fill()
    # step2: draw triangle
    penup()
    setheading(0)
    forward(30)
    fillcolor(house_color)
    pendown()
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            forward(house_length)
            left(90)
        else:
            forward(house_width)
            left(90)
    end_fill()
    # step3: draw door
    penup()
    setheading(0)
    forward(5)
    fillcolor(door_window_color)
    pendown()
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            forward(15)
            left(90)
        else:
            forward(20)
            left(90)
    end_fill()
    # step4: draw window
    penup()
    setheading(70)
    forward(25)
    setheading(0)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        left(90)
    end_fill()
    # step4: draw roof
    penup()
    setheading(131)
    forward(21)
    fillcolor(roof_color)
    pendown()
    begin_fill()
    set_heading = [60, 300, 180]
    for i in set_heading:
        setheading(i)
        forward(30)
    end_fill()


cloud_direction = [45, 320, 45, 320, 45]


# define a function to draw cloud
def draw_cloud(radius, distance):
    dot(radius)
    for i in cloud_direction:
        setheading(i)
        forward(distance)
        dot(radius)


### Draw the house on a sunny day
def draw_sunny_day():
    # draw the house
    draw_house('yellow', 'light yellow', 'brown', 'red')
    # Draw the sun
    penup()
    setheading(30)
    forward(50)
    dot(20, 'orange')
    penup()


### Draw the house at starry night
def draw_starry_night():
    # draw the house
    draw_house('navy', 'orange', 'yellow', 'black')
    # draw the moon
    penup()
    pencolor('white')
    setheading(120)
    forward(30)
    pendown()
    dot(20)
    penup()
    pencolor('navy')
    forward(5)
    dot(15)
    # draw stars
    pencolor('white')
    setheading(0)
    forward(2)
    star_directions = [10, 330, 0, 210, 40, 180, 30, 220]
    star_steps = [1, 3, 2, 4, 5, 2, 4, 1]
    for x in star_directions:
        setheading(x)
        for y in star_steps:
            forward(y)
        dot(2)


### Draw the house on a cloudy day

def draw_cloudy_day():
    # draw the house
    draw_house('lightcyan', 'light yellow', 'brown', 'orange')
    # draw clouds
    penup()
    pencolor('white')
    setheading(130)
    forward(30)
    draw_cloud(10, 5)
    setheading(10)
    forward(20)
    draw_cloud(10, 5)


### Draw the house on a rainy day
def draw_gloomy_day():
    # draw the house
    draw_house('grey', 'brown', 'light yellow', 'tan')
    # draw the cloud
    pencolor('lavender')
    penup()
    setheading(110)
    forward(30)
    draw_cloud(20, 12)
    penup()
    # hideturtle()


def draw_image(image, x, y):
    goto(cell_size * (x - 5), (y - 68) * cell_size)
    if image == 'A':
        draw_sunny_day()
    elif image == 'B':
        draw_starry_night()
    elif image == 'C':
        draw_cloudy_day()
    elif image == 'D':
        draw_gloomy_day()


def visualise(steps):
    penup()
    pencolor('black')
    goto(-(cell_size * 6), cell_size)
    draw_sunny_day()
    goto(-(cell_size * 6), (cell_size - 30))
    write('A : A sunny day!', align='left', font=big_font)
    goto(-(cell_size * 6), -(cell_size * 2))
    draw_starry_night()
    goto(-(cell_size * 6), -(cell_size * 2) - 30)
    pencolor('black')
    write('B : A starry night!', align='left', font=big_font)
    goto(cell_size * 5, cell_size)
    draw_cloudy_day()
    goto(cell_size * 5, (cell_size - 30))
    pencolor('black')
    write('C : A cloudy day!', font=big_font, align='left')
    goto(cell_size * 5, -(cell_size * 2))
    draw_gloomy_day()
    goto(cell_size * 5, -(cell_size * 2) - 30)
    pencolor('black')
    write('D : A gloomy day!', align='left', font=big_font)

    for step in steps:
        if step[0] == "Start":
            y = ord(step[1])
            x = step[2]
            image = step[3]
            draw_image(image, x, y)
        elif step[0] == "Change":
            image = step[1]
        elif step[0] == "East":
            for i in range(step[1]):
                draw_image(image, x + i + 1, y)
            x = x + step[1] 
        elif step[0] == "West":
            for i in range(step[1]):
                draw_image(image, x - i - 1, y)
            x = x - step[1]
        elif step[0] == "North":
            for i in range(step[1]):
                draw_image(image, x, y + 1 + i)
            y = y + step[1]
        elif step[0] == 'South':
            for i in range(step[1]):
                draw_image(image, x, y - i - 1)
            y = y - step[1]

    #


# --------------------------------------------------------------------#


# -----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.  You
# should NOT change any of the code in this section.
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's "raw data" function if available, but otherwise
### creating a dummy function that returns an empty list
if isfile('data_generator.py'):
    print('\nNote: Data module found\n')
    from data_generator import raw_data


    def data_set(new_seed=None):
        seed(new_seed)
        return raw_data(grid_height, grid_width)
else:
    print('\nNote: No data module available\n')


    def data_set(dummy_parameter=None):
        return []

#
# --------------------------------------------------------------------#


# -----Main Program to Create Drawing Canvas--------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas()

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** overall theme
title("House in distinct kinds of weather")

### Call the student's function to process the data set
### ***** While developing your program you can call the
### ***** "data_set" function with a fixed seed for the
### ***** random number generator, but your final solution must
### ***** work with "data_set()" as the argument to "visualise",
### ***** i.e., for any data set that can be returned by
### ***** calling function "data_set" with no seed.
visualise(data_set())  # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
# --------------------------------------------------------------------#
