# BHTools 🎬

BHTools is a collection of custom tools and nodes designed to enhance creative workflows by merging traditional film, VFX, and animation techniques with innovative AI-driven methods. Developed by BrettMedia, these tools empower visual storytellers to generate cinematic prompts and streamline their production pipelines.

## Overview

BHTools integrates a suite of custom nodes that simplify the process of crafting detailed cinematic scene descriptions. Inspired by a passion for visual storytelling, these tools help you fine-tune parameters such as composition, camera angle, lighting, mood, and technical aesthetics.

## Custom Node: CinematicSceneDirectorBHTools

**CinematicSceneDirectorBHTools** is a highly flexible node within the BHTools collection. It generates comprehensive cinematic scene prompts through a range of optional inputs—ensuring you can tailor the output to your needs without being forced to fill every field.

### How It Works

- **Optional Input Fields:**  
  The node can process various input types, all of which are optional:
  - **Trigger Words (LORA-like Triggers):**  
    Use these to rapidly invoke thematic styles or moods via shortcut trigger words.
  - **Prompt Description:**  
    A text field where you describe your scene in detail. This free-form narrative forms the core of the creative prompt.
  - **Preset Override:**  
    Presets allow you to automatically apply a set of predefined parameters. These can complement the trigger words and description but are not required.

- **Parameter Weighting:**  
  Additional optional parameters outside the core text inputs include:
  - **Composition / Camera Perspective:**  
    Controls like shot type, angle, and movement are available.
  - **Camera Details:**  
    Adjustments for focus, depth-of-field, and lens specifics.
  - **Style, Mood & Lighting:**  
    Options for art style, time of day, lighting mood, and overall atmosphere.
  - **Aesthetic Adjustments:**  
    Fine-tuning settings for color palettes, film grain, and other visual effects.
  
  Each provided input is assigned a weighting that determines its influence on the final generated prompt. If an input is omitted, its associated weight drops to zero, allowing the node to default to preset values or ignore that parameter. This mechanism guarantees that even with minimal input—such as a simple trigger word—the final cinematic prompt remains coherent and visually compelling.

### Example Code

Below is a sample of how you might use the node within your project:

```python
# Example: Generate a cinematic scene prompt using the custom node
from cinematic_node import CinematicSceneDirectorBHTools

node = CinematicSceneDirectorBHTools()
result = node.generate_prompt(
    # All these fields are optional; fill in only what you need.
    trigger_word="Epic",              # LORA-like trigger word
    prompt="A breathtaking view of ancient ruins at sunrise",  # Narrative description
    preset_override="Epic Adventure", # Optional preset to apply default settings
    shot_type="Wide Shot",            # Optional composition parameter
    camera_angle="Eye-Level",         # Optional camera perspective
    lighting="Natural"                # Optional lighting parameter
)
print(result)
