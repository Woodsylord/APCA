# Changelog

## [v1.3] - 2025-05-02

### Added
- `deploy_delta_swifty.sh`: Optional standalone script for Delta Deployment.
  - Detects which mods have changed since last deployment (based on `mod_versions_cache.json`)
  - Copies only changed mods from `/cmods` and `/omods` to a staging directory
  - Runs `mono swifty.exe create` only on changed mod set
  - Syncs to live Swifty repo with `rsync`
  - Logs the process to `deploy_delta.log`
  - Falls back gracefully if no mods have changed

---

**Status:** Optional  
**Location:** `/home/arma3server/scripts/deploy_delta_swifty.sh`  
**Package:** `APCA_Server_Automation_v1.3`