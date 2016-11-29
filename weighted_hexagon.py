#----------------------------------------------------------
# File weighted_hexagon.py
#----------------------------------------------------------
# import bpy

import math
import matplotlib.pyplot as plt
 
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

def getXYVertsForAngles(angles, radius=1, width=3):
    verts = []
    faces = []
    
    

    return verts, faces
 
def run(origin):
    verts, faces = getVertFaces()

    ob1 = createMesh('Die', origin, verts, [], faces)
    return
 
if __name__ == "__main__":
    run((0,0,0))