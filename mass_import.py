import os
import json
import datetime

# Directory settings
SOURCE_DIR = "./raw_scans"
OUTPUT_DIR = "./logs/2026-01"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SOURCE_DIR, exist_ok=True) # Ensure source exists

def mass_import():
    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.json')]
    if not files:
        print(f"⚠️ No .json files found in {SOURCE_DIR}. Place your raw twins there first!")
        return

    print(f"📦 Found {len(files)} twins to import...")

    for filename in files:
        with open(os.path.join(SOURCE_DIR, filename), 'r') as f:
            raw_data = json.load(f)
        
        digital_twin = {
            "detection_event": f"BATCH-{filename.split('.')[0]}",
            "spectral_calibration": "v2.1_20260107",
            "taxonomy": {
                "material": raw_data.get('material', 'Unknown'),
                "condition": raw_data.get('condition', 'Unknown'),
                "disposal": "Circular Economy"
            },
            "digital_twin_forecast": {
                "2076_outlook": "Persistent" if raw_data.get('material') == "Polymer" else "Stable",
                "environmental_impact_score": 8.5
            }
        }

        output_path = os.path.join(OUTPUT_DIR, f"twin_{filename}")
        with open(output_path, 'w') as out_f:
            json.dump(digital_twin, out_f, indent=2)

    print("✅ All twins processed and moved to logs.")

if __name__ == "__main__":
    mass_import()
