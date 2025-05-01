# APCA Server Automation

Automation framework for managing Arma 3 multiplayer server mods using SteamCMD, Swifty, and LGSM. Includes support for both Steam Workshop mods and Creator DLC (CDLC).

## Features

- Download and install mods from SteamCMD
- Rename and sanitize folders for Linux compatibility
- Automatically update LGSM mod configuration
- Deploy mods to HTTP with Swifty
- Handle CDLC entries (e.g., `vn`, `gm`)
- Modular scripts and logs
- Markdown and PDF documentation

## Getting Started

```bash
# Extract and enter directory
tar -xzvf APCA_Server_Automation.tar.gz
cd APCA_Server_Automation/scripts

# Configure your mods
nano mods.json

# Download mods
python3 download_mods.py

# Sanitize file/folder names
bash tolower.sh

# Update LGSM config
bash update_lgsm_config.sh

# Deploy to Swifty
bash deploy_swifty.sh
```

## File Structure

- `scripts/` – Core scripts and mod manager tools
- `logs/` – Log files generated from each run
- `mods.json` – Your list of mods (core, optional, CDLC)
- `README.md` – Usage guide
- `README.pdf` – Printable guide
- `CHANGELOG.md` – CDLC test branch updates
- `APCA_Server_Automation_Roadmap.md` – Feature roadmap
- `APCA_Server_Automation_Roadmap_Monday.xlsx/csv` – Import into Monday.com
- `APCA_Server_Automation_Release_Roadmap.xlsx/csv` – Version tracking

## License

MIT License

## Contributing

Pull requests welcome. Please fork the project and submit a merge request to the `dev` branch.