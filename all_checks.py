#!/usr/bin/env python3
import os
import shutil
import sys

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)

def check_disk_full(disk, min_absolute, min_percent):
    if min_absolute > 2:
        return disk
    if min_percent < 19:
        print("All good")
    sys.exit(0)

main()
