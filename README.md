# ComfyUI-AF-EditGeneratedPrompt

A ComfyUI custom node that allows you to pipe a generated prompt into from an LLM and either pass it as is, or copy and edit it manually.

If you have a prompting AI assistant in your workflow, you can pipe the output of that into the "AF - Edit Generated Prompt" 'input_text' input and forward it to your CLIP Text Encode (Prompt) node.  

There are two text fields in this node.
- The upper one is the one that receives and displays the incoming prompt (slightly grayed out).
- The text field below is a regular prompt input text field. You can either write your own, or click the "Copy Generated Prompt to Edit it" button, which will copy the prompt to the lower text input filed, where you can edit it.  

The content of the lower text field will always dominate the output of the node. So if you leave it empty, the prompt above will be rendered.
	
---

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
	```

---

## ⚠️ Disclaimer

This ComfyUI custom node is developed through AI-assisted coding, prompted and directed by a human developer. While considerable care has been taken to ensure proper functionality, security, and compatibility, this software is provided **"as is" without warranty of any kind**, express or implied.

**By using this custom node, you acknowledge that:**
- You install and run this software at your own risk
- The creator is not liable for any damages, data loss, or issues arising from its use
- Compatibility with your specific setup is not guaranteed
- You should test thoroughly in a safe environment before production use

This node has been carefully designed and tested, but individual system configurations may vary. Please report any issues on the GitHub repository.

---

## Features
- Display generated prompts in a read-only field
- Copy button for easy editing
- Prioritizes manual edits over original input
- Clean, user-friendly interface

<img width="1395" height="909" alt="image" src="https://github.com/user-attachments/assets/29e381f1-e4e4-4e65-b798-4bc6635102b6" />

---

## Usage
1. Add the "AF - Edit Generated Prompt" node to your workflow
2. Connect a text input to the input_text input
3. After running the workflow, the generated prompt will be displayed in the readonly field
4. Use the "Copy Generated Prompt to Edit it" button to copy to the editable field
5. Edit as needed - the edited version will be output if present, otherwise the generated prompt will be used

