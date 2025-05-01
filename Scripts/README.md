
# Arma 3 Mod Automation Guide

This guide describes how to use the Arma 3 automation tools on a Linux server using LGSM and Swifty.

## Included Tools

- `download_mods.py` - Downloads and installs Steam mods from `mods.json`.
- `tolower.sh` - Sanitizes mod folder and filenames.
- `update_lgsm_config.sh` - Updates the LGSM server config with current mods.
- `deploy_swifty.sh` - Publishes the modset to Swifty for client syncing.
- `mods.json` - Define your list of Steam mods here.

## Setup Instructions

```bash
tar -xzvf APCA_Server_Automation_package_final.tar.gz -C /home/arma3server
cd /home/arma3server/scripts/APCA_Server_Automation/scripts
```

## Step 1: Define Mods in mods.json

Example:
```json
[
  {
    "id": "463939057",
    "name": "ace",
    "type": "core"
  },
  {
    "id": "751965892",
    "name": "ACRE2",
    "type": "optional"
  }
]
```

- "id" = Steam Workshop ID
- "name" = Folder name (renamed to @name)
- "type" = core or optional

## Step 2: Download Mods

```bash
python3 download_mods.py
```

- Downloads each mod
- Renames to @modname
- Moves to /cmods/ or /omods/
- Copies .bikey files to /serverfiles/keys

## Step 3: Sanitize Mod Folders

```bash
bash tolower.sh
```

- Lowercases all folders/files
- Replaces spaces with underscores

## Step 4: Update LGSM Config

```bash
bash update_lgsm_config.sh
```

- Updates arma3server.cfg with installed mods
- Creates backup before changes

## Step 5: Deploy to Swifty

```bash
bash deploy_swifty.sh
```

- Runs:
  sudo mono swifty.exe create ...
- Publishes modset for client syncing

## Log Files

All actions are logged in:
/home/arma3server/scripts/APCA_Server_Automation/scripts/logs/


---

## CDLC Support (Creator DLCs)

Arma 3 CDLCs (like SOG Prairie Fire, Global Mobilization, etc.) are not downloaded via SteamCMD. They must be:

1. Installed manually via the full Steam client on the server.
2. Specified in `mods.json` using type `"cdlc"`.

Example entry:
```json
{
  "id": "vn",
  "name": "vn",
  "type": "cdlc"
}
```

- These are appended to the LGSM `mods=` config line without the `@` prefix.
- They are not downloaded or deployed via Swifty.
- All clients must own the CDLC to join sessions using them.

CDLCs like `vn`, `gm`, `csla`, and `ws` are supported.

