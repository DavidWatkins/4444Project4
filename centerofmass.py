import numpy
from stl import mesh

#http://stackoverflow.com/questions/2083771/a-method-to-calculate-the-centre-of-mass-from-a-stl-stereo-lithography-file
#http://www.math.uiuc.edu/~redavid2/PW/TimsPaper.pdf

your_mesh = mesh.Mesh.from_file('2percent_6_sided_die.stl')

total_volume = 0
current_volume = 0
xCenter, yCenter, zCenter = 0,0,0 

for triangle in your_mesh.vectors:
    print(triangle)
    x1y2z3 = triangle[0][0] * triangle[1][1] * triangle[2][2]
    x1y3z2 = triangle[0][0] * triangle[2][1] * triangle[1][2]
    x2y1z3 = triangle[1][0] * triangle[0][1] * triangle[2][2]
    x2y3z1 = triangle[1][0] * triangle[2][1] * triangle[0][2]
    x3y1z2 = triangle[2][0] * triangle[0][1] * triangle[1][2]
    x3y2z1 = triangle[2][0] * triangle[1][1] * triangle[0][2]

    current_volume = (x1y2z3 - x1y3z2 - x2y1z3 + x2y3z1 + x3y1z2 - x3y2z1)/6

    total_volume += current_volume

    xCenter += ((triangle[0][0] + triangle[1][0] + triangle[2][0]) / 4) * current_volume
    yCenter += ((triangle[0][1] + triangle[1][1] + triangle[2][1]) / 4) * current_volume
    zCenter += ((triangle[0][2] + triangle[1][2] + triangle[2][2]) / 4) * current_volume

print("Total Volume = " + str(total_volume))
print("X Center = " + str(xCenter/total_volume))
print("Y Center = " + str(yCenter/total_volume))
print("Z Center = " + str(zCenter/total_volume))

cube = numpy.zeros(24, dtype=mesh.Mesh.dtype)
index = 0
for triangle in your_mesh.vectors:
    cube['vectors'][index] = numpy.array([[triangle[0][0], triangle[0][1], triangle[0][2]],
                                         [triangle[1][0], triangle[1][1], triangle[1][2]],
                                         [xCenter, yCenter, zCenter]])

cube = mesh.Mesh(cube)

# Optionally render the rotated cube faces
from matplotlib import pyplot
from mpl_toolkits import mplot3d

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Render the cube
# axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))#cube['vectors']))
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(cube.vectors))

# Auto scale to the mesh size
scale = cube.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()