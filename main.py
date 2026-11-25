#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene — one scene, two lines."""
import os

LINE = "Sunday lunch, and my grandmother finally lets me stir the rendang — three generations around one stove, the youngest one in charge, the oldest one pretending not to watch."
assert 1 <= len(LINE) <= 280, "entry must be 1-280 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
