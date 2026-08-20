#!/usr/bin/env python3
"""Gerador de imagens da LP ESPUMA via Nano Banana 2 (gemini-3.1-flash-image-preview)."""
import base64, json, os, sys, urllib.request

KEY = os.environ.get("GEMINI_API_KEY")
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent"

def gen(prompt, out, ratio="1:1", temp=0.45):
    body = json.dumps({
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "candidateCount": 1,
            "temperature": temp,
            "imageConfig": {"aspectRatio": ratio},
        },
    }).encode()
    req = urllib.request.Request(URL, data=body, headers={
        "Content-Type": "application/json",
        "x-goog-api-key": KEY,
        "User-Agent": "lp-espuma/1.0",
    })
    try:
        resp = json.load(urllib.request.urlopen(req, timeout=180))
    except urllib.error.HTTPError as e:
        print(f"ERRO {out}: {e.code} {e.read()[:400].decode(errors='ignore')}")
        return False
    for part in resp["candidates"][0]["content"]["parts"]:
        if "inlineData" in part:
            open(out, "wb").write(base64.b64decode(part["inlineData"]["data"]))
            print(f"OK {out}")
            return True
    print(f"SEM IMAGEM {out}: {json.dumps(resp)[:300]}")
    return False

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    for item in spec:
        gen(item["prompt"], item["out"], item.get("ratio", "1:1"), item.get("temp", 0.45))
