#!/usr/bin/env python3
"""
BW16 Specter Beta — Flasher Build Script
==========================================
Reads compiled .bin files from the firmware/ directory and injects them
as base64 into index_template.html, producing index.html.

Usage:
    python3 generate_flasher.py
"""

import base64
import os
import sys

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
FIRMWARE_DIR = os.path.join(SCRIPT_DIR, "firmware")
TEMPLATE     = os.path.join(SCRIPT_DIR, "index_template.html")
OUTPUT       = os.path.join(SCRIPT_DIR, "index.html")

FILES = {
    "PLACEHOLDER_FLASHLOADER": "imgtool_flashloader_amebad.bin",
    "PLACEHOLDER_KM0_BOOT":    "km0_boot_all.bin",
    "PLACEHOLDER_KM4_BOOT":    "km4_boot_all.bin",
    "PLACEHOLDER_APP":         "km0_km4_image2.bin",
}

def read_b64(filename):
    path = os.path.join(FIRMWARE_DIR, filename)
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("ascii")
    print(f"  [{filename}]  {len(data):>9,} bytes  →  {len(b64):>9,} base64 chars")
    return b64

def main():
    print("\n╔══════════════════════════════════════╗")
    print("║   BW16 Specter Beta — Flasher Build  ║")
    print("╚══════════════════════════════════════╝\n")

    if not os.path.exists(TEMPLATE):
        print(f"ERROR: Template not found: {TEMPLATE}")
        sys.exit(1)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        html = f.read()

    errors = []
    print("Encoding firmware files:")

    for placeholder, filename in FILES.items():
        b64 = read_b64(filename)
        if b64 is None:
            errors.append(filename)
            print(f"  [MISSING]  {filename}")
        else:
            html = html.replace(f'"{placeholder}"', f'"{b64}"')

    if errors:
        print("\n❌  Build FAILED — missing required binaries:")
        for f in errors:
            print(f"     firmware/{f}")
        sys.exit(1)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(html)

    # Verify decoded byte size
    import re
    m = re.search(r'app:\s*\"([^\"]+)\"', html)
    if m:
        decoded_len = len(base64.b64decode(m.group(1)))
        print(f"\n✅  VERIFIED DECODED APP SIZE: {decoded_len:,} bytes")

    size_kb = os.path.getsize(OUTPUT) / 1024
    print(f"\n✅  Build complete! Generated index.html ({size_kb:,.1f} KB).\n")

if __name__ == "__main__":
    main()
