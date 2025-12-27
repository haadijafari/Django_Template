#!/usr/bin/env python3

"""
Initialize a new Django project from this template.
Replaces placeholder values with user-provided information.
"""

import json
import os
import re
import subprocess
import sys


def get_input(prompt, default=None):
    """Get user input with optional default value."""
    if default:
        prompt = f"{prompt} [{default}]"
    user_input = input(f"{prompt}: ").strip()
    return user_input or default


def slugify(text):
    """Convert text to a valid Python/npm package name."""
    # Remove special characters, convert to lowercase
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug


def update_pyproject_toml(project_name, description):
    """Update pyproject.toml with project information."""
    with open("./backend/pyproject.toml", "r", encoding="utf-8") as f:
        content = f.read()

    # Replace project name
    content = re.sub(
        r'name\s*=\s*"[^"]*"', f'name = "{project_name}"', content, count=1
    )

    # Replace description
    content = re.sub(
        r'description\s*=\s*"[^"]*"', f'description = "{description}"', content, count=1
    )

    with open("./backend/pyproject.toml", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ Updated pyproject.toml")


# TODO: Create a better README template system
def update_readme(project_name, description):
    """Update README.md with project information."""
    if not os.path.exists("README.md"):
        print("⚠️  Warning: README.md not found, skipping")
        return

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Replace project name (first h1 heading)
    content = re.sub(
        r"^# .*$", f"# {project_name}", content, count=1, flags=re.MULTILINE
    )

    # Replace description (line after the h1 heading)
    content = re.sub(
        r"(^# .*\n\n).*$", rf"\1{description}", content, count=1, flags=re.MULTILINE
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ Updated README.md")


def setup_python_environment():
    """Create Python virtual environment and sync dependencies with uv."""
    print("\n🐍 Setting up Python environment...")

    try:
        # Check if uv is installed
        subprocess.run(["uv", "--version"], check=True, capture_output=True)
    except FileNotFoundError:
        print(
            "   ⚠️  uv not found. Install uv, then run 'uv sync' manually in ./backend"
        )
        return False

    try:
        # Run uv sync to create venv and install dependencies
        print("   📦 Running uv sync (this may take a moment)...")
        subprocess.run(["uv", "sync"], check=True, capture_output=True, cwd="./backend")
        print("   ✅ Created virtual environment and installed Python packages")
        print("   ✅ Generated uv.lock")
    except subprocess.CalledProcessError as e:
        print(f"   ❌ uv sync failed: {e}")
        print("   You'll need to run 'uv sync' manually in ./backend")
        return False

    return True


def main():
    """Main initialization process."""
    print("🚀 Django Project Template Initialization\n")

    # Get project information
    project_display_name = get_input("Project name", "My Django Project")
    project_slug = slugify(project_display_name)
    project_slug = get_input("Project slug (for package names)", project_slug)

    description = get_input("Project description", "A Django web application")

    print("\n📋 Summary:")
    print(f"   Display name: {project_display_name}")
    print(f"   Slug: {project_slug}")
    print(f"   Description: {description}")

    confirm = get_input("\nProceed with initialization? (y/n)", "y")
    if confirm.lower() not in ["y", "yes"]:
        print("❌ Initialization cancelled")
        sys.exit(0)

    print("\n🔧 Updating files...")

    # Update files
    update_pyproject_toml(project_slug, description)
    # update_readme(project_display_name, description)

    # Setup dependencies
    uv_success = setup_python_environment()

    print("\n✨ Initialization complete!")
    print("\n📝 Next steps:")
    if not uv_success:
        print('   1. Install uv and run: "cd backend && uv sync"')
    if uv_success:
        print('   1. Run: " backend && uv run manage.py migrate"')
        print("   2. Start building! 🎉")
    else:
        print('   2. Then run: "cd backend && uv run manage.py migrate"')
        print("   3. Start building! 🎉")

    print("\n💡 Optional:")
    print('   - Use "npm init" to setup Node.js dependencies')
    print('   - Use "update_vendors.py" to manage frontend vendor files')

    # Optionally remove the init script
    remove_script = get_input("\nRemove this initialization script? (y/n)", "y")
    if remove_script.lower() in ["y", "yes"]:
        try:
            os.remove(__file__)
            print("✅ Removed init_project.py")
        except Exception as e:
            print(f"⚠️ Could not remove script: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Initialization cancelled")
        sys.exit(1)
