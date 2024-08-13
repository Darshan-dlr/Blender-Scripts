"""
Blender Object Data Saver

This script defines functions to list and retrieve data about objects in a Blender scene, categorized by type.

Features:
- List objects in the scene based on their type (e.g., meshes, materials, curves).
- Retrieve detailed data about individual objects.

Author: Darshan D
Date: 2024-05-22

Usage:
- Run this script within Blender to list and retrieve data about objects in the scene.

Example:
    object_type = ObjectType.CAMERA
    objects = list_objects_by_type(object_type)
    for obj in objects:
        print(obj)
"""

import bpy
from enum import Enum
from typing import Dict, Any, List

class ObjectType(Enum):
    MESH = 'MESH'
    MATERIAL = 'MATERIAL'
    CURVE = 'CURVE'
    CAMERA = 'CAMERA'
    LIGHT = 'LIGHT'
    IMAGE = 'IMAGE'


def list_objects_by_type(object_type: ObjectType) -> List[str]:
    """
    List all objects in the Blender scene by their type.

    :param object_type: The type of objects to list (e.g., ObjectType.MESH, ObjectType.MATERIAL).
    :return: A list of object names of the specified type.
    """
    if object_type == ObjectType.MATERIAL:
        return [mat.name for mat in bpy.data.materials]
    elif object_type == ObjectType.MESH:
        return [obj.name for obj in bpy.data.objects if obj.type == 'MESH']
    elif object_type == ObjectType.CURVE:
        return [curve.name for curve in bpy.data.curves]
    elif object_type == ObjectType.CAMERA:
        return [cam.name for cam in bpy.data.cameras]
    elif object_type == ObjectType.LIGHT:
        return [light.name for light in bpy.data.lights]
    elif object_type == ObjectType.IMAGE:
        return [image.name for image in bpy.data.images]
    else:
        return f"Object type '{object_type.name}' is not supported."

if __name__ == "__main__":
    object_type = ObjectType.CAMERA  
    objects = list_objects_by_type(object_type)
    
    print(f"Listing {object_type.name.lower()} objects:")
    for obj in objects:
        print(obj)
