import bpy
import bmesh

class Tria():
    def __init__(self):
        print('init')
        self.cnt = 1
    def create_tria(self, coords):
        # Create a new mesh and a new object
        mesh = bpy.data.meshes.new(name=f"mesh_{self.cnt:03n}")
        obj = bpy.data.objects.new(name=f"obj_{self.cnt:03n}", object_data=mesh)
        # Link the object to the collection
        bpy.context.collection.objects.link(obj)
        # Set the object as the active object
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        # Create a bmesh object and add the vertices to it
        bm = bmesh.new()
        for coord in coords:
            bm.verts.new(coord)
        # Create a face using the vertices
        bm.faces.new(bm.verts)
        # Update the bmesh to the mesh
        bm.to_mesh(mesh)
        bm.free()
        self.cnt += 1

t = Tria()

coords = [(0,0,0), (0,1,0), (1,1,1)]
t.create_tria(coords)
