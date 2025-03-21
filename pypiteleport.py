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
    """Check if required dependencies are installed and install them if needed."""
    required = ['build', 'twine']
    missing = []
    
    print("Checking for required dependencies...")
    for package in required:
        try:
            # Try to import the package first (for packages that don't have CLI)
            try:
                __import__(package)
                print(f"✓ {package} is installed")
                continue
            except ImportError:
                pass
                
            # Try to run the package as a module
            result = subprocess.run(
                [sys.executable, '-m', package, '--help'], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                check=False
            )
            if result.returncode == 0:
                print(f"✓ {package} is installed")
            else:
                missing.append(package)
                print(f"✗ {package} is not installed or not working properly")
        except FileNotFoundError:
            missing.append(package)
            print(f"✗ {package} is not installed")
    
    if missing:
        print(f"\nMissing required packages: {', '.join(missing)}")
        install = input("Install them now? (y/n): ").lower()
        if install == 'y':
            print(f"\nInstalling: {', '.join(missing)}...")
            try:
                subprocess.run(
                    [sys.executable, '-m', 'pip', 'install'] + missing, 
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                print("✓ Dependencies installed successfully!")
            except subprocess.CalledProcessError as e:
                print(f"Error installing dependencies: {e}")
                print(e.stderr)
                sys.exit(1)
        else:
            print("Please install the required packages and try again.")
            sys.exit(1)
    else:
        print("All required dependencies are installed.")

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

def get_package_version():
    """Extract the package version from pyproject.toml."""
    try:
        with open('pyproject.toml', 'r') as f:
            for line in f:
                if line.strip().startswith('version = '):
                    # Extract version from the line (handling quotes)
                    version = line.split('=')[1].strip().strip('"\'')
                    return version
    except Exception as e:
        print(f"Error reading version from pyproject.toml: {e}")
    return None

def increment_version(version_str):
    """Increment the patch version number (last part of semver)."""
    parts = version_str.split('.')
    if len(parts) >= 3:
        parts[-1] = str(int(parts[-1]) + 1)
    elif len(parts) == 2:
        parts.append('1')
    elif len(parts) == 1:
        parts.append('0')
        parts.append('1')
    return '.'.join(parts)

def update_version_in_pyproject():
    """Update the version in pyproject.toml by incrementing the patch version."""
    current_version = get_package_version()
    if not current_version:
        print("Could not determine current version.")
        return False
    
    new_version = increment_version(current_version)
    print(f"Incrementing version: {current_version} -> {new_version}")
    
    # Read the entire file
    try:
        with open('pyproject.toml', 'r') as f:
            content = f.read()
        
        # Replace the version
        updated_content = content.replace(
            f'version = "{current_version}"', 
            f'version = "{new_version}"'
        )
        
        # Write back to the file
        with open('pyproject.toml', 'w') as f:
            f.write(updated_content)
        
        return new_version
    except Exception as e:
        print(f"Error updating version in pyproject.toml: {e}")
        return False

def upload_to_pypi(test=False):
    """Upload the package to PyPI using twine."""
    repository_name = "PyPI"
    repository = ''
    
    # Get the package version
    version = get_package_version()
    if version:
        print(f"\n=== Uploading version {version} to {repository_name} ===")
    else:
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
            
            # Check for version conflict error
            if "File already exists" in stderr and "See https://pypi.org/help/#file-name-reuse" in stderr:
                print("\nERROR: Version conflict detected!")
                print("You are trying to upload a version that already exists on PyPI.")
                print("Please update the version number in pyproject.toml and try again.")
                print("\nCurrent version in pyproject.toml:", get_package_version())
                print("Suggestion: Increment the version number (e.g., from 0.1.0 to 0.1.1)")
            
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
    
    try:
        # Check for required dependencies
        check_dependencies()
        
        # Automatically increment version
        current_version = get_package_version()
        if current_version:
            print(f"\nCurrent package version: {current_version}")
            print("Automatically incrementing version number...")
            print("(You can manually edit version in pyproject.toml if needed)")
            new_version = update_version_in_pyproject()
            if not new_version:
                print("Failed to update version. Please update manually in pyproject.toml.")
                proceed = input("Continue anyway? (y/n): ").lower()
                if proceed != 'y':
                    sys.exit(1)
        
        # Clean dist directory
        clean_dist()
        
        # Build the package
        build_package()
        
        # Upload directly to PyPI
        upload_to_pypi()
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nAn unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
