
#!/bin/bash

# Configuration
MODS_JSON="/home/arma3server/scripts/mods.json"
MODS_BASE_PATH="/home/arma3server/arma3server/serverfiles"
LGSM_CONFIG_DIR="/home/arma3server/arma3server/lgsm/config-lgsm/arma3server"
CFG_FILE="${LGSM_CONFIG_DIR}/arma3server.cfg"
LOG_FILE="/home/arma3server/scripts/logs/update_lgsm_config_$(date +'%Y%m%d_%H%M%S').log"

log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "Updating LGSM mod configuration..."

if [ ! -f "$CFG_FILE" ]; then
    log "Configuration file not found: $CFG_FILE"
    exit 1
fi

if [ ! -f "$MODS_JSON" ]; then
    log "mods.json file not found: $MODS_JSON"
    exit 1
fi

# Read mods.json and generate mod list
MOD_LINE="mods="
MOD_LIST=$(jq -r '.[] | select(.type != "cdlc") | "@\(.name)"' "$MODS_JSON")
CDLC_LIST=$(jq -r '.[] | select(.type == "cdlc") | .name' "$MODS_JSON")

for mod in $MOD_LIST; do
    MOD_LINE+="${mod};"
done

for cdlc in $CDLC_LIST; do
    MOD_LINE+="${cdlc};"
done

# Trim trailing semicolon
MOD_LINE="${MOD_LINE%;}"

# Backup and replace mod line
cp "$CFG_FILE" "${CFG_FILE}.bak"
grep -v '^mods=' "$CFG_FILE" > "${CFG_FILE}.tmp"
echo "$MOD_LINE" >> "${CFG_FILE}.tmp"
mv "${CFG_FILE}.tmp" "$CFG_FILE"

log "Mod line updated in $CFG_FILE"
log "New mod line: $MOD_LINE"
