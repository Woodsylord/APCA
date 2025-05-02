# `mod_dependency_check.py` - Mod Dependency Checker

This script checks your `mods.json` configuration for missing dependencies among commonly used Arma 3 mods.

## ✅ What It Detects

- Mods that typically rely on others (e.g., ACE requiring CBA_A3)
- Warnings when required mods are not listed

## ▶️ Usage

Run the tool manually:

```bash
cd /home/arma3server/scripts
python3 mod_dependency_check.py
```

## 🧠 Example Output

```
=== Mod Dependency Check ===
[WARNING] Missing dependencies detected:
  - ace is missing: cba_a3
  - rhsusaf is missing: rhsafrf
```

## 💡 Supported Dependencies

| Mod             | Requires               |
|------------------|------------------------|
| ace              | cba_a3                 |
| rhsusaf          | rhsafrf                |
| rhsgref          | rhsafrf                |
| rhssaf           | rhsafrf                |
| cup_terrains_maps| cup_terrains_core      |
| project_opfor    | cba_a3                 |
| 3cb_factions     | cba_a3, rhsusaf, rhsgref, rhsafrf |

## 🔧 Customization

To add your own dependency rules, edit the `DEPENDENCIES` dictionary inside the script.