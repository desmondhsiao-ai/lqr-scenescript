import xml.etree.ElementTree as ET

def render_svg(parsed):
    scene = parsed["scene"]
    action = parsed["action"]
    
    svg = ET.Element('svg', width="200", height="200", xmlns="http://www.w3.org/2000/svg")
    poly = ET.SubElement(svg, 'polygon', points=scene["points"], fill=scene["fill"])
    
    if action.get("effect") == "translateY":
        value_px = action["value"].replace("px", "")
        anim = ET.SubElement(
            poly, 'animate',
            attributeName="y",
            from_="0", to=value_px,
            dur=action["duration"],
            fill="freeze"
        )
    
    return ET.tostring(svg, encoding='unicode')
