
import os
import subprocess
import json
from datetime import datetime
from pathlib import Path

# Configuration
STEAMCMD_PATH = "/home/arma3server/.steam/steamcmd"
MODS_JSON = "/home/arma3server/scripts/mods.json"
MODS_BASE_PATH = "/home/arma3server/arma3server/serverfiles"
LOG_DIR = "/home/arma3server/scripts/logs"
LOG_FILE = os.path.join(LOG_DIR, f"download_mods_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# Ensure log directory exists
Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

# Logging function
def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} {message}\n")
    print(f"{timestamp} {message}")

# Load mods
try:
    with open(MODS_JSON, "r") as f:
        mods = json.load(f)
except Exception as e:
    log(f"Failed to load mods.json: {e}")
    exit(1)

# Download mods
for mod in mods:
    mod_id = mod.get("id")
    mod_name = mod.get("name")
    mod_type = mod.get("type", "optional").lower()
    target_dir = "cmods" if mod_type == "core" else "omods"
    mod_dir = f"@{mod_name}"
    destination = os.path.join(MODS_BASE_PATH, target_dir, mod_dir)

    log(f"Starting download for {mod_name} (ID: {mod_id})")

    try:
        steamcmd_script = f"""
        login APCAUnit
        download_item 107410 {mod_id}
        quit
        """
        steamcmd_script_path = os.path.join(STEAMCMD_PATH, "mod_download.txt")
        with open(steamcmd_script_path, "w") as f:
            f.write(steamcmd_script)

        subprocess.run(
            ["./steamcmd.sh", "+runscript", "mod_download.txt"],
            cwd=STEAMCMD_PATH,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        log(f"SteamCMD failed for {mod_name}: {e}")
        continue

    workshop_path = os.path.join(STEAMCMD_PATH, "steamapps", "workshop", "content", "107410", mod_id)
    if not os.path.exists(workshop_path):
        log(f"Downloaded mod directory not found for {mod_id}")
        continue

    try:
        final_path = os.path.join(MODS_BASE_PATH, target_dir, mod_dir)
        if os.path.exists(final_path):
            log(f"Destination already exists: {final_path}, skipping")
            continue
        os.rename(workshop_path, final_path)
        log(f"Moved mod to {final_path}")

        key_path = os.path.join(final_path, "keys")
        server_keys_path = os.path.join(MODS_BASE_PATH, "keys")
        if os.path.exists(key_path):
            for file in os.listdir(key_path):
                if file.endswith(".bikey"):
                    src = os.path.join(key_path, file)
                    dst = os.path.join(server_keys_path, file)
                    subprocess.run(["cp", "-n", src, dst])
                    log(f"Copied key: {file}")
        else:
            log(f"No keys folder found in {final_path}")
    except Exception as e:
        log(f"Error processing mod {mod_name}: {e}")

log("All mods processed.")
