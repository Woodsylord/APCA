#!/usr/bin/env python3
import os
import time
import gzip
import shutil
from datetime import datetime, timedelta

# Configurations
log_dir = "logs"
archive_threshold_days = 7
deletion_threshold_days = 30
summary_filename = "latest_log_summary.txt"

def rotate_and_archive_logs():
    now = time.time()
    for filename in os.listdir(log_dir):
        full_path = os.path.join(log_dir, filename)
        if os.path.isfile(full_path):
            age_days = (now - os.path.getmtime(full_path)) / 86400
            if filename.endswith(".log"):
                if age_days > archive_threshold_days:
                    archive_path = full_path + ".gz"
                    with open(full_path, 'rb') as f_in, gzip.open(archive_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                    os.remove(full_path)
            elif filename.endswith(".gz") and age_days > deletion_threshold_days:
                os.remove(full_path)

def generate_summary():
    log_files = sorted(
        [f for f in os.listdir(log_dir) if f.endswith(".log")],
        key=lambda x: os.path.getmtime(os.path.join(log_dir, x)),
        reverse=True
    )
    if not log_files:
        return

    latest_log_path = os.path.join(log_dir, log_files[0])
    summary_lines = []

    with open(latest_log_path, 'r') as log_file:
        for line in log_file:
            if any(key in line for key in ["Declared Mods", "Actual Mods", "Missing Mods", "Extra Mods", "Deleting"]):
                summary_lines.append(line.strip())

    summary_path = os.path.join(log_dir, summary_filename)
    with open(summary_path, 'w') as summary_file:
        summary_file.write(f"Summary generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        summary_file.write("\n".join(summary_lines))

def main():
    print("Running log maintenance and summary generation...")
    rotate_and_archive_logs()
    generate_summary()
    print(f"Log rotation complete. Summary written to {os.path.join(log_dir, summary_filename)}")

if __name__ == "__main__":
    main()