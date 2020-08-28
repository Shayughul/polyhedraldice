bl_info = {
	"name": "Increase all Meshes by 1.1",
	"category": "Add",
	"author": "Beau Lundmark",
	"version": (1, 0),
	"blender": (2, 83, 0),
}


import bpy

class OBJECT_OT_increase_mesh_11(bpy.types.Operator):
	"""Increase all Meshes by 1.1"""     
	bl_idname = "object.increase_mesh_11"        
	bl_label = "Mesh Increase 1.1"         
	bl_options = {'REGISTER', 'UNDO'}  

	def execute(self, context):

		for obj in bpy.context.scene.objects:
			if obj.type == 'MESH':
				obj.scale = (1.1,1.1,1)
				obj.select_set(True)
				bpy.ops.object.transform_apply(location = False, rotation = False, scale = True)

		return {'FINISHED'}

def menu_draw(self, context):
		self.layout.operator("object.increase_mesh_11")


def register():
	bpy.utils.register_class(OBJECT_OT_increase_mesh_11)
	bpy.types.VIEW3D_MT_add.prepend(menu_draw)


def unregister():
	bpy.utils.unregister_class(OBJECT_OT_increase_mesh_11)
	bpy.types.VIEW3D_MT_add.remove(menu_draw)

if __name__ == "__main__":
	register()