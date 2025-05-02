# APCA Server Automation Toolkit (v1.1)

This project provides a fully automated, modular, and extensible solution for managing mods on a Linux-based Arma 3 dedicated server.

## Contents

### Core Automation Scripts
- `download_mods.py`: Download mods from Steam, rename, extract keys, and move them to the proper location.
- `tolower.sh`: Lowercase mod files/folders for Linux compatibility.
- `update_lgsm_config.sh`: Append mod list to LGSM config.
- `deploy_swifty.sh`: Publish mod folder structure to Swifty repo.
- `run_all.sh`: Full automation orchestrator. Logs output to file.

### Phase 2 Enhancements
- `mod_diff.py`: Detect and optionally delete mods that don’t match the configuration.
- `self_check.py`: Validate environment conditions before any automation.
- `menu.sh`: Terminal-based UI to manage the server.
- `log_maintenance.py`: Rotate/compress/delete logs and generate summaries.
- `mod_dependency_check.py`: Warn about missing dependencies (e.g., ACE requires CBA_A3).

## Usage

```bash
cd /home/arma3server/scripts
bash run_all.sh        # Full automation pipeline
python3 mod_diff.py    # Diff mod state vs config
python3 self_check.py  # Pre-deployment checks
python3 log_maintenance.py  # Log rotation + summary
python3 mod_dependency_check.py  # Dependency checks
bash menu.sh           # Interactive CLI menu
```

## Configuration

All mods are managed via a simple `mods.json`:

```json
[
  { "id": "463939057", "name": "ace", "type": "core" },
  { "id": "751965892", "name": "ACRE2", "type": "core" },
  { "id": "vn", "name": "vn", "type": "cdlc" }
]
```

## Logs

- All scripts write to `/logs/` with timestamped filenames.
- `log_maintenance.py` generates a summary in `latest_log_summary.txt`.

## Security Notes

- Only users with access to `scripts/` can run automation.
- `self_check.py` validates before modification scripts are executed.
- `mod_diff.py` confirms before deleting files.

## Version

**v1.1** – Includes all Phase 2 features.
