#!/usr/bin/env python3
import os
import shutil
import json
import subprocess

def check_directory(path, name):
    if os.path.isdir(path):
        print(f"[OK] {name} directory exists.")
    else:
        print(f"[ERROR] {name} directory does NOT exist: {path}")

def check_permissions(path, name):
    if os.access(path, os.R_OK | os.W_OK):
        print(f"[OK] Read/write access to {name}.")
    else:
        print(f"[ERROR] No read/write access to {name}.")

def check_disk_space(path):
    total, used, free = shutil.disk_usage(path)
    if free < 2 * 1024**3:  # Less than 2GB
        print(f"[WARNING] Low disk space on {path}: {free // (1024**2)} MB free")
    else:
        print(f"[OK] Disk space is sufficient on {path}.")

def check_mods_json(path):
    try:
        with open(path, "r") as f:
            json.load(f)
        print(f"[OK] mods.json is valid JSON.")
    except Exception as e:
        print(f"[ERROR] mods.json is invalid: {e}")

def check_steamcmd():
    result = subprocess.run(["which", "steamcmd"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"[OK] steamcmd found at {result.stdout.strip()}")
    else:
        print("[ERROR] steamcmd not found in PATH.")

def main():
    print("=== Self-Check Report ===")
    check_directory("/home/arma3server/arma3server/serverfiles/cmods", "cmods")
    check_directory("/home/arma3server/arma3server/serverfiles/omods", "omods")
    check_directory("/home/arma3server/scripts/logs", "logs")
    check_permissions("/home/arma3server/scripts", "scripts directory")
    check_mods_json("/home/arma3server/scripts/mods.json")
    check_disk_space("/")
    check_steamcmd()
    print("=== Self-Check Complete ===")

if __name__ == "__main__":
    main()
