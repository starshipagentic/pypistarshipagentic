#!/usr/bin/env python3
import os
import sys

LICENSE_HEADER_FILE = "LICENSE_HEADER.txt"
TARGET_EXTENSIONS = [".py"]

def get_license_header():
    """Read and return the license header from LICENSE_HEADER.txt."""
    try:
        with open(LICENSE_HEADER_FILE, "r", encoding="utf-8") as f:
            return f.read().rstrip()
    except FileNotFoundError:
        print(f"Error: {LICENSE_HEADER_FILE} not found.")
        sys.exit(1)

def insert_license_header(file_path, header):
    """Insert the license header into a file if not already present."""
    with open(file_path, "r", encoding="utf-8") as f:
        contents = f.read()

    # Skip files that already include the header (using a unique identifier)
    if "Starship Agentic License Header" in contents:
        print(f"Skipping {file_path}: header already present.")
        return

    lines = contents.splitlines(keepends=True)
    new_contents = ""
    if lines and lines[0].startswith("#!"):
        # Preserve shebang line and insert header after it
        new_contents = lines[0] + header + "\n" + "".join(lines[1:])
    else:
        new_contents = header + "\n" + "".join(lines)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_contents)
    print(f"Added header to {file_path}")

def process_directory(root_dir, header):
    """Recursively process all Python files in the given directory."""
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in TARGET_EXTENSIONS):
                file_path = os.path.join(dirpath, filename)
                insert_license_header(file_path, header)

def main():
    header = get_license_header()
    target_dirs = ["."]
    for d in target_dirs:
        process_directory(d, header)

if __name__ == "__main__":
    main()
