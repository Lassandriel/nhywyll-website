import os

# Mapping of corrupted byte sequences to correct UTF-8 byte sequences
# We use bytes directly to avoid encoding/decoding issues in the script itself
replacements = {
    b'\xc3\xb0\xc5\xb8\xc5\x92\xe2\x84\xa2': '🌙'.encode('utf-8'), # ðŸŒ™ -> 🌙
    b'\xc3\x82\xc2\xb7': '·'.encode('utf-8'),                     # Â· -> ·
    b'\xc3\xa2\xe2\x80\xa0\xe2\x80\xb9': '↑'.encode('utf-8'),      # â†‘ -> ↑
    b'\xc3\xb0\xc5\xb8\xc5\xbd\xc2\xae': '🎮'.encode('utf-8'),     # ðŸŽ® -> 🎮
    b'\xc3\xb0\xc5\xb8\xe2\x80\x9c\xc2\xba': '📺'.encode('utf-8'), # ðŸ“º -> 📺
    b'\xc3\xa2\xc5\x92\xe2\x80\x9b': '⏰'.encode('utf-8'),         # âŒ› -> ⏰
    b'f\xc3\x83\xc2\xbc': 'fü'.encode('utf-8'),                   # fÃ¼ -> fü
    b'H\xc3\x83\xc2\xb6he': 'Höhe'.encode('utf-8'),               # HÃ¶he -> Höhe
    b'Zus\xc3\x83\xc2\xa4tzlicher': 'Zusätzlicher'.encode('utf-8'), # ZusÃ¤tzlicher -> Zusätzlicher
    b'F\xc3\x83\xc2\xbc': 'Für'.encode('utf-8')                    # FÃ¼ -> Für
}

def clean_file(path):
    try:
        with open(path, 'rb') as f:
            content = f.read()
        
        changed = False
        for old_bytes, new_bytes in replacements.items():
            if old_bytes in content:
                content = content.replace(old_bytes, new_bytes)
                changed = True
        
        if changed:
            with open(path, 'wb') as f:
                f.write(content)
            print(f"Cleaned {path}")
        else:
            print(f"No changes needed for {path}")
    except Exception as e:
        print(f"Error cleaning {path}: {e}")

if __name__ == '__main__':
    root_dir = '.'
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file.endswith(('.html', '.js', '.css', '.xml')):
                clean_file(os.path.join(root, file))
