#----------------------------------------------------------
# File meshes.py
#----------------------------------------------------------
import bpy
import math
 
def createMesh(name, origin, verts, edges, faces):
    # Create mesh and object
    me = bpy.data.meshes.new(name+'Mesh')
    ob = bpy.data.objects.new(name, me)
    ob.location = origin
    ob.show_name = True
    # Link object to scene
    bpy.context.scene.objects.link(ob)
 
    # Create mesh from given verts, edges, faces. Either edges or
    # faces should be [], or you ask for problems
    me.from_pydata(verts, edges, faces)
 
    # Update mesh with new data
    me.update(calc_edges=True)
    return ob

#Using the theory we defined in lecture
def getAnglesFor(n):
    angles = []
    denom = 2**n - 1
    for i in range(n):
        angles.append((2**i) * 2 * math.pi/denom)
    return angles

def getXYVertsForAngles(angles, radius=1):
    #First point:
    pointOrigin = (0,0)
    pointCurrent = (0, radius)
    points = [pointOrigin, pointCurrent]

    for angle in angles:
        angleOpposite = (math.pi - angle)/2
        oo = math.atan2(pointCurrent[1] - pointOrigin[1], pointCurrent[0] - pointOrigin[0])
        oo = oo + angleOpposite
        d = getDistance(pointCurrent, pointOrigin) * math.sin(angleOpposite) / math.sin(math.pi - angleOpposite - angle)
        pointCurrent = (pointCurrent[0] + d * math.cos(oo), pointCurrent[1] + d * math.sin(oo))
        points.append(pointCurrent)

    faces = []
    points3DTop = []
    points3DBottom = []
    pointOrigin = points[0]
    for point in points[1:]:
        pointTop = (point[0], point[1], width/2)
        pointBottom = (point[0], point[1], 1-width/2)
        points3D.append(pointTop, pointBottom)
        


 
def run(origin, n, radius=1, width=3):
    angles = getAnglesFor(n)
    getXYVertsForAngles(angles)

    (x,y,z) = (0.707107, 0.258819, 0.965926)
    verts1 = ((x,x,-1), (x,-x,-1), (-x,-x,-1), (-x,x,-1), (0,0,1))
    faces1 = ((1,0,4), (4,2,1), (4,3,2), (4,0,3), (0,1,2,3))
    ob1 = createMesh('Solid', origin, verts1, [], faces1)
 
    # Move second object out of the way
    ob1.select = False
    ob2.select = True
    bpy.ops.transform.translate(value=(0,2,0))
    return
 
if __name__ == "__main__":
    run((0,0,0), 3)