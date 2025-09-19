# ComfyUI-AF-EditGeneratedPrompt
A ComfyUI custom node that allows you to pipe a generated prompt and either pass it as is, or copy and edit it manually. Or you can use the lower input field like any regular text input filed. The content of the lower text field will always dominate the output of the node.

## Features
- Display generated prompts in a read-only field
- Copy button for easy editing
- Prioritizes manual edits over original input
- Clean, user-friendly interface

<img width="1395" height="909" alt="image" src="https://github.com/user-attachments/assets/29e381f1-e4e4-4e65-b798-4bc6635102b6" />

## Installation
### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "AF - Edit Generated Prompt"
3. Install

### Manual Installation
1. Clone this repository into your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/yourusername/ComfyUI-AF-EditGeneratedPrompt.git

## Usage
1. Add the "AF - Edit Generated Prompt" node to your workflow
2. Connect a text input to the input_text input
3. After running the workflow, the generated prompt will be displayed in the readonly field
4. Use the "Copy Generated Prompt to Edit it" button to copy to the editable field
5. Edit as needed - the edited version will be output if present, otherwise the generated prompt will be used

## Version History
v0.0.16 - Put the version number and infos into the main python file, in the hopes of it showing up in the ComfyUI Manager
v0.0.15 - Fixed an issue with LiteGraph throwing an error about the space widgets
v0.0.14 - Inital Git Release
v0.0.01 - 0.0.13 Internal dev versions. Too many changes to list

## Disclaimer
This custom node was written with the help of AI.
