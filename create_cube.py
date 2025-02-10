import bpy

#オペレータ Cube生成
class MYADDON_OT_create_cube(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_create_cube"
    bl_label = "Cube生成"
    bl_description = "Cubeを生成します"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        print("Cubeを生成しました。")

        return {'FINISHED'}