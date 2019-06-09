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

        prefs.selected_index = len(prefs.presets) -1

        for param in params:
            if hasattr(space.overlay, param):
                setattr(preset, param, getattr(space.overlay, param))

            if hasattr(space, param):
                setattr(preset, param, getattr(space, param))

            if hasattr(space.shading, param):
                setattr(preset, param, getattr(space.shading, param))

        return {'FINISHED'}

def register():
    bpy.utils.register_class(SavePreset)

def unregister():
    bpy.utils.unregister_class(SavePreset)
