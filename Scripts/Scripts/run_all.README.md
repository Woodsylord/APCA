# `run_all.sh` - Full Automation Orchestrator

This script executes the entire Arma 3 server mod deployment pipeline in one step.

## 🔧 What It Does

- Downloads mods listed in `mods.json` using `download_mods.py`
- Sanitizes mod folders with `tolower.sh`
- Updates the LGSM server configuration using `update_lgsm_config.sh`
- Deploys the mod list to Swifty using `deploy_swifty.sh`
- Logs all steps and outputs to a dated log file in `logs/`

## ▶️ Usage

Run the script as the `arma3server` user:

```bash
cd /home/arma3server/scripts
bash run_all.sh
```

The log will be saved to:

```
/home/arma3server/scripts/logs/run_all_YYYYMMDD_HHMMSS.log
```

## ⚠️ Error Handling

- If any script step fails, the orchestrator logs the failure and exits
- Review logs for issues before retrying

## 📋 Requirements

- All individual scripts (`download_mods.py`, `tolower.sh`, etc.) must exist in the same directory
- Run with standard Linux permissions (no root required)

## 📁 Files

- `run_all.sh` — the script itself
- `run_all.README.md` — this documentation

## 🔐 Security Notes

- Ensure the script is only executable by trusted users
- Avoid editing `mods.json` manually while this is running