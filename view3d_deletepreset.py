import bpy
from . import viewport_presets_addonprefs



class DeletePreset(bpy.types.Operator):
    bl_idname = "view3d.deletepreset"
    bl_label = "Save preset"

    index: bpy.props.IntProperty(default=-1)

    def execute(self, context):
        prefs = bpy.context.preferences.addons[__package__].preferences

        if self.index >= 0:
            prefs.presets.remove(self.index)

        prefs.selected_index = -1

        return {'FINISHED'}

def register():
    bpy.utils.register_class(DeletePreset)

def unregister():
    bpy.utils.unregister_class(DeletePreset)
