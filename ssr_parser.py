def parse_scene_script(text):
    lines = [line.strip() for line in text.split('\n') if line.strip() and not line.startswith('#')]
    scene = {"shape": None, "points": None, "fill": "#000000"}
    action = {}
    
    current_block = None
    for line in lines:
        if line == "SCENE {":
            current_block = "scene"
        elif line == "ACTION {":
            current_block = "action"
        elif line == "META {":
            current_block = "meta"
        elif line == "}":
            current_block = None
        elif current_block == "scene":
            if ":" in line:
                key, val = line.split(":", 1)
                scene[key.strip()] = val.strip().strip('"')
        elif current_block == "action":
            if ":" in line:
                key, val = line.split(":", 1)
                action[key.strip()] = val.strip().strip('"')
    
    return {"scene": scene, "action": action}
