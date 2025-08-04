"""
@author: Alex Furer
@title: AF - Edit Generated Prompt
@nickname: alFrame
@description: This custom node let's you pipe a generated prompt and either pass it as is, or copy and paste it to the lower text widget for editing. The lower one will be passed on, if there's text.
@version: v14
"""

#---------------------------------------------------------------------------------------------------------------------------------------------------#
# AF nodes are created by Alex Furer developed in 2025 with the help of QWEN3 and Claude AI                                                         #
# for ComfyUI                                                                                                                                       #
# Like the pack and want to support me?                                                                                                             #
#---------------------------------------------------------------------------------------------------------------------------------------------------#


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
    CATEGORY = "text/editing"
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