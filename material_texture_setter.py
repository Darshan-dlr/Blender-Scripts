"""
Material Texture Setter

This script automates texture assignment to Blender object materials. It creates a new material if needed and sets up nodes to incorporate the provided texture file.

Author: Darshan D
Date: 2024-05-21

Usage:
- Run this script within Blender to set a texture for the material of the active object.
"""

import bpy
import os


def set_material_texture(texture_path: str, material_name: str = "TextureMaterial") -> None:
    """
    Assigns a texture to the newly created material for the selected object

    :param texture_path: The full path to the texture file.
    :param material_name: The name of the new material.
    """
    if not os.path.isfile(texture_path):
        raise FileNotFoundError(f"Texture file not found: {texture_path}")

    new_material = bpy.data.materials.new(name=material_name)
    new_material.use_nodes = True

    texture_node = new_material.node_tree.nodes.new('ShaderNodeTexImage')
    texture_node.image = bpy.data.images.load(texture_path)

    bsdf_node = next((node for node in new_material.node_tree.nodes if node.type == 'BSDF_PRINCIPLED'), None)
    if bsdf_node is None:
        bsdf_node = new_material.node_tree.nodes.new('ShaderNodeBsdfPrincipled')

    new_material.node_tree.links.new(texture_node.outputs[0], bsdf_node.inputs[0])

    active_object = bpy.context.active_object
    if not active_object:
        raise RuntimeError("No object selected.")

    if not active_object.material_slots:
        bpy.ops.object.material_slot_add()

    active_object.material_slots[0].material = new_material


if __name__ == "__main__":
    texture_path = r"C:\Users\admin\Downloads\photo686.jpeg"
    set_material_texture(texture_path)
