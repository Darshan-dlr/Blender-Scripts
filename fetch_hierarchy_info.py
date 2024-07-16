"""
Fetch Hierarchy Info

This script retrieves information about the hierarchy of objects in a Blender scene,
including the name of the root/main parent object and a list of names of all its children recursively.

Author: Darshan D
Date: 2024-05-21

Usage:
- Run this script within Blender to retrieve hierarchy information about the active object.
"""

import bpy
from typing import Optional, Tuple, List


def get_hierarchy_info(obj: bpy.types.Object) -> Tuple[Optional[str], List[str]]:
    """
    Returns the name of the root/main parent object and a list of names of all its children recursively.

    :param obj: The object for which to retrieve hierarchy information.
    :return: A tuple containing the root/main parent object's name (or None if no parent) and a list of all children's names.
    """
    if not obj:
        raise ValueError("No object provided.")

    def get_root_parent(obj: bpy.types.Object) -> Optional[str]:
        """
        Returns the name of the root/main parent object.

        :param obj: The object for which to retrieve the root/main parent.
        :return: The name of the root/main parent object (or None if no parent).
        """
        return get_root_parent(obj.parent) if obj.parent else obj.name
             
    
    parent_name = get_root_parent(obj)

    def recursive_get_children_names(obj: bpy.types.Object, children_list: List[str]) -> None:
        """
        Recursively collects the names of all children objects.

        :param obj: The current object whose children are to be retrieved.
        :param children_list: The list to store children object names.
        """
        for child in obj.children:
            children_list.append(child.name)
            recursive_get_children_names(child, children_list)
    
    all_children_names = []
    recursive_get_children_names(obj, all_children_names)
    
    return parent_name, all_children_names

def main() -> None:
    """
    Main function to execute the script.
    """
    if bpy.context.active_object:
        main_object: bpy.types.Object = bpy.context.active_object
        parent_name, all_children_names = get_hierarchy_info(main_object)
        
        print(f"Root/Main Parent Name: {parent_name}")
        print("Children Names:")
        for name in all_children_names:
            print(name)
    else:
        raise RuntimeError("No active object selected.")


if __name__ == "__main__":
    main()
