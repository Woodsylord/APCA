# `menu.sh` - Interactive CLI Menu

This script provides a simple, user-friendly menu for managing your Arma 3 server automation tasks using `whiptail`.

## Features

- Run the full deployment pipeline via `run_all.sh`
- Run environment self-checks
- Check for missing or extra mods
- View the most recent log file
- Exit safely

## Usage

1. SSH into your server.
2. Navigate to the scripts directory:

```bash
cd /home/arma3server/scripts
```

3. Run the menu:

```bash
bash menu.sh
```

4. Use the arrow keys or number keys to select an option.

## Example Menu

```
+------------------------------------------+
|        APCA Server Automation            |
| Choose an action:                        |
|------------------------------------------|
| 1 - Run Full Deployment (run_all.sh)     |
| 2 - Run Self-Check (self_check.py)       |
| 3 - Check Mod Differences (mod_diff.py)  |
| 4 - View Latest Log                      |
| 5 - Exit                                 |
+------------------------------------------+
```

## Requirements

- `whiptail` must be installed on your system.
- Ensure `run_all.sh`, `self_check.py`, and `mod_diff.py` exist in the same directory.

### Install `whiptail` (Debian/Ubuntu)

```bash
sudo apt update && sudo apt install whiptail
```

---