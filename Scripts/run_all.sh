#!/bin/bash

# Central orchestrator for Phase 1 automation

LOG_DIR="/home/arma3server/scripts/logs"
TIMESTAMP=$(date +'%Y%m%d_%H%M%S')
LOG_FILE="${LOG_DIR}/run_all_${TIMESTAMP}.log"

log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}


log "Running pre-checks..."
if ! python3 self_check.py >> "$LOG_FILE" 2>&1; then
    log "Self-check failed. Please resolve issues above before continuing."
    exit 1
fi
log "Starting full automation sequence..."

cd /home/arma3server/scripts || { log "Failed to enter script directory"; exit 1; }

# Step 1: Download mods
log "Running: download_mods.py"
if python3 download_mods.py >> "$LOG_FILE" 2>&1; then
    log "Mod download completed successfully."
else
    log "Mod download FAILED. Aborting."
    exit 1
fi

# Step 2: Sanitize mod folders
log "Running: tolower.sh"
if bash tolower.sh >> "$LOG_FILE" 2>&1; then
    log "Sanitization completed."
else
    log "Sanitization FAILED. Aborting."
    exit 1
fi

# Step 3: Update LGSM config
log "Running: update_lgsm_config.sh"
if bash update_lgsm_config.sh >> "$LOG_FILE" 2>&1; then
    log "LGSM config updated."
else
    log "LGSM config update FAILED. Aborting."
    exit 1
fi

# Step 4: Deploy to Swifty
log "Running: deploy_swifty.sh"
if bash deploy_swifty.sh >> "$LOG_FILE" 2>&1; then
    log "Swifty deployment completed."
else
    log "Swifty deployment FAILED. Aborting."
    exit 1
fi

log "Full deployment process completed successfully!"


log "Running log maintenance..."
if python3 log_maintenance.py >> "$LOG_FILE" 2>&1; then
    log "Log maintenance completed."
else
    log "Log maintenance failed."
fi
