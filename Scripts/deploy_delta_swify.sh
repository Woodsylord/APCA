#!/bin/bash

# === deploy_delta_swifty.sh ===
# Deploy only changed mods using mod_versions_cache.json + Swifty
# Usage: ./deploy_delta_swifty.sh <swifty_config_json> <target_repo_dir>

set -euo pipefail

# ---- CONFIG ----
CMODS_DIR="/home/arma3server/arma3server/serverfiles/cmods"
OMODS_DIR="/home/arma3server/arma3server/serverfiles/omods"
STAGING_DIR="/var/www/html/oprepo_staging"
LOG_FILE="/home/arma3server/scripts/logs/deploy_delta.log"
MOD_CACHE="/home/arma3server/scripts/mod_versions_cache.json"
MOD_TRACKER="/home/arma3server/scripts/mod_version_tracker.py"

# ---- ARGS ----
SWIFTY_JSON="${1:-}"
TARGET_REPO="${2:-/var/www/html/oprepo}"

if [[ -z "$SWIFTY_JSON" || -z "$TARGET_REPO" ]]; then
  echo "Usage: $0 <swifty_json_config> <target_repo_dir>"
  exit 1
fi

echo "🔄 Starting Delta Deployment..." | tee -a "$LOG_FILE"

# ---- RUN VERSION TRACKER ----
echo "📦 Detecting changed mods..." | tee -a "$LOG_FILE"
python3 "$MOD_TRACKER" >> "$LOG_FILE" 2>&1

# ---- Read changed mods ----
CHANGED_MODS=$(python3 -c "
import json
with open('$MOD_CACHE') as f:
    current = json.load(f)
try:
    with open('$MOD_CACHE.prev') as f:
        old = json.load(f)
except:
    old = {}

changed = [mod for mod in current if mod not in old or current[mod]['hash'] != old.get(mod, {}).get('hash')]
print(' '.join(changed))
")

if [[ -z "$CHANGED_MODS" ]]; then
  echo '✅ No mods changed. Skipping deployment.' | tee -a "$LOG_FILE"
  exit 0
fi

# ---- Prepare Staging Area ----
echo "🚧 Preparing staging area..." | tee -a "$LOG_FILE"
rm -rf "$STAGING_DIR"
mkdir -p "$STAGING_DIR"

# ---- Copy Changed Mods ----
for MOD in $CHANGED_MODS; do
  SRC=""
  [[ -d "$CMODS_DIR/$MOD" ]] && SRC="$CMODS_DIR/$MOD"
  [[ -d "$OMODS_DIR/$MOD" ]] && SRC="$OMODS_DIR/$MOD"
  if [[ -n "$SRC" ]]; then
    echo "🔁 Copying $MOD..." | tee -a "$LOG_FILE"
    cp -r "$SRC" "$STAGING_DIR/"
  else
    echo "⚠️ Mod $MOD not found in cmods or omods" | tee -a "$LOG_FILE"
  fi
done

# ---- Run Swifty ----
echo "🚀 Running Swifty to create updated repo..." | tee -a "$LOG_FILE"
sudo mono swifty.exe create "$SWIFTY_JSON" "$STAGING_DIR" >> "$LOG_FILE" 2>&1

# ---- Sync to Live Repo ----
echo "🔃 Syncing staging to live repo at $TARGET_REPO..." | tee -a "$LOG_FILE"
rsync -a --delete "$STAGING_DIR/" "$TARGET_REPO/" >> "$LOG_FILE" 2>&1

# ---- Archive current mod cache as .prev and update new cache ----
cp "$MOD_CACHE" "$MOD_CACHE.prev"

echo "✅ Delta deployment complete." | tee -a "$LOG_FILE"
