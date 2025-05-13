#!/usr/bin/env -S uv run --script

import subprocess
import os
import sys
from dotenv import load_dotenv

load_dotenv()

prompt = "You are a software engineer. First git checkout a new branch. CREATE a todo.py: a minimal cli todo application. Then commit your changes."

# Using the full path to the PowerShell script
codex_path = r"C:\ProgramData\global-npm\codex.ps1"
command = ["pwsh", "-Command", f"& '{codex_path}' --approval-mode full-auto '{prompt}'"]

print(f"Running command: {' '.join(command)}")

try:
    subprocess.run(command, check=True)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
