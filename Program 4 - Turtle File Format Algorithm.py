##CS 101
##Program 1
##Christina Gerstner
##clgdtf@mail.umkc.edu
##
##Problem: A new graphics file format called turtle has been created and you are tasked
##      writing a python program to read the data from the file and using the turtle
##      module to draw the shapes from the file. This assignment will have you using
##      your skills with file handling, error handling, string manipulation and using
##      the turtle module. To make this easier you should use your newfound knowledge
##      of functions to break the program down into smaller testable portions. You will
##      be required to use functional decomposition in your assignments from this
##      assignment on.
##
##ALGORITHM:
##
##
##ERROR HANDLING: None
##
##OTHER COMMENTS: None
##################################################################################################
import turtle

def determineShapeFile(fileName):
	if fileName == rectangle file:
                return True
	elif fileName == circle file:
                return True
	elif fileName == star file:
                return True
        elif fileName == pythonlogo file:
                return True
        elif fileName == badcommand file:
                return True
        elif fileName == rectangle_value_error file:
                return True
        elif fileName == rectangle_index_error file:
                return True
        else:
                return False

def drawShape(shapeFile):
        shapeDetails = open(shapeFile)
        
        if shapeFile == 'rectangle.tff':
		#draw_rectangle(x, y, width, height, color)
	elif shapeFile == 'circle.tff':
		#draw_circle(x, y, radius, color)
	elif shapeFile == 'star.tff':
                #draw_star(x, y) #more parameters are probably needed
        elif shapeFile == 'pythonlogo.tff':
                #draw_pythonlogo(x, y) #more parameters are probably needed

def draw_rectangle(x : int, y : int, width : int, height : int, color : str) -> None:
	""" Draws a rectangle of given width and height at position x, y
		Parameters :
			x : int - The x position of the top left corner.
			y : int - The y position of the top right corner.
			width : int - The width of the rectangle to be drawn
			height : int - The height of the rectangle to be drawn
			color : str - The color to draw the circle with and fill
		returns : None
	"""
	# Reads file
	# use turtle to draw lines of 3 rectangles
	# use fill method to color rectangles from rectangle.tff

def draw_circle(x : int, y : int, radius : int, color : str) -> None:
	""" Draws a circle with turtle at the point x, y with the given radius
		Parameters :
			x : int - The x position of the center of the circle.
			y : int - The y position of the center of the circle.
			radius : int - The radius of the circle to be drawn
			color : str - The color of the circle and the fill color
		returns : None
	"""
	# Reads file
	# use turtle to draw 3 circles in different locations
	# use fill method to color circles from circle.tff

def draw_star(x : int, y : int, width : int, height : int, color : str) -> None:
	""" Draws a circle with turtle at the point x, y with the given radius
		Parameters :
			x : int - The x position of the center of the circle.
			y : int - The y position of the center of the circle.
			width : int - The width of the rectangle to be drawn
			height : int - The height of the rectangle to be drawn
			color : str - The color of the circle and the fill color
		returns : None
	"""
	# Reads file
	# use turtle to draw lines of 3 star in different locations
	# use fill method to color stars from star.tff

def draw_pythonlogo_4(x : int, y : int, width : int, height : int, color : str) -> None:
	""" Draws a circle with turtle at the point x, y with the given radius
		Parameters :
			x : int - The x position of the center of the circle.
			y : int - The y position of the center of the circle.
			width : int - The width of the rectangle to be drawn
			height : int - The height of the rectangle to be drawn
			color : str - The color of the circle and the fill color
		returns : None
	"""
	# Reads file
	# use turtle to draw lines of all shapes w/ 4 sides in different locations
	# use fill method to color shapes from pythonlogo.tff

def draw_pythonlogo_3(x : int, y : int, radius : int, color : str) -> None:
	""" Draws a circle with turtle at the point x, y with the given radius
		Parameters :
			x : int - The x position of the center of the circle.
			y : int - The y position of the center of the circle.
			radius : int - The radius of the circle to be drawn
			color : str - The color of the circle and the fill color
		returns : None
	"""
	# Reads file
	# use turtle to draw curves of all shapes in different locations
	# use fill method to color shapes from pythonlogo.tff

exist = True
while exist:
        userFile = input('Enter File to open & draw ==>\t')

        if userFile.lower() == 'quit':
                exist = False

        validateFile = determineShapeFile(userFile)
        if validateFile == False:
                print('Could not open file :', userFile)
        else:
                if userfile == 'badcommand.tff' or userfile == 'rectangle_value_error.tff' or userfile == 'rectangle_index_error.tff':
                        file = open(userFile)
                        content = file.readlines()
                        file.close()

                        for line in content:
                                print(line)
                else:
                        drawShape(userFile) # drawShape(shapeFile) function
        


