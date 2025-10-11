# ****** ComfyUI-AF-EditGeneratedPrompt ******
#
# Creator: Alex Furer - Co-Creator(s): Qwen3 and Claude AI
#
# Description:
# A ComfyUI custom node that allows you to pipe a generated prompt and either pass it as is, or copy and edit it manually. Or you can use the lower input field like any regular text input filed. The content of the lower text field will always dominate the output of the node.
#
# Repo and ReadMe URL: https://github.com/alFrame/ComfyUI-AF-EditGeneratedPrompt
#
# Praise, comment, bugs, improvements: https://github.com/alFrame/ComfyUI-AF-EditGeneratedPrompt/issues
#
# LICENSE: MIT License
#
# v0.0.17
#
# Usage:
# Read Me on Github
#
# Changelog:
# "v0.0.17 - Updated the init.py and modified the README",
# "v0.0.16 - Reorganized metadata to follow ComfyUI standards",
# "v0.0.15 - Fixed an issue with LiteGraph throwing an error about the spacer widgets",
# "v0.0.14 - Initial Git Release",
# "v0.0.01 - 0.0.13 Internal dev versions. Too many changes to list."
#
# Feature Requests / Wet Dreams
# - Be able to access the "Copy Generated Prompt for Editing" button outside a subgraph.
# - Video

class AF_Edit_Generated_Prompt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "generated_prompt": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "readonly": True
                }),
                "manual_or_paste_generated": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            },
            "optional": {
                "input_text": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "forceInput": True
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "AF - Nodes"
    OUTPUT_NODE = False
    
    def process(self, generated_prompt="", manual_or_paste_generated="", input_text=""):
        # Handle None values by converting to empty strings
        generated_prompt = generated_prompt or ""
        manual_or_paste_generated = manual_or_paste_generated or ""
        input_text = input_text or ""
        
        # Determine output - NO ERROR THROWING, just return the manual text or input
        if manual_or_paste_generated.strip():
            output = manual_or_paste_generated
        elif input_text.strip():
            output = input_text
        else:
            # No prompt provided - return empty string to allow continuation
            output = ""
        
        # Send data to JavaScript extension
        display_text = input_text if input_text else "No input connected"
        
        return {
            "ui": {"generated_prompt": [str(display_text)]},
            "result": (output,)
        }

# These mappings MUST be at the end of the file
NODE_CLASS_MAPPINGS = {
    "AF_Edit_Generated_Prompt": AF_Edit_Generated_Prompt
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AF_Edit_Generated_Prompt": "AF - Edit Generated Prompt"

}

