
#!/bin/bash

# Configuration
SWIFTY_DIR="/home/swifty"
SWIFTY_CMD="sudo mono swifty.exe create /home/arma3server/arma3server/serverfiles/apca_operations.json /var/www/html/oprepo"
LOG_FILE="/home/arma3server/scripts/logs/deploy_swifty_$(date +'%Y%m%d_%H%M%S').log"

log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "Starting Swifty deployment..."

cd "$SWIFTY_DIR" || { log "Failed to navigate to $SWIFTY_DIR"; exit 1; }

if $SWIFTY_CMD >> "$LOG_FILE" 2>&1; then
    log "Swifty deployment completed successfully."
else
    log "Swifty deployment encountered errors. Check the log for details."
    exit 1
fi
