__version__ = '1.0.3'

bl_info = {
    "name": "Viewport Presets",
    "author": "Andrew Charlton",
    "version": (1, 0, 3),
    "blender": (2, 80, 0),
    "location": "3D Viewport Header",
    "description": "Adds a preset popup to allow easy saving and recall of viewport shading, overlays and gizmos",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}

if 'bpy' in locals():
    import importlib

    if 'ViewportPresets' in locals():
        importlib.reload(view3d_pt_presets)
        importlib.reload(viewport_presets_addonprefs)
        importlib.reload(view3d_applypreset)
        importlib.reload(view3d_savepreset)
        importlib.reload(view3d_deletepreset)
else:
    from . import view3d_pt_presets
    from . import viewport_presets_addonprefs
    from . import view3d_applypreset
    from . import view3d_savepreset
    from . import view3d_deletepreset 

import bpy

def register():
    view3d_pt_presets.register()
    viewport_presets_addonprefs.register()
    view3d_applypreset.register()
    view3d_savepreset.register()
    view3d_deletepreset.register()
  
def unregister():
    view3d_pt_presets.unregister()
    viewport_presets_addonprefs.unregister()
    view3d_applypreset.unregister()
    view3d_savepreset.unregister()
    view3d_deletepreset.unregister()

if __name__ == "__main__":
    register()
