import bpy

# Define the operator to adjust X-Ray alpha and toggle X-Ray visibility
class AdjustXRayAlphaOperator(bpy.types.Operator):
    bl_idname = "preferences.adjust_xray_alpha"
    bl_label = "Adjust X-Ray Alpha"
    
    def execute(self, context):
        if context.space_data.shading.xray_alpha == 1.0:  # If xray_alpha is already 1
            context.space_data.shading.show_xray = not context.space_data.shading.show_xray # Toggle show_xray
        if context.space_data.shading.show_xray == True and context.space_data.shading.xray_alpha == 1.0:
            context.space_data.shading.xray_alpha = 0.5
        else:
            context.space_data.shading.xray_alpha = 1.0  # Set xray_alpha to 1
        return {'FINISHED'}

# Register the operator
def register_operator():
    bpy.utils.register_class(AdjustXRayAlphaOperator)

# Unregister the operator
def unregister_operator():
    bpy.utils.unregister_class(AdjustXRayAlphaOperator)

# Define the keymap item
addon_keymaps = []

def register_keymap():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("preferences.adjust_xray_alpha", 'Z', 'PRESS', ctrl=True, alt=True)
        addon_keymaps.append((km, kmi))

def unregister_keymap():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
        addon_keymaps.clear()

if __name__ == "__main__":
    register_operator()
    register_keymap()
