from turtle import Turtle
from math import sin, cos, radians
import turtle
from PIL import Image
import os,time

'''
A circle can be defined as the locus of all points that satisfy the equations:

x= r.cos(t); y=r.sin(t)

where x,y are the coordinates of any point on the circle, r is the radius of the circle and
t is the parameter - the angle subtended by the point at the circle's center.

If we let x and y be the coordinates of the center of the circle, 
we simply add them to the a and b coordinates in the equations, which then become:

a  =  x + r cos(teta)
b  =  y + r sin(teta)

where r is the radius of the circle, and x,kyare the coordinates of the center.
more info: https://www.mathopenref.com/coordparamcircle.html

'''
def check_cordinat(radius, d, x, y, h, w):
    # check if circule will fit in square(fully contained in image)
    if(x+radius+d > h/2):
        print("The circle is outside of the figure on the right side")
        quit()
    elif(x-radius-d< -(h/2)):
        print("The circle is outside of the figure on the left side")
        quit()
    if(y+radius+d > w/2 ):
        print("The circle is outside of the figure on the to side")
        quit()
    elif(y-radius+d < -(w/2)):
        print("The circle is outside of the figure on the button side")
        quit()

    
def circle(radius, d, x, y, h, w, color="black"):
    try:
        # ------ optimizing turtle -------------# 
        turtle.tracer(0, 0)
        turtle.speed("fastest")
        tr = Turtle(visible=True)
        #---------------------------------------
        # this assures that the size of the image is set by user ...
        screen = turtle.Screen()
        screen.setup(h, w)
        tr.width(d)
        tr.penup()
        tr.goto(x + radius, y)
        tr.pendown()

        # color of drawing line
        tr.color("blue", color)
        tr.begin_fill()
        #-------------------------------------------------
        # Circle drawing starts here
        for i in range(1, 361):
            tr.goto(radius * cos(radians(i)) + x,
                   radius * sin(radians(i)) + y)
        # Circle drawing ends here
        #-------------------------------------------------
        tr.end_fill()
        ts = turtle.getscreen()
        # export as eps objects
        ts.getcanvas().postscript(file="circle.eps")
        turtle.update()
        #turtle.done()
        try:
            turtle.bye()   
        except turtle.Terminator:
            pass

        # convert eps into circle
        img = Image.open('circle.eps')
        img.save('circle.png', 'png')
        print("Plot generated in: ", os.getcwd())
        # remove the eps file
        os.remove("circle.eps")

    except OSError:
        pass

def run(radius, d, x, y, h, w):
    # get time 
    start_time = time.time()
    # check cordinates
    check_cordinat(radius, d, x, y, h, w)
    # plot
    circle(radius, d, x, y, h, w,)
    print("generated plot in:  --- %s seconds ---" % (time.time() - start_time))

