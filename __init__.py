import bpy

from .create_uv_sphere import MYADDON_OT_create_uv_sphere
from .create_cube import MYADDON_OT_create_cube
from .export_scene import MYADDOM_OT_export_scene
from .my_menu import TOPBAR_MT_my_menu
from .collider import MYADDON_OT_add_collider, OBJECT_PT_collider, DrawCollider
from .filename import MYADDON_OT_add_filename, OBJECT_PT_file_name
from .objectname import MYADDON_OT_add_objectName, OBJECT_PT_object_name
from .disabled import MYADDON_OT_add_disabled, OBJECT_PT_disabled
from .spawn import MYADDON_OT_spawn_load_symbol, MYADDON_OT_spawn_create_symbol, MYADDON_OT_spawn_create_player_symbol, MYADDON_OT_spawn_create_enemy_symbol

# ブレンダーに登録するアドオン情報
bl_info = {
    "name": "レベルエディタ",
    "author": "Dai",
    "version": (1, 0),
    "blender": (3, 3, 1),
    "location": "",
    "description": "レベルエディタ",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

classes = (
    MYADDON_OT_create_uv_sphere,
    MYADDON_OT_create_cube,
    MYADDOM_OT_export_scene,
    TOPBAR_MT_my_menu,
    MYADDON_OT_add_filename,
    OBJECT_PT_file_name,
    MYADDON_OT_add_collider,
    OBJECT_PT_collider,
    MYADDON_OT_add_objectName,
    OBJECT_PT_object_name,
    MYADDON_OT_add_disabled,
    OBJECT_PT_disabled,
    MYADDON_OT_spawn_load_symbol,
    MYADDON_OT_spawn_create_symbol,
    MYADDON_OT_spawn_create_player_symbol,
    MYADDON_OT_spawn_create_enemy_symbol,
)

#アドオン有効化時コールバック
def register():
    #Blenderにクラスを登録
    for cls in classes:
        bpy.utils.register_class(cls)

    #メニューに項目を追加
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    #3Dビューに描画関数を追加
    DrawCollider.handle = bpy.types.SpaceView3D.draw_handler_add(DrawCollider.draw_collider, (), "WINDOW", "POST_VIEW")
    print("レベルエディタが有効化されました。")
    
#アドオン無効化時コールバック
def unregister():
    #メニューから項目を削除
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
    #3Dビューから描画関数を削除
    bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle, "WINDOW")

    #Blenderからクラスを削除
    for cls in classes:
        bpy.utils.unregister_class(cls)

    print("レベルエディタが無効化されました。")
    
# テスト実行用コード
if __name__ == "__main__":
    register()
