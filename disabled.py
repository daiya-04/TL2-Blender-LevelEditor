import bpy

class MYADDON_OT_add_disabled(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_add_disabled"
    bl_label = "Disabled 追加"
    bl_description = "['disabled']カスタムプロパティを追加します"
    bl_options = {"REGISTER","UNDO"}

    def execute(self, context):
        context.object["disabled"] = True

        return {"FINISHED"}


class OBJECT_PT_disabled(bpy.types.Panel):
    """オブジェクトの種類の名前パネル"""
    bl_idname = "OBJECT_PT_disabled"
    bl_label = "Disabled"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    def draw(self, context):
        if "disabled" in context.object:
            #既にプロパティがあれば、プロパティを表示
            self.layout.prop(context.object, '["disabled"]', text = self.bl_label)
        else:
            #プロパティがなければ、プロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_add_disabled.bl_idname)