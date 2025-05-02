import os
import json

# Configuration
mods_json_path = "mods.json"
cmods_path = "/home/arma3server/arma3server/serverfiles/cmods"
omods_path = "/home/arma3server/arma3server/serverfiles/omods"

def list_mod_folders(path):
    return sorted([f for f in os.listdir(path) if f.startswith("@") and os.path.isdir(os.path.join(path, f))])

def load_mods_json():
    with open(mods_json_path, "r") as f:
        return json.load(f)

def main():
    declared_mods = load_mods_json()
    declared_folders = {"@{}".format(mod['name'].lower()) for mod in declared_mods if mod["type"] in ("core", "optional")}

    actual_cmods = set(list_mod_folders(cmods_path))
    actual_omods = set(list_mod_folders(omods_path))
    actual_mods = actual_cmods.union(actual_omods)

    missing_mods = declared_folders - actual_mods
    extra_mods = actual_mods - declared_folders

    print("\n=== Mod Diff Report ===")
    print(f"Declared Mods: {len(declared_folders)}")
    print(f"Actual Mods  : {len(actual_mods)}")
    print(f"Missing Mods : {len(missing_mods)}")
    print(f"Extra Mods   : {len(extra_mods)}\n")

    if missing_mods:
        print("Missing Mods (declared but not found on disk):")
        for mod in sorted(missing_mods):
            print(f"  - {mod}")
    else:
        print("No missing mods.")

    print()

    if extra_mods:
        print("Extra Mods (found on disk but not in mods.json):")
        for mod in sorted(extra_mods):
            print(f"  - {mod}")
    else:
        print("No extra mods.")

if __name__ == "__main__":
    main()