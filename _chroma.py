#!/usr/bin/env python3
"""Tira o fundo chroma verde e deixa PNG com alpha + trim + resize."""
import sys
import numpy as np
from PIL import Image, ImageFilter

def cut(src, dst, max_side=1400):
    im = Image.open(src).convert("RGB")
    a = np.asarray(im).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]

    # quanto o pixel é "verde puro" (0 = nada, 1 = chroma cheio)
    spill = g - np.maximum(r, b)
    key = np.clip((spill - 10) / 60.0, 0, 1)          # rampa suave na borda
    alpha = (1.0 - key) * 255.0

    # despill: puxa o verde de volta pra média nas bordas
    mix = np.maximum(r, b)
    g2 = np.where(g > mix, mix + (g - mix) * (1 - key), g)
    out = np.dstack([r, g2, b, alpha]).astype(np.uint8)

    img = Image.fromarray(out, "RGBA")
    # suaviza 1px o alpha pra não serrilhar
    al = img.getchannel("A").filter(ImageFilter.GaussianBlur(0.6))
    img.putalpha(al)

    bbox = img.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    if bbox:
        pad = 12
        bbox = (max(0, bbox[0]-pad), max(0, bbox[1]-pad),
                min(img.width, bbox[2]+pad), min(img.height, bbox[3]+pad))
        img = img.crop(bbox)
    if max(img.size) > max_side:
        s = max_side / max(img.size)
        img = img.resize((int(img.width*s), int(img.height*s)), Image.LANCZOS)
    img.save(dst)
    print(f"{dst}  {img.size[0]}x{img.size[1]}")

if __name__ == "__main__":
    cut(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1400)
