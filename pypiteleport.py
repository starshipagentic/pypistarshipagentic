#!/usr/bin/env python3
"""
PyPI Teleport - A utility script to build and upload packages to PyPI.
"""

import os
import sys
import subprocess
import getpass
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

def upload_to_pypi(test=False):
    """Upload the package to PyPI using twine."""
    repository = '--repository-url https://test.pypi.org/legacy/' if test else ''
    
    print("\n=== Uploading to PyPI ===")
    print("Please enter your PyPI API token:")
    token = getpass.getpass()
    
    # Set environment variables for twine
    env = os.environ.copy()
    env['TWINE_USERNAME'] = '__token__'
    env['TWINE_PASSWORD'] = token
    
    cmd = f"{sys.executable} -m twine upload {repository} dist/*"
    print(f"\nRunning: {cmd}")
    
    result = subprocess.run(
        cmd,
        shell=True,
        env=env,
        capture_output=True,
        text=True,
        check=False
    )
    
    if result.returncode != 0:
        print("Error uploading to PyPI:")
        print(result.stderr)
        sys.exit(1)
    
    print("\nPackage uploaded successfully!")
    
    if test:
        print("\nYour package is now available on TestPyPI.")
        print("You can install it with:")
        print(f"pip install --index-url https://test.pypi.org/simple/ your-package-name")
    else:
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
    
    # Ask if user wants to upload to TestPyPI first
    test_first = input("\nDo you want to upload to TestPyPI first? (y/n): ").lower() == 'y'
    if test_first:
        upload_to_pypi(test=True)
        proceed = input("\nDo you want to proceed with uploading to PyPI? (y/n): ").lower() == 'y'
        if not proceed:
            print("Upload to PyPI canceled.")
            return
    
    # Upload to PyPI
    upload_to_pypi()

if __name__ == "__main__":
    main()
