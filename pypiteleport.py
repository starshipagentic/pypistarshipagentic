#!/usr/bin/env python3
"""
PyPI Teleport - A utility script to build and upload packages to PyPI.
"""

import os
import sys
import subprocess
import getpass
import json
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed."""
    required = ['build', 'twine']
    missing = []
    
    for package in required:
        try:
            subprocess.run(
                [sys.executable, '-m', package, '--help'], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                check=False
            )
        except FileNotFoundError:
            missing.append(package)
    
    if missing:
        print(f"Missing required packages: {', '.join(missing)}")
        install = input("Install them now? (y/n): ").lower()
        if install == 'y':
            subprocess.run([sys.executable, '-m', 'pip', 'install'] + missing, check=True)
        else:
            print("Please install the required packages and try again.")
            sys.exit(1)

def clean_dist():
    """Clean the dist directory."""
    dist_dir = Path('dist')
    if dist_dir.exists():
        print("Cleaning dist directory...")
        for file in dist_dir.glob('*'):
            file.unlink()
    else:
        dist_dir.mkdir()

def build_package():
    """Build the package using the build module."""
    print("\n=== Building package ===")
    result = subprocess.run(
        [sys.executable, '-m', 'build'], 
        capture_output=True,
        text=True,
        check=False
    )
    
    if result.returncode != 0:
        print("Error building package:")
        print(result.stderr)
        sys.exit(1)
    
    print("Package built successfully!")
    
    # List the built files
    dist_files = list(Path('dist').glob('*'))
    if dist_files:
        print("\nBuilt files:")
        for file in dist_files:
            print(f"  - {file.name}")
    else:
        print("No files were built. Check for errors.")
        sys.exit(1)

def get_stored_token(test=False):
    """Get stored token from ~/.pypi-keys.json file."""
    token_file = Path.home() / ".pypi-keys.json"
    key = 'testpypi' if test else 'pypi'
    
    if token_file.exists():
        try:
            with open(token_file, 'r') as f:
                tokens = json.load(f)
                return tokens.get(key)
        except (json.JSONDecodeError, IOError):
            return None
    return None

def store_token(token, test=False):
    """Store token in ~/.pypi-keys.json file."""
    token_file = Path.home() / ".pypi-keys.json"
    tokens = {}
    key = 'testpypi' if test else 'pypi'
    
    # Read existing tokens if file exists
    if token_file.exists():
        try:
            with open(token_file, 'r') as f:
                tokens = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    
    # Update token and write back to file
    tokens[key] = token
    with open(token_file, 'w') as f:
        json.dump(tokens, f)
    
    # Set secure permissions
    os.chmod(token_file, 0o600)

def upload_to_pypi(test=False):
    """Upload the package to PyPI using twine."""
    repository_name = "PyPI"
    repository = ''
    
    print(f"\n=== Uploading to {repository_name} ===")
    
    # Try to get stored token
    stored_token = get_stored_token(test=False)
    if stored_token:
        # Display masked token
        masked_token = f"{stored_token[:6]}...{stored_token[-4:]}"
        response = input(f"Use stored {repository_name} token ({masked_token})? (y/n) [y]: ").lower()
        if response == '' or response == 'y':
            token = stored_token
        else:
            print(f"Please enter your {repository_name} API token:")
            token = getpass.getpass()
            store_token(token, test=False)
    else:
        print(f"Please enter your {repository_name} API token:")
        token = getpass.getpass()
        store_token(token, test=False)
    
    # Set environment variables for twine
    env = os.environ.copy()
    env['TWINE_USERNAME'] = '__token__'
    env['TWINE_PASSWORD'] = token
    
    cmd = f"{sys.executable} -m twine upload {repository} dist/* --verbose"
    print(f"\nRunning: {cmd}")
    
    # Run with output streaming to console for better visibility
    try:
        process = subprocess.Popen(
            cmd,
            shell=True,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        
        # Print output in real-time
        print("\n--- Output ---")
        for line in process.stdout:
            print(line.strip())
        
        # Wait for process to complete
        return_code = process.wait()
        
        # Get any remaining stderr
        stderr = process.stderr.read()
        
        if return_code != 0:
            print("\n--- Error ---")
            print(stderr)
            sys.exit(1)
    except Exception as e:
        print(f"\nException during upload: {str(e)}")
        sys.exit(1)
    
    print("\nPackage uploaded successfully!")
    
    print("\nYour package is now available on PyPI.")
    print("Users can install it with:")
    print("pip install starshipagentic")

def main():
    """Main function."""
    print("🚀 PyPI Teleport - Build and upload packages to PyPI 🚀")
    
    # Check for required dependencies
    check_dependencies()
    
    # Clean dist directory
    clean_dist()
    
    # Build the package
    build_package()
    
    # Upload directly to PyPI
    upload_to_pypi()

if __name__ == "__main__":
    main()
