#!/usr/bin/env python3
import json

mods_json_path = "mods.json"

# Define a basic dependency map
DEPENDENCIES = {
    "ace": ["cba_a3"],
    "rhsusaf": ["rhsafrf"],
    "rhsgref": ["rhsafrf"],
    "rhssaf": ["rhsafrf"],
    "cup_terrains_maps": ["cup_terrains_core"],
    "cup_terrains_cwa": ["cup_terrains_core"],
    "project_opfor": ["cba_a3"],
    "3cb_factions": ["cba_a3", "rhsusaf", "rhsgref", "rhsafrf"]
}

def load_mods_json():
    try:
        with open(mods_json_path, "r") as f:
            return [mod["name"].lower() for mod in json.load(f) if mod["type"] in ("core", "optional")]
    except Exception as e:
        print(f"[ERROR] Failed to read or parse mods.json: {e}")
        return []

def check_dependencies(mod_list):
    missing = {}
    for mod in mod_list:
        required = DEPENDENCIES.get(mod, [])
        for dep in required:
            if dep not in mod_list:
                if mod not in missing:
                    missing[mod] = []
                missing[mod].append(dep)
    return missing

def main():
    print("=== Mod Dependency Check ===")
    mods = load_mods_json()
    if not mods:
        print("No mods found or mods.json is invalid.")
        return

    missing_deps = check_dependencies(mods)

    if not missing_deps:
        print("[OK] All dependencies satisfied.")
    else:
        print("[WARNING] Missing dependencies detected:")
        for mod, deps in missing_deps.items():
            print(f"  - {mod} is missing: {', '.join(deps)}")

if __name__ == "__main__":
    main()