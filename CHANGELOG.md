
# APCA Server Automation - CDLC Test Branch Changelog

## Branch: APCA_Automation_CDLC_Test

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
