import hashlib
import json
import os
import shutil
import subprocess
import sys


def load_config(config_path="./update_vendor_config.json"):
    """Load file mappings from JSON config file."""
    if not os.path.exists(config_path):
        print(f"❌ Error: Config file not found: {config_path}")
        sys.exit(1)

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        # Validate config structure
        if "files" not in config:
            print("❌ Error: Config file must contain a 'files' array")
            sys.exit(1)

        # Convert to list of tuples (src, dest)
        files = []
        for item in config["files"]:
            if "src" not in item or "dest" not in item:
                print(f"⚠️ Warning: Skipping invalid entry (missing src/dest): {item}")
                continue
            files.append((item["src"], item["dest"]))

        if not files:
            print("⚠️ Warning: No valid file mappings found in config")

        return files

    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in config file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error loading config: {e}")
        sys.exit(1)


def install_node_modules():
    """
    Runs 'npm install' to ensure node_modules are up to date
    based on package.json and package-lock.json.
    """
    if not os.path.exists("package.json"):
        print("⚠️ Warning: package.json not found. Skipping npm install.")
        return

    # Check if npm install is already running
    if os.path.exists("package-lock.json.lock"):
        print("⚠️ Warning: Another npm install may be running. Waiting...")

    print("🔄 Installing/Updating Node modules...")

    try:
        # Determine the correct npm command based on the operating system
        # Windows requires 'npm.cmd', others use 'npm'
        npm_command = "npm.cmd" if os.name == "nt" else "npm"

        # Run npm install
        subprocess.run([npm_command, "install"], check=True)
        print("✅ Node modules installed successfully.")

    except subprocess.CalledProcessError:
        print("❌ Error: 'npm install' failed.")
        sys.exit(1)
    except FileNotFoundError:
        print(
            "❌ Error: npm command not found. Please ensure Node.js is installed and in your PATH."
        )
        sys.exit(1)


def verify_sources(files):
    """Verify all source files exist before copying."""
    missing = [src for src, _ in files if not os.path.exists(src)]
    if missing:
        print("❌ Missing source files:")
        for f in missing:
            print(f"   - {f}")
        return False
    return True


def files_are_identical(src, dest):
    """Check if source and destination files are identical."""
    if not os.path.exists(dest):
        return False

    def get_hash(filepath):
        with open(filepath, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    try:
        return get_hash(src) == get_hash(dest)
    except Exception:
        return False


if __name__ == "__main__":
    # 1. Load configuration
    print("📋 Loading configuration...")
    files = load_config()
    print(f"   Found {len(files)} file mapping(s)")

    # 2. Update modules
    install_node_modules()

    # 3. Verify sources exist
    if not verify_sources(files):
        print("\n❌ Cannot proceed: Some source files are missing")
        sys.exit(1)

    # 4. Copy files with statistics
    print("\n📦 Starting file copy...")
    success_count = 0
    failed_count = 0
    skipped_count = 0

    for src, dest in files:
        try:
            # Skip if files are identical
            if files_are_identical(src, dest):
                print(f"   ⏭️  Skipped (unchanged): {dest}")
                skipped_count += 1
                continue

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(dest), exist_ok=True)

            # Copy file
            shutil.copyfile(src, dest)
            print(f"   ✅ Updated: {dest}")
            success_count += 1

        except FileNotFoundError:
            print(f"   ❌ Error: Source file not found: {src}")
            failed_count += 1
        except PermissionError:
            print(f"   ❌ Error: Permission denied: {dest}")
            failed_count += 1
        except Exception as e:
            print(f"   ❌ Error copying {src}: {e}")
            failed_count += 1

    # 5. Print summary
    print(
        f"\n📊 Summary: {success_count} updated, {skipped_count} skipped, {failed_count} failed"
    )

    if failed_count > 0:
        print("⚠️ Warning: Some files failed to copy")
        sys.exit(1)
    else:
        print("🎉 Vendor files updated successfully!")
