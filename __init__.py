import os
from .AF_Edit_Generated_Prompt import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# Get the directory of this file
node_dir = os.path.dirname(__file__)
js_path = os.path.join(node_dir, "AF_Edit_Generated_Prompt.js")

# Tell ComfyUI to serve web files from this directory
WEB_DIRECTORY = "." if os.path.exists(js_path) else None

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']