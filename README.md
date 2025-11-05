# LQR SceneScript Protocol (v0.2)

A text-based, AI-native protocol for visual communication using QR as a transport layer.

## 🧪 Demo: Animated Triangle

This repo contains a minimal SceneScript file that describes a red triangle with a translateY animation.

- Source: [`scene_triangle.scene`](scene_triangle.scene)
- Rendered SVG: (run `renderer_svg.py` to generate)
- LQR-Mini QR: (run `lqr_encoder.py` to generate)

## ▶ How to Use

1. Clone this repo
2. Run in Python:
   ```bash
   python renderer_svg.py > output.svg
   python lqr_encoder.py "https://github.com/yourname/lqr-scenescript" > qr.txt
