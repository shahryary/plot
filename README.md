# Circle plot
Plotting a black circle on a white background by using ''Turtle' 
---

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


Installation 
=============

###### *Approximate time ~ 5 minutes*

Before running program, you will need to install or check the installation of few packages.

##### Step A — Installing packages (skip if you have already )

Assume you are using python 3.X.X and already have pip3.

Install tkinter for python 3.X.X, you can install it in ubuntu with following command:
``` bash
$ sudo apt-get install python3-tk
```

Install libraries 

``` bash
$ pip3 install pillow
```

Download the "dist/circle-0.1.1.tar.gz" file. 
 
 ``` bash
$ pip3 install circle-0.1.1.tar.gz
```

##### Step B — Runnig program. 

``` bash
$ python3 -c "import draw; draw.run(100, 5, 20, 40, 800, 300)"
```
Parameters: 

1st: Radius of the circle in pixel

2nd: Thickness of the circle in pixel

3rd,4th: Center of the circle in pixel coordinate

5,6th: Size of the image in pixel

examples: 
=============

Will plot a circle with 150 radian, with thickness 3, center of circle in 50.50 and figure size 400 in 400 

``` bash
$ python3 -c "import draw; draw.run(150, 3, 50, 50, 400, 400)"
```
![shahryary/plot](images/circle1.png)

Will plot a circle with 200 radian, with thickness 5, center of circle in 50.50 and figure size 400 in 400 

``` bash
$ python3 -c "import draw; draw.run(100, 5, -40, -40, 400, 400)"
```
![shahryary/plot](images/circle2.png)