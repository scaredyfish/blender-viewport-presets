import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty
from bpy.props import EnumProperty
from bpy.props import CollectionProperty
from bpy.props import PointerProperty

class ViewportPreset(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Preset name", default="Unknown")
    show_gizmo: bpy.props.BoolProperty(name="Show gizmo", default=True)
    show_gizmo_navigate : bpy.props.BoolProperty(default=True)
    show_gizmo_tool : bpy.props.BoolProperty(default=True)
    show_gizmo_context : bpy.props.BoolProperty(default=True)
    show_gizmo_object_translate : bpy.props.BoolProperty(default=True)
    show_gizmo_object_rotate : bpy.props.BoolProperty(default=True)
    show_gizmo_object_scale : bpy.props.BoolProperty(default=True)
    show_gizmo_empty_image : bpy.props.BoolProperty(default=True)
    show_gizmo_empty_forcefield : bpy.props.BoolProperty(default=True)
    show_gizmo_light_size : bpy.props.BoolProperty(default=True)
    show_gizmo_light_look_at : bpy.props.BoolProperty(default=True)
    show_gizmo_camera_lens : bpy.props.BoolProperty(default=True)
    show_gizmo_camera_dof_distance : bpy.props.BoolProperty(default=True)

    show_overlays: bpy.props.BoolProperty(default=True)
    show_ortho_grid: bpy.props.BoolProperty(default=True)
    show_floor: bpy.props.BoolProperty(default=True)
    show_axis_x: bpy.props.BoolProperty(default=True)
    show_axis_y: bpy.props.BoolProperty(default=True)
    show_axis_z: bpy.props.BoolProperty(default=True)
    grid_scale: bpy.props.FloatProperty(default=1.0)
    grid_subdivisions: bpy.props.IntProperty(default=10)
    show_text: bpy.props.BoolProperty(default=True)
    show_cursor: bpy.props.BoolProperty(default=True)
    show_annotation: bpy.props.BoolProperty(default=True)
    show_extras: bpy.props.BoolProperty(default=True)
    show_relationship_lines: bpy.props.BoolProperty(default=True)
    show_outline_selected: bpy.props.BoolProperty(default=True)
    show_bones: bpy.props.BoolProperty(default=True)
    show_motion_paths: bpy.props.BoolProperty(default=True)
    show_object_origins: bpy.props.BoolProperty(default=True)
    show_object_origins_all: bpy.props.BoolProperty(default=True)
    show_wireframes: bpy.props.BoolProperty(default=True)
    wireframe_threshold: bpy.props.FloatProperty(default=1.0)
    show_face_orientation: bpy.props.BoolProperty(default=True)
    show_reconstruction: bpy.props.BoolProperty(default=True)

    light: bpy.props.StringProperty()
    color_type: bpy.props.StringProperty()
    wireframe_color_type: bpy.props.StringProperty()
    background_type: bpy.props.StringProperty()
    background_color: bpy.props.FloatVectorProperty(subtype='COLOR', default=[0.0,0.0,0.0])
    show_backface_culling: bpy.props.BoolProperty(default=True)
    show_xray: bpy.props.BoolProperty(default=True)
    xray_alpha: bpy.props.FloatProperty()
    show_xray_wireframe: bpy.props.BoolProperty(default=True)
    xray_alpha_wireframe: bpy.props.FloatProperty()
    show_shadows: bpy.props.BoolProperty(default=True)
    shadow_intensity: bpy.props.FloatProperty()
    show_cavity: bpy.props.BoolProperty(default=True)
    cavity_type: bpy.props.StringProperty()
    curvature_ridge_factor: bpy.props.FloatProperty()
    curvature_valley_factor:bpy.props.FloatProperty()
    cavity_ridge_factor: bpy.props.FloatProperty()
    cavity_valley_factor:bpy.props.FloatProperty()
    use_dof:bpy.props.BoolProperty(default=True)
    show_object_outline:bpy.props.BoolProperty(default=True)
    object_outline_color : bpy.props.FloatVectorProperty(subtype='COLOR', default=[0.0,0.0,0.0])
    show_specular_highlight: bpy.props.BoolProperty(default=True)
    use_scene_lights:bpy.props.BoolProperty(default=True)
    use_scene_world: bpy.props.BoolProperty(default=True)


class ViewportPresetsAddonPreferences(AddonPreferences):
    bl_idname = __package__

    presets: CollectionProperty(type=ViewportPreset)
    selected_index: bpy.props.IntProperty()

    def draw(self, context):
        layout = self.layout
        
        layout.prop(self, "presets")

def register():
    bpy.utils.register_class(ViewportPreset)
    bpy.utils.register_class(ViewportPresetsAddonPreferences)

    prefs = bpy.context.preferences.addons[__package__].preferences

    # one = prefs.presets.add()
    # one.name = "First"
    # one.show_gizmo = True
    # one.show_overlays = False
    # two = prefs.presets.add()
    # two.name = "Second"
    # two.show_gizmo = False
    # two.show_overlays = True

    # two.show_ortho_grid = False
    # two.show_floor = True
    # two.show_axis_x = False
    # two.show_axis_y = False
    # two.show_axis_z = False
    # two.grid_scale = 0.5
    # two.grid_subdivisions = 30
    # two.show_text = False
    # two.show_cursor = True
    # two.show_annotation = False
    # two.show_extras = False
    # two.show_relationship_lines = True
    # two.show_outline_selected = False
    # two.show_bones = True
    # two.show_motion_paths = True
    # two.show_object_origins = True
    # two.show_object_origins_all = False
    # two.show_wireframes = True
    # two.wireframe_threshold = 0.33
    # two.show_face_orientation = True
    # two.show_reconstruction = True


def unregister():
    bpy.utils.unregister_class(ViewportPresetsAddonPreferences)
    bpy.utils.unregister_class(ViewportPreset)