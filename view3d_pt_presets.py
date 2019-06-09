import bpy


class ViewportPresets(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Viewport presets panel"
    bl_idname = "VIEW3D_PT_presets"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        prefs = context.preferences.addons[__package__].preferences

        layout.label(text="Presets")

        row = layout.row()
        col = row.column()

        i = 0
       
        for preset in prefs.presets:
            op = col.operator('view3d.applypreset', text=preset.name )
            op.index = i
            params = op.preset.__annotations__.keys()

            for param in params:
                setattr(op.preset, param, getattr(preset, param))

            i = i + 1

        row.operator("view3d.savepreset", text="", icon='ADD', emboss=False)

        row=layout.row()

        row.prop(prefs.presets[prefs.selected_index], "name")


def view3d_presets_draw(self, context):
    layout = self.layout

    self.layout.popover(
        panel="VIEW3D_PT_presets",
        text="Presets",
    )

def register():
    bpy.utils.register_class(ViewportPresets)
    bpy.types.VIEW3D_HT_header.append(view3d_presets_draw)


def unregister():
    bpy.utils.unregister_class(ViewportPresets)
    bpy.types.VIEW3D_HT_header.remove(view3d_presets_draw)


if __name__ == "__main__":
    register()