# `mod_diff.py` - Modset Difference Checker

This script compares the declared mods in `mods.json` with the actual folders installed in `/cmods` and `/omods`.

## 🔍 What It Detects

- **Missing Mods**: Mods listed in `mods.json` that are not found on disk
- **Extra Mods**: Mod folders found on disk that are not listed in `mods.json`

## ▶️ Usage

```bash
cd /home/arma3server/scripts
python3 mod_diff.py
```

## ✅ Output Example

```
=== Mod Diff Report ===
Declared Mods: 5
Actual Mods  : 4
Missing Mods : 1
Extra Mods   : 0

Missing Mods:
  - @some_mod_not_on_disk
```

## 🧠 Notes

- Only checks `core` and `optional` mods — CDLCs are ignored
- Folder names are normalized to lowercase
- Uses `@modname` folder naming convention

## 📁 Requirements

- Valid `mods.json` in the same directory
- Mod folders in `/cmods` or `/omods`