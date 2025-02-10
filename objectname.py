import bpy

#オペレータ カスタムプロパティ['object_name']追加
class MYADDON_OT_add_objectName(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_add_objectname"
    bl_label = "ObjectName 追加"
    bl_description = "['object_name']カスタムプロパティを追加します"
    bl_options = {"REGISTER","UNDO"}

    def execute(self,context):

        #['object_name']カスタムプロパティ追加
        context.object["object_name"] = ""

        return {"FINISHED"}


class OBJECT_PT_object_name(bpy.types.Panel):
    """オブジェクトの種類の名前パネル"""
    bl_idname = "OBJECT_PT_object_name"
    bl_label = "ObjectName"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    def draw(self, context):
        if "object_name" in context.object:
            #既にプロパティがあれば、プロパティを表示
            self.layout.prop(context.object, '["object_name"]', text = self.bl_label)
        else:
            #プロパティがなければ、プロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_add_objectName.bl_idname)