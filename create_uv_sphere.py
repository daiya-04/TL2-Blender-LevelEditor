import bpy

#オペレータ UV球生成
class MYADDON_OT_create_uv_sphere(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_create_uv_object"
    bl_label = "UV球生成"
    bl_description = "UV球を生成します"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_uv_sphere_add()
        print("UV球を生成しました。")

        return {'FINISHED'}