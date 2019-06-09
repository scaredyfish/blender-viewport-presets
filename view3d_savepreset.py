import bpy
from . import viewport_presets_addonprefs


class SavePreset(bpy.types.Operator):
    bl_idname = "view3d.savepreset"
    bl_label = "Save preset"

    def execute(self, context):
        prefs = bpy.context.preferences.addons[__package__].preferences

        space = context.area.spaces[0]

        preset = prefs.presets.add()
        preset.name = "New preset"
        params = preset.__annotations__.keys()

        for param in params:
            if hasattr(space.overlay, param):
                setattr(preset, param, getattr(space.overlay, param))

            if hasattr(space, param):
                print("saving " + param)
                setattr(preset, param, getattr(space, param))

        return {'FINISHED'}

def register():
    bpy.utils.register_class(SavePreset)

def unregister():
    bpy.utils.unregister_class(SavePreset)
