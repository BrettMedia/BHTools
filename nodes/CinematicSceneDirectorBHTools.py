import random

OUTPUT_NODE = True

class CinematicSceneDirectorBHTools:
    @classmethod
    def INPUT_TYPES(cls):
        # Logical grouping of inputs. The most-used options are at the top.
        return {
            "optional": {
                # Group 1: Primary Inputs
                "trigger_word": ("STRING", {"default": "", "multiline": True}),
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "preset_override": (
                    [
                        "None",
                        "Cinematic Drama",
                        "Sunny Landscape",
                        "Noir Urban",
                        "Fantasy Epic",
                        "Sci-Fi Futuristic",
                        "Romantic Dream",
                        "Horror Mystery",
                        "Vintage Nostalgia",
                        "Action Thrill",
                        "Comedy Bright",
                        "Cyberpunk Edge",
                        "Minimalist Chic",
                        "Surreal Wonderland",
                        "Mystery Noir",
                        "Urban Dystopia",
                        "Epic Adventure",
                        "Mystic Fantasy",
                        "Moody Twilight",
                        "Vibrant Festival",
                        "Golden Hour Glow",
                        "Icy Wonderland",
                        "Rustic Charm",
                        "Urban Jungle",
                        "Dreamy Pastel",
                        "Futuristic Minimalism",
                        "POV Drama",
                        "Profile Intensity",
                        "Cinematic Quality"
                    ],
                    {"default": "None"}
                ),

                # Group 2: Composition / Camera Perspective
                "shot_type": (
                    [
                        "None",
                        "Extreme Close-Up",
                        "Close-Up",
                        "Medium Close-Up",
                        "Medium Shot",
                        "Cowboy Shot",
                        "Medium Full Shot",
                        "Full Shot",
                        "Wide Shot",
                        "Establishing Shot"
                    ],
                    {"default": "None"}
                ),
                "shot_type_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "camera_angle": (
                    [
                        "None",
                        "Eye-Level",
                        "Low-Angle",
                        "High-Angle",
                        "Dutch Angle",
                        "Overhead",
                        "Bird's Eye View",
                        "Worm's Eye View"
                    ],
                    {"default": "None"}
                ),
                "camera_angle_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "viewpoint": (
                    [
                        "None",
                        "POV",
                        "Over-the-Shoulder",
                        "Profile",
                        "Side",
                        "Front"
                    ],
                    {"default": "None"}
                ),
                "viewpoint_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "camera_movement": (
                    [
                        "None",
                        "Static",
                        "Pan",
                        "Tilt",
                        "Dolly",
                        "Zoom",
                        "Handheld",
                        "Steadicam",
                        "Tracking Shot",
                        "Crane"
                    ],
                    {"default": "None"}
                ),
                "camera_movement_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                # Group 3: Camera Details
                "focus_depth": (
                    [
                        "None",
                        "Shallow Depth of Field",
                        "Deep Focus",
                        "Soft Focus",
                        "Tilt-Shift",
                        "Selective Focus"
                    ],
                    {"default": "None"}
                ),
                "focus_depth_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "depth_of_field_focus": (
                    [
                        "None",
                        "Crisp subject isolation",
                        "High bokeh",
                        "Exaggerated blur",
                        "Balanced focus",
                        "Soft background"
                    ],
                    {"default": "None"}
                ),
                "depth_of_field_focus_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "camera_lens": (
                    [
                        "None",
                        "Wide-Angle",
                        "Telephoto",
                        "Macro",
                        "Fisheye",
                        "Zoom lens"
                    ],
                    {"default": "None"}
                ),
                "camera_lens_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                # Group 4: Style & Mood / Lighting
                "art_style": (
                    [
                        "None",
                        "Realistic",
                        "Abstract",
                        "Animated",
                        "Digital",
                        "Surreal",
                        "Cinematic",
                        "Impressionistic",
                        "Expressionistic"
                    ],
                    {"default": "None"}
                ),
                "art_style_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "lighting": (
                    [
                        "None",
                        "Natural",
                        "Dramatic",
                        "Soft",
                        "High-Contrast",
                        "Ambient",
                        "Harsh",
                        "Spotlight"
                    ],
                    {"default": "None"}
                ),
                "lighting_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "directional_lighting": (
                    [
                        "None",
                        "Front Lighting",
                        "Side Lighting",
                        "Back Lighting",
                        "Top Lighting",
                        "Bottom Lighting",
                        "Oblique Lighting"
                    ],
                    {"default": "None"}
                ),
                "directional_lighting_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "time_of_day": (
                    [
                        "None",
                        "Morning",
                        "Afternoon",
                        "Evening",
                        "Night",
                        "Golden Hour",
                        "Blue Hour"
                    ],
                    {"default": "None"}
                ),
                "time_of_day_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "environment": (
                    [
                        "None",
                        "Interior",
                        "Exterior",
                        "Urban",
                        "Rural",
                        "Wilderness",
                        "Underwater",
                        "Space"
                    ],
                    {"default": "None"}
                ),
                "environment_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "genre": (
                    [
                        "None",
                        "Modern",
                        "Classic",
                        "Fantasy",
                        "Horror",
                        "Sci-Fi",
                        "Cyberpunk",
                        "Action",
                        "Steampunk",
                        "Romantic",
                        "Mystery",
                        "Western"
                    ],
                    {"default": "None"}
                ),
                "genre_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "mood": (
                    [
                        "None",
                        "Melancholic",
                        "Joyful",
                        "Serene",
                        "Tense",
                        "Mysterious",
                        "Energetic",
                        "Romantic",
                        "Angsty",
                        "Whimsical",
                        "Foreboding"
                    ],
                    {"default": "None"}
                ),
                "mood_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                # Group 5: Aesthetics / Color
                "color_palette": (
                    [
                        "None",
                        "Vibrant",
                        "Muted",
                        "Monochrome",
                        "Pastel",
                        "High Saturation",
                        "Earth Tones",
                        "Neon"
                    ],
                    {"default": "None"}
                ),
                "color_palette_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "film_grain": (
                    [
                        "None",
                        "Light Grain",
                        "Heavy Grain",
                        "Minimal Grain"
                    ],
                    {"default": "None"}
                ),
                "film_grain_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "atmosphere": (
                    [
                        "None",
                        "Fog",
                        "Mist",
                        "Cloudy",
                        "Overcast",
                        "Sunny",
                        "Moonlit",
                        "Stormy",
                        "Rainy",
                        "Snowy",
                        "Dusty",
                        "Hazy",
                        "Smoky"
                    ],
                    {"default": "None"}
                ),
                "atmosphere_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                # Group 6: Technical (only Quality remains)
                "quality": (
                    [
                        "None",
                        "Standard",
                        "Standard 8K",
                        "Standard Vector",
                        "High",
                        "High 8K",
                        "High Vector",
                        "Ultra",
                        "Ultra 8K",
                        "Ultra Vector",
                        "Cinematic",
                        "Cinematic 8K",
                        "Cinematic Vector",
                        "Highest Quality",
                        "Highest Quality 8K",
                        "Highest Quality Vector"
                    ],
                    {"default": "None"}
                ),
                "quality_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                # Group 7: Post Production Finishes
                "lens_effects": (
                    [
                        "None",
                        "Lens Flare",
                        "Cinematic Bloom",
                        "High Contrast",
                        "Glare",
                        "Prismatic Effect"
                    ],
                    {"default": "None"}
                ),
                "lens_effects_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "color_tone": (
                    [
                        "None",
                        "HDR",
                        "Vignette",
                        "Matte Finish",
                        "Color Graded",
                        "Black and White",
                        "Noir",
                        "Vintage Film Look",
                        "Sepia",
                        "Cool Tone",
                        "Warm Tone"
                    ],
                    {"default": "None"}
                ),
                "color_tone_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"}),

                "artistic_effect": (
                    [
                        "None",
                        "Diffusion",
                        "Ethereal Glow",
                        "Impressionistic",
                        "Surreal Filter",
                        "Grunge Texture"
                    ],
                    {"default": "None"}
                ),
                "artistic_effect_weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.1, "ui": "arrow"})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt_string"
    CATEGORY = "BH Tools🎬"

    # Helper: Format a value with its weight.
    def weighted_format(self, value, weight):
        if value == "None" or not value.strip():
            return None
        value = value.lower()
        rounded_weight = round(weight, 1)
        if rounded_weight == 1.0:
            return value
        else:
            return f"[{value}:{rounded_weight}]"

    def format_setting(self, value, weight, prefix="", suffix=""):
        formatted = self.weighted_format(value, weight)
        if formatted is None:
            return None
        return f"{prefix}{formatted}{suffix}"

    def generate_prompt_string(
        self,
        # Group 1: Primary Inputs
        trigger_word="",
        prompt="",
        preset_override="None",
        # Group 2: Composition / Camera Perspective
        shot_type="None",
        shot_type_weight=1.0,
        camera_angle="None",
        camera_angle_weight=1.0,
        viewpoint="None",
        viewpoint_weight=1.0,
        camera_movement="None",
        camera_movement_weight=1.0,
        # Group 3: Camera Details
        focus_depth="None",
        focus_depth_weight=1.0,
        depth_of_field_focus="None",
        depth_of_field_focus_weight=1.0,
        camera_lens="None",
        camera_lens_weight=1.0,
        # Group 4: Style & Mood / Lighting
        art_style="None",
        art_style_weight=1.0,
        lighting="None",
        lighting_weight=1.0,
        directional_lighting="None",
        directional_lighting_weight=1.0,
        time_of_day="None",
        time_of_day_weight=1.0,
        environment="None",
        environment_weight=1.0,
        genre="None",
        genre_weight=1.0,
        mood="None",
        mood_weight=1.0,
        # Group 5: Aesthetics / Color
        color_palette="None",
        color_palette_weight=1.0,
        film_grain="None",
        film_grain_weight=1.0,
        atmosphere="None",
        atmosphere_weight=1.0,
        # Group 6: Technical (Quality Only)
        quality="None",
        quality_weight=1.0,
        # Group 7: Post Production Finishes
        lens_effects="None",
        lens_effects_weight=1.0,
        color_tone="None",
        color_tone_weight=1.0,
        artistic_effect="None",
        artistic_effect_weight=1.0
    ):
        """
        Constructs a detailed cinematic scene prompt by combining inputs from logical groups:
        
        • Primary (trigger, prompt, preset)
        • Composition / Camera Perspective (shot type, camera angle, viewpoint, camera movement)
        • Camera Details (focus depth, depth of field, camera lens)
        • Style & Mood (art style, lighting, time of day, environment, genre, mood)
        • Aesthetics (color palette, film grain, atmosphere)
        • Technical (quality)
        • Post Production Finishes (lens effects, color tone, artistic effect)
        """
        plain_trigger = trigger_word.strip()
        plain_prompt = prompt.strip()
        if plain_trigger and not plain_trigger.endswith(","):
            plain_trigger += ","
        if plain_prompt and not plain_prompt.endswith(","):
            plain_prompt += ","
    
        # Preset definitions pulled from director’s dictionaries.
        PRESETS = {
            "Cinematic Drama": "a visually striking cinematic scene with deep shadows, rich contrast, and dynamic composition",
            "Sunny Landscape": "a radiant outdoor scene with brilliant sunlight, expansive skies, and vibrant colors",
            "Noir Urban": "a moody urban nightscape with stark shadows and intriguing light contrasts",
            "Fantasy Epic": "an epic fantasy scene bursting with magical elements, surreal lighting, and imaginative vistas",
            "Sci-Fi Futuristic": "a futuristic digital scene with sleek elements, neon highlights, and advanced technology",
            "Romantic Dream": "a soft, dreamy ambiance filled with pastel hues, gentle lighting, and a romantic glow",
            "Horror Mystery": "a chilling, mysterious scene with eerie shadows, unsettling textures, and high contrast lighting",
            "Vintage Nostalgia": "a timeless scene with muted colors, nostalgic film grain, and retro charm",
            "Action Thrill": "a high-energy scene with bold movement, rapid action, and dramatic lighting",
            "Comedy Bright": "a lively, playful scene overflowing with vibrant energy and cheerful hues",
            "Cyberpunk Edge": "a neon-drenched urban scene with cybernetic elements, futuristic grit, and edgy aesthetics",
            "Minimalist Chic": "a clean, minimalist scene with crisp lines, subtle tones, and modern simplicity",
            "Surreal Wonderland": "a bizarre, dreamlike scene with exaggerated perspectives and whimsical details",
            "Mystery Noir": "a suspenseful, shadowy scene with moody contrasts and enigmatic ambiance",
            "Urban Dystopia": "a bleak urban landscape marked by gritty decay and dystopian overtones",
            "Epic Adventure": "a grandiose scene with sweeping vistas and dynamic energy",
            "Mystic Fantasy": "a magical realm alive with mystical elements, vibrant colors, and enchanting light",
            "Moody Twilight": "a somber twilight scene with deep blues, soft ambient glow, and introspective mood",
            "Vibrant Festival": "an exuberant celebration scene with bold colors and festive energy",
            "Golden Hour Glow": "a warm scene bathed in the soft, magical light of golden hour",
            "Icy Wonderland": "a crisp, ethereal winter scene with sparkling ice formations and cool tones",
            "Rustic Charm": "a quaint, rustic scene with earthy textures and timeless appeal",
            "Urban Jungle": "a striking blend of urban grit and untamed nature",
            "Dreamy Pastel": "a delicate scene with soft pastel hues and a tranquil vibe",
            "Futuristic Minimalism": "a sleek, ultra-modern scene defined by minimalistic design and futuristic tech",
            "POV Drama": "a dynamic point-of-view scene with immersive perspective and dramatic angles",
            "Profile Intensity": "a focused scene that highlights a compelling profile shot with intense character expression",
            "Cinematic Quality": "a scene rendered in ultra-high cinematic quality boasting pristine detail and luminous clarity"
        }
    
        # Group 2: Composition / Camera Perspective
        comp_parts = []
        s = self.format_setting(shot_type, shot_type_weight, "", " shot")
        if s: comp_parts.append(s)
        s = self.format_setting(camera_angle, camera_angle_weight, "from a ", " perspective")
        if s: comp_parts.append(s)
        s = self.format_setting(viewpoint, viewpoint_weight, "featuring ", " viewpoint")
        if s: comp_parts.append(s)
        s = self.format_setting(camera_movement, camera_movement_weight, "captured using ", " movement")
        if s: comp_parts.append(s)
    
        # Group 3: Camera Details
        cam_parts = []
        s = self.format_setting(focus_depth, focus_depth_weight, "with ", "")
        if s: cam_parts.append(s)
        s = self.format_setting(depth_of_field_focus, depth_of_field_focus_weight, "featuring ", " depth of field")
        if s: cam_parts.append(s)
        s = self.format_setting(camera_lens, camera_lens_weight, "shot with a ", " lens")
        if s: cam_parts.append(s)
    
        # Group 4: Style & Mood / Lighting
        style_parts = []
        s = self.format_setting(art_style, art_style_weight, "in a ", " style")
        if s: style_parts.append(s)
        # Combine lighting and directional lighting.
        lighting_phrase = ""
        if lighting != "None" and directional_lighting != "None":
            l = self.format_setting(lighting, lighting_weight, "", "")
            dl = self.format_setting(directional_lighting, directional_lighting_weight, "", "")
            if l and dl:
                lighting_phrase = f"illuminated by {l} lighting with {dl} direction"
        elif lighting != "None":
            l = self.format_setting(lighting, lighting_weight, "", "")
            if l: lighting_phrase = f"illuminated by {l} lighting"
        elif directional_lighting != "None":
            dl = self.format_setting(directional_lighting, directional_lighting_weight, "", "")
            if dl: lighting_phrase = f"with {dl} lighting"
        if lighting_phrase: style_parts.append(lighting_phrase)
        s = self.format_setting(time_of_day, time_of_day_weight, "during ", " hours")
        if s: style_parts.append(s)
        s = self.format_setting(environment, environment_weight, "set in a ", " environment")
        if s: style_parts.append(s)
        s = self.format_setting(genre, genre_weight, "evoking ", " vibes")
        if s: style_parts.append(s)
        s = self.format_setting(mood, mood_weight, "with a ", " mood")
        if s: style_parts.append(s)
    
        # Group 5: Aesthetics / Color
        aesthetic_parts = []
        s = self.format_setting(color_palette, color_palette_weight, "in a ", " color palette")
        if s: aesthetic_parts.append(s)
        s = self.format_setting(film_grain, film_grain_weight, "with ", " film grain")
        if s: aesthetic_parts.append(s)
        s = self.format_setting(atmosphere, atmosphere_weight, "with an ", " atmosphere")
        if s: aesthetic_parts.append(s)
    
        # Assemble all descriptive parts from groups 2 - 5.
        group_parts = comp_parts + cam_parts + style_parts + aesthetic_parts
        individual_desc = ", ".join(group_parts)
    
        # Apply preset override if set.
        if preset_override != "None":
            preset_desc = PRESETS.get(preset_override, "")
            if individual_desc:
                plain_scene_description = f"{preset_desc}, {individual_desc}"
            else:
                plain_scene_description = preset_desc
        else:
            plain_scene_description = individual_desc
    
        # Group 6: Technical (Quality Only)
        tech_info = []
        if quality != "None":
            quality_text = self.format_setting(quality, quality_weight, "rendered in ", " quality")
            if quality_text:
                tech_info.append(quality_text)
        tech_info_text = ""
        if tech_info:
            tech_info_text = ", " + ", ".join(tech_info)
    
        # Group 7: Post Production Finishes.
        pp_parts = []
        s = self.format_setting(lens_effects, lens_effects_weight, "", "")
        if s: pp_parts.append(s)
        s = self.format_setting(color_tone, color_tone_weight, "", "")
        if s: pp_parts.append(s)
        s = self.format_setting(artistic_effect, artistic_effect_weight, "", "")
        if s: pp_parts.append(s)
        pp_text = ""
        if pp_parts:
            pp_text = ", " + ", ".join(pp_parts)
    
        # Assemble the final prompt.
        final_prompt = ""
        if plain_trigger:
            final_prompt += plain_trigger
        if plain_prompt:
            if final_prompt:
                final_prompt += "\n"
            final_prompt += plain_prompt
        if plain_scene_description or tech_info_text or pp_text:
            if final_prompt:
                final_prompt += "\n\n"
            final_prompt += plain_scene_description + tech_info_text + pp_text
    
        return {"ui": {"text": (final_prompt,)}, "result": (final_prompt,)}

NODE_CLASS_MAPPINGS = {
    "CinematicSceneDirectorBHTools": CinematicSceneDirectorBHTools
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CinematicSceneDirectorBHTools": "Cinematic Scene Director | BHTools🎬"
}
