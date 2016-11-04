#Team 3 - nsided die problem
- David Watkins (djw2146)
- David RC
- Shardendu

##Progress since class 1 (10/26)
- We all got our certification to use the Maker Space
- We generated a script to produce n-sided die
- We realized that the proportion of the angle that defines the length of a side can be the center of a cirlce that circumscribes an n-sided polygonal barrel die. Therefore for a six sided die the angles of the triangles form from the center point to two adjacent vertices could be: 2*pi * 1/63, 2*pi * 2/63, 2*pi * 4/63, etc.
- We looked at bullet for attempting to simulate the rolling of die but we haven't had any progress yet. 


-There was discussion from class about making a robot die that could internally force a distribution, and it was permitted. Although it seemed extremely hard, we trivialized it to just a die with an accelerometer and 6 led on each side with a loaded side that the die physically lands on everytime, while the led change the labels of the faces. We predict the class will not allow this.

-We have a barrel die model that involves a regular hexagon and internal trapezoids (1 triangle) to manipulate the weight of each face's sector without changing the the center of mass. The idea being that the weight of each face should be proportional to its weight assuming the center of mass stays in the middle. Some math and documents have been uploaded to showcase the idea. This is the current model we are playing with.

##Progress since class 2
