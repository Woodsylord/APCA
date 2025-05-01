
# APCA Server Automation - Feature Roadmap

This document outlines the strategic roadmap for expanding the APCA Server Automation toolkit for Arma 3 mod and server management.

---

## Phase 1: Core Functionality (Complete)

These foundational features have been implemented and packaged:

- **Mod Downloader (`download_mods.py`)**: Automates downloading from Steam using `mods.json`.
- **Sanitizer (`tolower.sh`)**: Normalizes mod folder names for Linux.
- **LGSM Config Updater (`update_lgsm_config.sh`)**: Automatically updates `arma3server.cfg` with the latest mods.
- **Swifty Deployment (`deploy_swifty.sh`)**: Pushes mods to HTTP for client-side syncing.
- **Documentation**: Markdown and PDF guides for server admins.

---

## Phase 2: Quality of Life & Maintenance

### Mod List Diff Tool
Compare `mods.json` with actual mods in `/cmods` and `/omods`. Identify:
- Missing mods
- Extra mods not listed
- Mods with mismatched folder names

### Interactive CLI Menu
User-friendly terminal interface using `dialog` or `whiptail`:
- Add/remove mods from JSON
- Trigger download/deploy
- View logs or summary

### Log Rotation and Summary
Automated log archiving with:
- Date-stamped archives
- Summary reports: success/failures, mod count, runtime

### Mod Dependency Checker
Scan known mods (e.g., ACE, RHS) and ensure dependencies are also listed or installed.

### Self-Check Script
Validates system state:
- Folder permissions
- Disk space
- Internet access
- SteamCMD authentication

---

## Phase 3: User Integration

### Discord Bot Integration
Use Discord to:
- Upload mod lists
- Trigger mod downloads and deployments
- View status updates and logs

Security: restrict to specific roles; log all actions.

### Web Dashboard (Optional: Flask or Node.js)
A lightweight UI with:
- Upload field for HTML or JSON
- Mod list viewer
- Start/stop server buttons
- Logs view
- Auth via password or Discord OAuth

---

## Phase 4: Advanced Features

### Mod Version Tracker
Maintain a local version registry and periodically check Workshop for updates.

Auto-notify or schedule update/download based on flags.

### Auto-Restart on Mod Update
Use `inotify` or polling to monitor mod folders for changes. If a mod is updated:
- Re-run sanitization and LGSM update
- Restart Arma server

### Cloud-Hosted Swifty Sync
Push mods to AWS S3, R2, or another CDN so clients download faster.

Useful for global player bases.

### Backup and Rollback
Keep compressed snapshots of:
- `mods.json`
- Installed mods
- LGSM configs

Allow reversion in case of error or corruption.

---

## Phase 5: Community and Mod Metadata

### Shared Mod Presets
Save and share `mods.json` files:
- Upload to GitHub or web portal
- Tag by mission/scenario

### Mod Tagging and Ratings
Enhance `mods.json` structure:
```json
{
  "id": "123456",
  "name": "ACE",
  "type": "core",
  "tag": "required",
  "rating": 5
}
```

Display in CLI, Discord, or web UI.

---

## Implementation Recommendations

| Phase | Features                                | Complexity | Impact  |
|-------|-----------------------------------------|------------|---------|
| 2     | CLI menu, mod diff, log tools           | Low        | High    |
| 3     | Discord bot, web UI                     | Medium     | High    |
| 4     | Auto updates, rollback, CDN sync        | High       | Medium  |
| 5     | Community tools, rating/tagging         | Medium     | Medium  |

This roadmap offers a robust, modular plan to evolve APCA Server Automation from a command-line toolset into a comprehensive mod and server orchestration suite.
