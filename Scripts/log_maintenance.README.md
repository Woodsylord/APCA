# `log_maintenance.py` - Log Rotation and Summary Tool

This tool manages your automation logs to help reduce clutter and provide quick insights into recent mod deployments.

## Features

- 🔁 Compress logs older than 7 days (`.log.gz`)
- 🧹 Delete archived logs older than 30 days
- 📄 Generate summary reports from the most recent log

## Usage

Run it manually:
```bash
cd /home/arma3server/scripts
python3 log_maintenance.py
```

Or, let it run automatically as part of `run_all.sh`.

## Output

- Compressed logs saved in: `logs/*.gz`
- Summary file: `logs/latest_log_summary.txt`

### Example Summary:
```
Summary generated on 2025-05-02 11:42:10

Declared Mods: 7
Actual Mods  : 6
Missing Mods : 1
Extra Mods   : 2
Deleting /home/arma3server/arma3server/serverfiles/omods/@outdated_mod...
```

## Settings

- Edit the script to change:
  - `archive_threshold_days` (default: 7)
  - `deletion_threshold_days` (default: 30)

## Notes

- Only `.log` files are rotated or summarized
- Automatically runs at the end of `run_all.sh`