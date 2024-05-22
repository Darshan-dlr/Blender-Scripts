"""
Blender addon for exporting models to specified formats like .obj, .fbx.

Author: Darshan D
Date: 2024-05-22

Usage:
- Install the addon in Blender.
- To export a model, go to File > Export > Export Model.
- Choose the desired file format from the dropdown menu and specify the file path.
- Click "Export" to save the model in the selected format.
"""

import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, EnumProperty
from bpy.types import Operator, Context
from typing import Any, Dict

class ExportModel(Operator, ExportHelper):
    bl_idname = "export.model"
    bl_label = "Export Model"
    bl_description = "Export model to specified format"
    
    filename_ext = ".obj" 

    file_format: EnumProperty(name="File Format",
                              items=[
                                ('.obj', "Wavefront OBJ", "Export as Wavefront OBJ format"),
                                ('.fbx', "FBX", "Export as FBX format")
                            ],
                            default='.obj'
                        )

    def execute(self, context: Context) -> Dict[str, Any]:
        """
        Execute the export operation.
        
        :return: {'FINISHED'} if successful.
        :rtype: Dict[str, Any]
        """
        filepath_split = self.filepath.rsplit('.',1)
        if len(filepath_split) > 1:
            filepath, file_extension = filepath_split
        if file_extension != self.file_format:
            filepath += self.file_format
        
        if self.file_format == '.obj':
            self.filename_ext = '.obj'
            bpy.ops.wm.obj_export(
                filepath=filepath,
                export_selected_objects=True
            )
        elif self.file_format == '.fbx':
            self.filename_ext = '.fbx'
            bpy.ops.export_scene.fbx(
                filepath=filepath,
                use_selection=True
            )
        return {'FINISHED'}

def menu_func(self, context: Context):
    """
    Add the export model option to the file export menu.
    
    :param self: The operator.
    :param context: The Blender context.
    """
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(ExportModel.bl_idname, text="Export Model")

def register():
    """
    Register the ExportModel addon.
    """
    bpy.utils.register_class(ExportModel)
    bpy.types.TOPBAR_MT_file_export.append(menu_func)

def unregister():
    """
    Unregister the ExportModel addon.
    """
    bpy.utils.unregister_class(ExportModel)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func)

if __name__ == "__main__":
    register()
