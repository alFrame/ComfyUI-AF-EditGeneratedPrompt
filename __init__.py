"""
@author: Alex Furer
@title: AF - Edit Generated Prompt
@nickname: AF - Edit Generated Prompt
@description: A ComfyUI custom node that allows you to pipe a generated prompt and either pass it as is, or copy and edit it manually.
"""

from .AF_Edit_Generated_Prompt import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

__version__ = "0.0.17"
__author__ = "Alex Furer"
__title__ = "AF - Edit Generated Prompt"
__description__ = "A ComfyUI custom node that allows you to pipe a generated prompt and either pass it as is, or copy and edit it manually."
__license__ = "MIT"
__changelog__ = [
    "v0.0.17 - Updated the init.py and modified the README",
    "v0.0.16 - Reorganized metadata to follow ComfyUI standards",
    "v0.0.15 - Fixed an issue with LiteGraph throwing an error about the spacer widgets",
    "v0.0.14 - Initial Git Release",
    "v0.0.01 - 0.0.13 Internal dev versions. Too many changes to list."
]

print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")
print(r"""
   ___   ____        _____           ___     __  ______  _  __       __      
  / _ | / __/ ____  / ___/__  __ _  / _/_ __/ / / /  _/ / |/ /__ ___/ /__ ___
 / __ |/ _/  /___/ / /__/ _ \/  ' \/ _/ // / /_/ // /  /    / _ Y _  / -_|_-
/_/ |_/_/          \___/\___/_/_/_/_/ \_, /\____/___/ /_/|_/\___|_,_/\__/___/
                                     /___/
                                     
                       🥃 AF - Edit Generated Prompt !
                 
""")
print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")