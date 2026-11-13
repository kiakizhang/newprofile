#!/usr/bin/env python3
import base64, pathlib

root = pathlib.Path(__file__).parent
tpl = (root / "template.html").read_text(encoding="utf-8")

images = {
    "__IMG_portrait__": ("assets/portrait.png", "image/png"),
    "__IMG_hackathon__": ("assets/hackathon.jpg", "image/jpeg"),
    "__IMG_ckj__": ("assets/ckj.jpg", "image/jpeg"),
    "__IMG_speech__": ("assets/speech.jpg", "image/jpeg"),
    "__IMG_visionpro__": ("assets/visionpro.jpg", "image/jpeg"),
    "__IMG_ry__": ("assets/ry.jpg", "image/jpeg"),
    "__IMG_AIcreators__": ("assets/AI-creators.jpg", "image/jpeg"),
    "__IMG_logo_mengma__": ("assets/logos/mengma.png", "image/png"),
    "__IMG_logo_tencent__": ("assets/logos/tencent.png", "image/png"),
    "__IMG_logo_weipai__": ("assets/logos/weipai.png", "image/png"),
    "__IMG_logo_presence__": ("assets/logos/presence.png", "image/png"),
}

for token, (rel, mime) in images.items():
    data = base64.b64encode((root / rel).read_bytes()).decode("ascii")
    tpl = tpl.replace(token, f"data:{mime};base64,{data}")

out = root / "index.html"
out.write_text(tpl, encoding="utf-8")
print(f"{out.name}: {out.stat().st_size/1024/1024:.2f} MB")
