#!/bin/bash

while true; do
    CHOICE=$(whiptail --title "APCA Server Automation" --menu "Choose an action:" 20 78 10 \
        "1" "Run Full Deployment (run_all.sh)" \
        "2" "Run Self-Check (self_check.py)" \
        "3" "Check Mod Differences (mod_diff.py)" \
        "4" "View Latest Log" \
        "5" "Run Log Maintenance (log_maintenance.py)" \
        "6" "Check Mod Dependencies (mod_dependency_check.py)" \
        "7" "Exit" 3>&1 1>&2 2>&3)

    exitstatus=$?
    if [ $exitstatus != 0 ]; then
        echo "User exited."
        break
    fi

    case $CHOICE in
        1)
            bash run_all.sh
            ;;
        2)
            python3 self_check.py
            ;;
        3)
            python3 mod_diff.py
            ;;
        4)
            LAST_LOG=$(ls -t logs/*.log 2>/dev/null | head -n 1)
            if [ -f "$LAST_LOG" ]; then
                whiptail --textbox "$LAST_LOG" 40 100
            else
                whiptail --msgbox "No logs found." 10 50
            fi
            ;;
        5)
            python3 log_maintenance.py
            ;;
        6)
            python3 mod_dependency_check.py
            ;;
        7)
            break
            ;;
    esac
done
