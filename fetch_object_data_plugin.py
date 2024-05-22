"""
Blender Object Data Saver

This script defines an operator in Blender to save data about selected objects to a JSON file.

Author: Your Name
Date: 2024-05-22

Usage:
- Run this script within Blender to save data about selected objects to a JSON file.
"""

import bpy
import json
from typing import Dict, Any, List

def get_object_data(obj: bpy.types.Object) -> Dict[str, Any]:
    """
    Get data about the given Blender object.

    :param obj: Blender object
    :return: Dictionary containing object data
    """
    data = {
        "name": obj.name,
        "location": obj.location[:],
        "rotation": [round(angle, 2) for angle in obj.rotation_euler],
        "scale": obj.scale[:],
        "parent": obj.parent.name if obj.parent else None,
        "children_count": len(obj.children),
    }
    return data

def save_selected_objects_data(filepath: str) -> None:
    """
    Save data about selected Blender objects to a JSON file.

    :param filepath: Path to the JSON file
    """
    selected_objects = bpy.context.selected_objects
    data_to_save: List[Dict[str, Any]] = []
    for obj in selected_objects:
        obj_data = get_object_data(obj)
        data_to_save.append(obj_data)
    
    with open(filepath, 'w') as json_file:
        json.dump(data_to_save, json_file, indent=4)

class SaveObjectDataOperator(bpy.types.Operator):
    """
    Operator to save data about selected Blender objects to a JSON file.
    """
    bl_idname = "object.save_object_data"
    bl_label = "Save Object Data"
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH", description="Path to the JSON file")
    
    def execute(self, context: bpy.types.Context) -> Dict[str, Any]:
        """
        Execute the operator.

        :param context: Blender context
        :return: Dictionary with result of the execution
        """
        save_selected_objects_data(self.filepath)
        return {'FINISHED'}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> Dict[str, Any]:
        """
        Invoke the operator.

        :param context: Blender context
        :param event: Blender event
        :return: Dictionary with result of the invocation
        """
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def register() -> None:
    """
    Register the operator.
    """
    bpy.utils.register_class(SaveObjectDataOperator)

def unregister() -> None:
    """
    Unregister the operator.
    """
    bpy.utils.unregister_class(SaveObjectDataOperator)

if __name__ == "__main__":
    register()
