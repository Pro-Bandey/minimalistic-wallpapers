import os
import json
import time

# --- CONFIGURATION ---
IMAGE_DIR = "Img"  # Your main image folder
OUTPUT_FILE = "list.json"
EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.avif')

def generate_manifest():
    image_list = []
    
    print(f"Scanning {IMAGE_DIR} for images...")

    for root, dirs, files in os.walk(IMAGE_DIR):
        for file in files:
            if file.lower().endswith(EXTENSIONS):
                file_path = os.path.join(root, file)
                
                # Get file statistics
                stats = os.stat(file_path)
                
                image_data = {
                    "name": file,
                    "path": file_path.replace("\\", "/"), # Ensure web-friendly slashes
                    "size": stats.st_size,
                    "date": int(stats.st_mtime) # Unix timestamp
                }
                image_list.append(image_data)
                print(f"Added: {file}")

    # Sort by date descending (newest first) by default
    image_list.sort(key=lambda x: x['date'], reverse=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(image_list, f, indent=2)

    print(f"\nSuccess! {len(image_list)} images saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_manifest()
