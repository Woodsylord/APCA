
# APCA Server Automation Changelog

## Branch: APCA_Server_Automation

# Changelog

## [v1.0] - 2025-05-01

### New Features

- **CDLC Support Added**
  - `mods.json` now accepts mods of type `"cdlc"` (e.g. `"vn"`, `"gm"`).
  - CDLCs are appended to the LGSM `mods=` line without "@" prefix.
  - Example CDLCs included in `mods.json`.

### Script Modifications

- **update_lgsm_config.sh**
  - Reads `mods.json` using `jq`.
  - Separates core/optional mods from CDLCs.
  - Builds `mods=` string with both types (e.g. `mods=@ace;@cba_a3;vn;gm`).
  - Skips CDLCs during folder lookup or file checks.

### Unchanged Scripts

- `download_mods.py`: Ignores entries of type `cdlc`.
- `tolower.sh`: No change, CDLCs not touched.
- `deploy_swifty.sh`: Unaffected, CDLCs not deployed via Swifty.
- `README.md` and `README.pdf`: Reference base process (could be updated next).

---

## Compatibility

This branch is fully backward-compatible for Steam Workshop mods. CDLC support is additive and non-intrusive.

## Recommendation

Use this branch if you plan to host missions requiring Arma 3 Creator DLCs. Otherwise, continue using the main automation branch for workshop-only deployments.

## [v1.1] - 2025-05-02

### Added
- `mod_diff.py`: Compares declared vs installed mods, with optional deletion and log output.
- `self_check.py`: Pre-deployment validation of disk space, directories, permissions, and SteamCMD.
- `menu.sh`: Interactive `whiptail`-based menu to run all major automation tools.
- `log_maintenance.py`: Compresses old logs, deletes aged archives, and generates summary reports.
- `mod_dependency_check.py`: Scans for common mod dependency issues and outputs warnings.

### Enhanced
- `run_all.sh` now includes:
  - Integrated self-check
  - Automatic log maintenance
  - Error handling and exit on failure
- All scripts now generate logs in a unified `/logs` directory.

### Documentation
- README files added for each script: usage, examples, and integration notes.
- Phase 2 Summary and Review exported as PDF.
- All scripts packaged under `APCA_Server_Automation_v1.1.zip` for GitHub release.